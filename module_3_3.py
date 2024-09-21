# Домашнее задание по уроку "Распаковка позиционных параметров".


def print_params(a=1, b='строка', c=True):
    print(a, b, c)

values_list = [5, 'текст', False]
values_dict = {'a': 12, 'b': 34, 'c': 56}

values_list_2 = [54.32, 'Строка']


print_params()
print_params(2)
print_params(3, '4')
print_params(5, '6', False)

print_params(b=25)          # некорректный тип параметра b
print_params(c=[1, 2, 3])   # некорректный тип параметра c

print_params(*values_list)
print_params(**values_dict)

print_params(*values_list_2, 24)