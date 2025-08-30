from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from loguru import logger
import concurrent.futures
import json
from config.llm_client import get_llm

INSTRUCTION = """Translate the provided COBOL statements into natural language sentences while preserving clarity and meaning. Each translation should maintain the sequence of up to 10 statements without overly focusing on nested structures. Use mathematical symbols (+, -, *, /, =, <, >) when suitable and replace outdated terms with modern equivalents. Enclose variables in HTML-like tags, such as `<var>name_of_variable</var>`, `<para>name_of_variable</para>`, or `<sub>name_of_variable</sub>` for clear identification.

### Steps

1. **Extract Statements**: Identify up to 10 statements from the COBOL code, ensuring they are distinct and individually translatable.
2. **Translation**: Convert each statement into natural language sentences using necessary mathematical symbols.
3. **Modernize Language**: Where appropriate, utilize modern terms for better comprehension.
4. **Tagging Variables**: Enclose each variable within designated tags for clarity.
5. **Detail Clarification**: Ensure all necessary details are included; do not omit any statement features.

### Output Format

- Present the output in a JSON format containing fields: `statement`, `explanation`, and `start_idx`.
- Each JSON object should accurately reflect the translated statements and maintain a valid JSON structure.

### Examples

- **Statements:** "ADD 1 TO FIND-CNT CNT-1000.", "IF CNT-1000 > 999", "MOVE 0 TO CNT-1000."
  - **JSON:**
    [
      {{
        "statement": "ADD 1 TO FIND-CNT CNT-1000.",
        "explanation": "Add 1 to both <var>FIND-CNT</var> and <var>CNT-1000</var>.",
        "start_idx": [position in source code]
      }},
      {{
        "statement": "IF CNT-1000 > 999",
        "explanation": "Check if <var>CNT-1000</var> > 999.",
        "start_idx": [position in source code]
      }}
      {{
        "statement": "MOVE 0 TO CNT-1000.",
        "explanation": "Move 0 to <var>CNT-1000</var>.",
        "start_idx": [position in source code]
      }}
    ]

- **Statements:** "CALL 'GETDATETIME OF DIANASYS/ALIB0010' USING LIB-DT-INTERFACE", "EXIT"
  - **JSON:**
    [
      {{
        "statement": "CALL 'GETDATETIME OF DIANASYS/ALIB0010' USING LIB-DT-INTERFACE",
        "explanation": "Call the <sub>'GETDATETIME'</sub> subroutine from DIANASYS/ALIB0010 that employs <var>LIB-DT-INTERFACE</var> to retrieve the current time.",
        "start_idx": [position in source code]
      }},
      {{
        "statement": "EXIT",
        "explanation": "Exit the [Name of paragraph or section].",
        "start_idx": [position in source code]
      }}
    ]

### Notes

- Maintain the semantic integrity of COBOL statements.
- Prioritize clarity to ensure all translated segments are easily understandable.
- Accurately include the `start_idx` for each translation segment, making sure no statements are missed.

{CODE}
"""

class Statement(BaseModel):
    translation: Optional[str] = Field(description='The statement translation in natural language')
    start_idx: Optional[int] = Field(description='The start index of the statement in the source code are provided in the original code')
    nested_statements: Optional[List['Statement']] = Field(default=None, description='Nested statements if any inside IF, PERFORM UNTIL, etc.')

class Statements(BaseModel):
    statements: List[Statement] = Field(description='The list of statements')

def clean_statement_data(statements: List[Dict]) -> List[Dict]:
    """Clean statements to retain only 'raw' and 'start_idx'"""
    cleaned_statements = []
    for stmt in statements:
        cleaned_stmt = {}
        if 'raw' in stmt:
            cleaned_stmt['raw'] = ' '.join(stmt['raw'].split())
        if 'start_idx' in stmt:
            cleaned_stmt['start_idx'] = stmt['start_idx']
        for nested_key in ('ifThen', 'ifElse', 'performInlineStatement', 'nested_statements'):
            if nested_key in stmt and isinstance(stmt[nested_key], list):
                cleaned_stmt[nested_key] = clean_statement_data(stmt[nested_key])
        cleaned_statements.append(cleaned_stmt)
    return cleaned_statements

def flatten_statement_hierarchy(statements: List[Dict]) -> List[Dict]:
    """Flatten statements into simple list"""
    flat_list = []
    for stmt in statements:
        flat_stmt = {
            'start_idx': stmt.get('start_idx'),
            'raw': ' '.join(stmt.get('raw', '').split())
        }
        flat_list.append(flat_stmt)
        for nested_key in ('ifThen', 'ifElse', 'performInlineStatement', 'nested_statements'):
            if nested_key in stmt and isinstance(stmt[nested_key], list):
                nested_flat = flatten_statement_hierarchy(stmt[nested_key])
                flat_list.extend(nested_flat)
    return flat_list

def split_into_chunks(lst: List, chunk_size: int):
    """Split list into chunks"""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def generate_statement_explanation(statements_chunk: List[Dict], llm) -> Dict:
    """Generate explanations for a chunk of statements"""
    try:
        structured_llm = llm.with_structured_output(Statements)
        clean_chunk = clean_statement_data(statements_chunk)
        code = json.dumps(clean_chunk, indent=2)
        output = structured_llm.invoke(INSTRUCTION.format(CODE=code))
        return output.model_dump()
    except Exception as e:
        logger.error(f"Error generating explanation: {e}")
        return {"statements": []}

@logger.catch
def statement_summary(statements: List[Dict]) -> Dict[str, Any]:
    """Process COBOL statements and generate summaries"""
    try:
        llm = get_llm(model_type="assistant")
        flat_list = flatten_statement_hierarchy(statements)
        combined_source_json = {'statements': []}

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            futures = [
                executor.submit(generate_statement_explanation, chunk, llm)
                for chunk in split_into_chunks(flat_list, 10)
            ]
            for future in concurrent.futures.as_completed(futures):
                output = future.result()
                combined_source_json['statements'].extend(output.get('statements', []))

        final_statements = merge_statement_translations(combined_source_json, statements)
        return {"statement_level": final_statements}

    except Exception as e:
        logger.error(f"Statement summarization failed: {e}")
        return {"statement_level": []}

def merge_statement_translations(source_json: Dict, target_json: List) -> List[Dict]:
    """Merge translations from source into target"""
    statement_map = build_statement_map(source_json.get('statements', []))
    for stmt in target_json:
        add_statement_translation(stmt, statement_map)
    return target_json

def build_statement_map(source_statements: List[Dict]) -> Dict:
    """Flatten statements into a dictionary by start_idx"""
    statement_map = {}
    for stmt in source_statements:
        start_idx = stmt.get('start_idx')
        if start_idx is not None:
            statement_map[start_idx] = stmt
        for nested_key in ('ifThen', 'ifElse', 'performInlineStatement', 'nested_statements'):
            if nested_key in stmt and isinstance(stmt[nested_key], list):
                nested_map = build_statement_map(stmt[nested_key])
                statement_map.update(nested_map)
    return statement_map

def add_statement_translation(entry: Dict, statement_map: Dict):
    """Add translations to statement entries"""
    start_idx = entry.get('start_idx')
    if start_idx in statement_map:
        source_entry = statement_map[start_idx]
        if 'translation' in source_entry:
            entry['translation'] = source_entry['translation']
    for nested_key in ('ifThen', 'ifElse', 'performInlineStatement', 'nested_statements'):
        if nested_key in entry and isinstance(entry[nested_key], list):
            for nested_stmt in entry[nested_key]:
                add_statement_translation(nested_stmt, statement_map)