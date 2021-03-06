# Имеется N кг металлического сплава. Из негоK кг к изготавливают заготовки массой аждая. После этого из каждой
# заготовки вытачиваются детали массой M кг каждая (из каждой заготовки вытачивают максимально возможное количество
# деталей). Если от заготовок после этого что-то остается, то этот материал возвращают к началу производственного цикла
# и сплавляют с тем, что осталось при изготовлении заготовок. Если того сплава, который получился, достаточно для
# зготовления хотя бы одной заготовки, то из него снова изготавливают заготовки, из них – детали и т.д. Напишите
# программу, которая вычислит, какое количество деталей может быть получено по этой технологии из имеющихся исходно
# N кг сплава.

# Формат ввода
# Вводятся N, K, M. Все числа натуральные и не превосходят 200.

# Формат вывода
# Выведите одно число — количество деталей, которое может
# получиться по такой технологии
import time

start_time = time.time()

temp_1 = [10, 5, 2]  # 4
temp_2 = [13, 5, 3]  # 3
temp_3 = [14, 5, 3]  # 4
temp_4 = [8, 4, 3]


def factory_parts(x):
    overall_w = x[0]
    blank_w = x[1]
    part_w = x[2]
    left_w = 0

    while (overall_w >= blank_w) and (blank_w >= part_w):
        t = overall_w // blank_w * (blank_w // part_w)
        overall_w = overall_w - t * part_w
        left_w += t

    return left_w


print(factory_parts(temp_1))
print(factory_parts(temp_2))
print(factory_parts(temp_3))

print("Время выполнения: ", time.time() - start_time)

