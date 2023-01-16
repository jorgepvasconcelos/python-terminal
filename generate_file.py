import string
import random


def reference_text():
    list_of_text = set()
    with open('text_base.txt', 'r') as file:
        for line in file:
            if line == '\n':
                continue
            list_of_text.add(line)

    return list(list_of_text)


def generate_large_file(list_of_text):
    with open('large_file.txt', 'w') as file:
        for _ in range(10_000_000):
            text = random.choice(list_of_text)
            file.write(text)


if __name__ == '__main__':
    list_of_text = reference_text()
    print(len(list_of_text))
    generate_large_file(list_of_text)
