import re


def count_line(code: str, label: str):

    match label:
        case "COBOL" | "COPY" | "DB":
            count = fast_analyze_cobol(code)
        case "JCL":
            count = fast_analyze_jcl_ibm(code)
        case "BMS":
            count = fast_analyze_bms(code)
        case "WFL":
            count = fast_analyze_wfl(code)
        case "A_AUTO":
            count = fast_analyze_A_AUTO(code)
        case "ASM":
            count = fast_analyze_ASM(code)
        case "CICS":
            count = fast_analyze_CICS(code)
        case "CLIST":
            count = fast_analyze_CLIST(code)
        case "CSD":
            count = fast_analyze_csd(code)
        case "DDL":
            count = fast_analyze_DDL(code)
        case "EASY":
            count = fast_analyze_EASY(code)
        case "PANEL":
            count = fast_analyze_PANEL(code)
        case "PLI_COPY":
            count = fast_analyze_PLI_COPY(code)
        case "PROC":
            count = fast_analyze_PROC(code)
        case "REPORT":
            count = fast_analyze_REPORT(code)
        case _:
            count = len(code.splitlines()), 0

    return count


def fast_analyze_cobol(code: str):

    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = 0
    code_with_comment_lines = 0
    for line in lines:
        if len(line) > 7 and line[6] == "*":
            comment_lines += 1

        # check *> not in string
        split = line.split("'")

        for i in range(0, len(split), 2):
            if "*>" in split[i]:
                comment_lines += 1

                if re.search(r"[A-Za-z0-9]", line[: line.find("*>")]):
                    code_with_comment_lines += 1

    loc = total_lines - empty_lines - comment_lines + code_with_comment_lines

    # print(parse_file_output['statsMap'])

    return [loc, comment_lines]


def fast_analyze_jcl_ibm(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = len(re.findall(r"^/{1,2}\*", code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]


def fast_analyze_bms(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = len(re.findall(r"^\s*\*", code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]


def fast_analyze_jcl_fujitsu(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = len(re.findall(r"^\\\*", code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]


def fast_analyze_wfl(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = len(re.findall(r"^\s*%", code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]


def fast_analyze_pli(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = len(re.findall(r"/\*.*\*/", code))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]


def fast_analyze_csd(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    loc = total_lines - empty_lines

    return [loc, 0]


def fast_analyze_sql(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_blocks = re.findall(r"/\*[\s\S]*\*/", code)
    comment_line_count = 0

    for line in comment_blocks:
        comment_line_count += len(line.splitlines())

    comment_blocks_lines = [
        line for block in comment_blocks for line in block.splitlines()
    ]

    for line in lines:
        if re.search(r"^\s*--", line) and line not in comment_blocks_lines:
            comment_line_count += 1
    loc = total_lines - empty_lines - comment_line_count

    # for line in lines:
    #     if line in_comm
    #     split = line.split("'")

    #     # check -- not in string
    #     for i in range(0, len(split), 2):
    #         if "--" in split[i]:
    #             comment_lines += 1
    #             break

    # loc = total_lines - empty_lines - comment_lines

    # return loc, comment_line_count
    return [loc, comment_line_count]

def fast_analyze_A_AUTO(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))
    comment_regex = r"^\s*\*"
    comment_lines = len(re.findall(comment_regex, code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]

def fast_analyze_ASM(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))
    comment_regex = r"^\s*\*"
    comment_lines = len(re.findall(comment_regex, code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]

def fast_analyze_PLI_COPY(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))
    comment_regex = r"^\s*\/\*.*\*\/"
    comment_lines = len(re.findall(comment_regex, code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]

def fast_analyze_CICS(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))
    comment_regex = r"^\s*\*"
    comment_lines = len(re.findall(comment_regex, code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]

def fast_analyze_PANEL(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))
    comment_regex = r"^\s*\/\*.*\*\/"
    comment_lines = len(re.findall(comment_regex, code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]


def fast_analyze_EASY(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))
    comment_regex = r"^\s*\*"
    comment_lines = len(re.findall(comment_regex, code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]

def fast_analyze_DDL(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))
    comment_regex = r"^\s*--"
    comment_lines = len(re.findall(comment_regex, code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]

def fast_analyze_REPORT(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))
    comment_regex = r"^\s*-\'.*"
    comment_lines = len(re.findall(comment_regex, code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]

def fast_analyze_CLIST(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))
    comment_regex = r"^\s*//\*.*"
    comment_lines = len(re.findall(comment_regex, code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]

def fast_analyze_PROC(code: str):
    lines = code.splitlines()
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))
    comment_regex = r"^\s*//\*.*"
    comment_lines = len(re.findall(comment_regex, code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]