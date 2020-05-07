
import collections
import random


def sum_tuple(num):

    total_sum = 0
    for sum_x in num:
        total_sum += sum_x
        return total_sum


All_dates = collections.namedtuple('All_dates', ['x_1', 'x_2', 'x_3', 'x_4'])

New_dict = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    total_x1 = int(input('Прибыль за 1-й квартал: '))
    total_x2 = int(input('Прибыль за 2-й квартал: '))
    total_x3 = int(input('Прибыль за 3-й квартал: '))
    total_x4 = int(input('Прибыль за 4-й квартал: '))
    New_dict[name] = All_dates(
        x_1=total_x1,
        x_2=total_x2,
        x_3=total_x3,
        x_4=total_x4
    )

total_result = ()

for name, profit in New_dict.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_result += profit

avg_profit_total = sum(total_result) / len(New_dict)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in New_dict.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

for name, profit in New_dict.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')
