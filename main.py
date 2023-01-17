import subprocess
from datetime import datetime
from typing import Generator

def get_lines_and_values(lines: Generator) -> list:
    result_list = []
    for line in lines:
        result_list.append(line.replace("\n", ""))
    return result_list


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
        output_file__path=output_file__path)

    lines = get_file_content(output_file__path=output_file__path)
    matched_texts = get_lines_and_values(lines=lines)
    print(matched_texts)

    end_time = datetime.now()
    print(f'\nExecution duration: {end_time - start_time}')


if __name__ == '__main__':
    main()
