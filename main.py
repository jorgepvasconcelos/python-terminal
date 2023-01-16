import subprocess
from datetime import datetime


def parse_terminal_output(output: str) -> list[str]:
    output = output.split('\n')
    output = [v for v in output if not v == '']
    return output


def get_lines_and_values(lines: list[str]) -> dict[int:str]:
    result = {}

    for line in lines:
        colon_index = line.index(":")

        line_number = int(line[:colon_index])
        line_value = line[colon_index + 1:]

        result[line_number] = line_value

    return result


def run_command(search_text: str, file_path: str) -> str:
    command = "ag"
    args = ["--numbers", '--nocolor', "--nobreak", "--nogroup", search_text, file_path]
    shell_command = [command, *args]

    output = subprocess.run(
        shell_command,
        stdout=subprocess.PIPE,
        text=True
    )
    return output.stdout


def main():
    start_time = datetime.now()

    command_output = run_command(search_text='ola', file_path='test.txt')
    response = parse_terminal_output(output=command_output)
    matched_texts = get_lines_and_values(lines=response)

    end_time = datetime.now()

    print(matched_texts)
    print(f'Execution duration: {end_time - start_time}')


if __name__ == '__main__':
    main()
