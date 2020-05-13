import random
import timeit


def play_of_bubble(num_list):
    step = 1
    while step < len(num_list):
        for i in range(len(num_list)-step):
            if num_list[i] < num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
        step += 1
    return num_list


num_list = [random.randint(-100, 100) for _ in range(10)]
print(num_list)
print(play_of_bubble(num_list))


# 10
print(timeit.timeit("play_of_bubble(num_list)", \
    setup="from __main__ import play_of_bubble, num_list", number=1000))


num_list = [random.randint(-100, 100) for _ in range(100)]

# 100
print(timeit.timeit("play_of_bubble(num_list)", \
    setup="from __main__ import play_of_bubble, num_list", number=1000))

num_list = [random.randint(-100, 100) for _ in range(1000)]

# 1000
print(timeit.timeit("play_of_bubble(num_list)", \
    setup="from __main__ import play_of_bubble, num_list", number=1000))


def b2_sort(num_list2):
    for i in range(len(num_list2) - 1, 0, -1):
        step_2 = True
        for k in range(i):
            if num_list2[k] < num_list2[k+1]:
                num_list2[k], num_list2[k+1] = num_list2[k+1], num_list2[k]
                step_2 = False

        if step_2 == True:
            break
    return num_list2


numbers = [random.randint(-100, 100) for _ in range(10)]
print(numbers)
print(b2_sort(numbers))

# 10
print(timeit.timeit("b2_sort(numbers)", \
    setup="from __main__ import b2_sort, numbers", number=1000))

numbers = [random.randint(-100, 100) for _ in range(100)]

# 100
print(timeit.timeit("b2_sort(numbers)", \
    setup="from __main__ import b2_sort, numbers", number=1000))

numbers = [random.randint(-100, 100) for _ in range(1000)]

# 1000
print(timeit.timeit("b2_sort(numbers)", \
    setup="from __main__ import b2_sort, numbers", number=1000))



"""
 
Функция play_of_bubble работате медленнее, функция b2_sort. Особонно когда сортирует 1000 элементов. 
Обе функции имеют квадратичную сложность, но в play_of_bubble используются циклы while и for, которым 
необходимо много времени на обработку массива.
В b2_sort используется два цикла for,  логические опрераторы True и False и сама по себе функция является рекурсией, 
все это значительно снижают время обработки массива. Из представленных примеров функция b2_sort является 
более эффективной для обработки больших массивов данных.


play_of_bubble
[-97, -65, -95, 79, -18, 28, 19, -90, -96, 16]
[79, 28, 19, 16, -18, -65, -90, -95, -96, -97]
0.028311584999999986
0.8169926439999999
85.354401671

b2_sort
[98, -48, 40, -87, -86, -67, 79, 74, 74, -83]
[98, 79, 74, 74, 40, -48, -67, -83, -86, -87]
0.0024966129999910436
0.016670235000006528
0.3300818400000054

"""
