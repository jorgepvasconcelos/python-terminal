from datetime import datetime
from typing import Generator


def get_file_content(output_file__path: str):
    with open(output_file__path, 'r') as file:
        for line, value in enumerate(file):
            yield line, value


def match_text(lines: Generator, text_to_match) -> list:
    result_list = []
    for line, value in lines:
        if text_to_match in value:
            result_list.append(value.replace("\n", ""))
    return result_list


def main():
    start_time = datetime.now()
    output_file__path = "large_file.txt"
    text_to_match = "Suco de cevadiss, é um leite divinis, qui tem lupuliz, matis, aguis e fermentis"

    line = get_file_content(output_file__path)
    matched_texts = match_text(lines=line, text_to_match=text_to_match)

    end_time = datetime.now()
    print(f'\nExecution duration: {end_time - start_time}')
    print("Matchs: ", len(matched_texts))


if __name__ == '__main__':
    main()
