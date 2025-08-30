INSTRUCTION = """Parse the provided COBOL paragraph code into JSON format that represents its structure and elements.

The parsing should capture key components from the COBOL paragraph, including but not limited to keywords, variable names, data types, values, and sections. Convert these components into standardized JSON fields using the expected schema below so that the output is comprehensible and structured for further use. The code needs to handle references in the format `[]` and `<>`, and preserve them in the paragraph summary and details fields.
{CODE}
"""