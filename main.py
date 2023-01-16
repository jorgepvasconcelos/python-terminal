import subprocess
from datetime import datetime
from typing import Generator

import sys


def parse_terminal_output(output: str) -> list[str]:
    if isinstance(output, list):
        output = [v.replace('\n', '') for v in output]
        return output

    output = output.split('\n')
    output = [v for v in output if not v == '']
    return output


def get_lines_and_values(lines: Generator) -> dict[int:str]:
    result = {}

    for line in lines:
        colon_index = line.index(":")

        line_number = int(line[:colon_index])
        line_value = line[colon_index + 1:]

        result[line_number] = line_value

    return result


def get_file_content(output_file__path: str):
    with open(output_file__path, 'r') as file:
        for line in file:
            yield line


def run_command(search_text: str, file_path: str, output_file__path: str = None) -> None:
    command = "ag"
    args = ["--numbers", '--nocolor', "--nobreak", "--nogroup", search_text, file_path]
    shell_command = [command, *args]

    with open(output_file__path, 'w') as file:
        subprocess.run(
            shell_command,
            stdout=file,
            text=True
        )


def main():
    start_time = datetime.now()
    output_file__path = 'output.txt'

    run_command(
        search_text="Suco de cevadiss, é um leite divinis, qui tem lupuliz, matis, aguis e fermentis",
        file_path='large_file.txt',
        output_file__path=output_file__path
    )

    lines = get_file_content(output_file__path=output_file__path)

    # response = parse_terminal_output(output=lines)
    matched_texts = get_lines_and_values(lines=lines)
    # print(matched_texts)

    end_time = datetime.now()
    print(f'\nExecution duration: {end_time - start_time}')


if __name__ == '__main__':
    main()
