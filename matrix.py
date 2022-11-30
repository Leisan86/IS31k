from random import randint


def create_matrix(h: int, w: int) -> str:
    counter: int = 1
    number_of_elements: int = h * w
    result: str = ''

    for i in range(number_of_elements):
        matrix_element: str = str(randint(10, 99))
        if counter == w:
            result += f"{matrix_element}\n"
            counter = 1
        else:
            result += f"{matrix_element} "
            counter += 1

    return result


def maximum_element(element: str) -> int:
    result = max(list(map(int, element.split())))

    return result
