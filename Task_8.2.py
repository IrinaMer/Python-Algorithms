
import hashlib

x = input('Введите строку: ')

list_1 = set()

for i in range(len(x)):
	for j in range(i,len(x)):
		list_1.add(hashlib.sha1(x[i:j+1].encode('utf-8')).hexdigest())

print('Количество неповторяющихся подстрок - ', len(list(list_1)))