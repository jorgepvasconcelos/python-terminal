import subprocess
from datetime import datetime


def parse_terminal_output(output: str) -> list[str]:
    if isinstance(output, list):
        output = [v.replace('\n', '') for v in output]
        return output

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


def run_command(search_text: str, file_path: str, file_output_path: str = None) -> str:
    command = "ag"
    # args = ["--numbers", '--nocolor', "--nobreak", "--nogroup", search_text, file_path]
    args = ["--numbers", '--nocolor', "--nobreak", "--nogroup", search_text, file_path, ">", "f.txt"]
    shell_command = [command, *args]

    if file_output_path:
        with open(file_output_path, 'w') as file:
            subprocess.run(
                shell_command,
                stdout=file,
                text=True
            )

        with open(file_output_path, 'r') as file:
            output = file.readlines()

    else:
        output = subprocess.run(
            shell_command,
            stdout=subprocess.DEVNULL,
            text=True
        )
        output = output.stdout

    return output


def main():
    start_time = datetime.now()

    command_output = run_command(
        search_text="Suco de cevadiss, é um leite divinis, qui tem lupuliz, matis, aguis e fermentis",
        file_path='large_file.txt',
        # file_output_path='output.txt'
    )

    response = parse_terminal_output(output=command_output)
    matched_texts = get_lines_and_values(lines=response)
    print(matched_texts)

    end_time = datetime.now()
    print(f'\nExecution duration: {end_time - start_time}')


if __name__ == '__main__':
    main()
