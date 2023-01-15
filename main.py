from typing import Optional

import os
import subprocess


def parse_terminal_output(output: bytes | str, decode: str = 'utf-8'):
    if isinstance(output, bytes):
        output = output.decode(decode)

    output = output.split('\n')
    output = [v for v in output if not v == '']

    return output


def get_lines_and_values(lines:list[str]) -> dict:
    result = {}

    for line in lines:
        colon_index = line.index(":")

        line_number = int(line[:colon_index])
        line_value = line[colon_index +1:]

        result[line_number] = line_value

    return result

def run_command(search_text:str, file_path:str) -> str:
    command = "ag"
    args = ["--numbers", search_text, file_path]
    shell_command = [command, *args]

    output = subprocess.run(
        shell_command,
        stdout=subprocess.PIPE,
        text=True
    )

    return output.stdout

def main():
    command_output = run_command(search_text='ola',file_path='test.txt')

    response = parse_terminal_output(output=command_output)

    matched_texts = get_lines_and_values(lines=response)
    print(matched_texts)


if __name__ == '__main__':
    main()