# Дополнительное практическое задание по модулю: "Подробнее о функциях."

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    s = 0
    if isinstance(data_structure, str):
        s += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        s += data_structure
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            s += calculate_structure_sum(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            s += calculate_structure_sum(key)
            s += calculate_structure_sum(value)
    return s


result = calculate_structure_sum(data_structure)
print(result)
