import re

def clean_code(input_text):
    lines = input_text.splitlines()
    cleaned_lines = []
    pattern = re.compile(r"^\d+\s*")
    for line in lines:
        new_line = pattern.sub(lambda m: " " * len(m.group(0)), line)
        cleaned_lines.append(new_line)

    # Join the cleaned lines back into a single string
    cleaned_output = "\n".join(cleaned_lines)
    return cleaned_output


def comment_specific_lines(code: str, truncate_col: int=72) -> str:
    # Split the code into lines
    lines = code.splitlines()
    for i, line in enumerate(lines):
        # Remove comments from the line
        if "*>" in line:
            line = line.split("*>")[0].rstrip()

        # Check for @OPTIONS and modify the line accordingly
        if line.strip().startswith("@OPTIONS"):
            line = line[:6] + "*" + line[6:].lstrip()

        # Truncate the line to 72 characters
        if truncate_col != 0:
            lines[i] = line[:72]
            if line.strip().startswith("*"):
                lines[i] = ""

    # Join the lines back into a single string
    return "\n".join(lines)