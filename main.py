import random

from typing import List


def generate_pin(length: int) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def replace_fives(a_list: list, value: str) -> List[str]:
    return [element.replace('5', value) for element in a_list]


def write_file(filename: str, data: str):
    with open(filename, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    pins = [generate_pin(8) for _ in range(5)]
    pins_without_fives = replace_fives(pins, '8')
    str_list = '\n'.join(pins_without_fives)
    write_file('test.txt', str_list)
