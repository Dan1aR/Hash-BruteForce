# -*- coding: UTF-8 -*-
import hashlib


abc_1 = '1234567890'
abc_2 = '1234567890qwertyuiopasdfghjklzxcvbnm'
abc_3 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
abc_4 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!"@#№;$%:^?&*()-_=+}{[]/<>.,'
abc = abc_4; tip = 'md5'; hash0 = ''; N = 10; N_min = 1


print("""Ддя брутфорса хэшей введите параметры к выполнению скрипта:
	-min :: Минимальная длина пароля (Стандартная - 1)
	-max :: Максимальная длинна пароля (Стандартная - 10)
	-l :: Сложность пароля (Стандартная 4)
		   - '1' :: только цифры
		   - '2' :: цифры и маленикье латинские буквы
		   - '3' :: цифры, маленькие и большие латинские буквы
		   - '4' :: цифры, маленькие и большие латинские буквы, специальные символы
	-t :: Тип хэша ('md5', 'sha1') (Стандартный md5)
	-h :: Хэш
	Пример ввода:
	-min 1 -max 4 -l 1 -t md5 -h 81dc9bdb52d04dc20036dbd8313ed055
	""")

param = input('>>> ')
param = param.split()
for i in range(len(param)):
	if param[i] == '-max':
		N = int(param[i + 1])
	elif param[i] == '-l':
		if param[i + 1] == '1':
			abc = abc_1
		elif param[i + 1] == '2':
			abc = abc_2
		elif param[i + 1] == '3':
			abc = abc_3
		elif param[i + 1] == '4':
			abc = abc_4
	elif param[i] == '-t':
		tip = param[i + 1]
	elif param[i] == '-h':
		hash0 = param[i + 1]
	elif param[i] == '-min':
		N_min = int(param [i + 1])

print("Процесс пошел, ждите результата")

def counting(N_current, abc, tip, hash0, s):
	for i in abc:
		s[N_current] = i
		
		if tip == 'md5' and hashlib.md5(''.join(s).encode()).hexdigest() == hash0:
			print(''.join(s), '::', hashlib.md5(''.join(s).encode()).hexdigest())
			input()
			exit()
		if tip == 'sha1' and hashlib.sha1(''.join(s).encode()).hexdigest() == hash0:
			print(''.join(s), '::', hashlib.sha1(''.join(s).encode()).hexdigest())
			input()
			exit()

		if N_current - 1 >= 0:
			counting(N_current - 1, abc, tip, hash0, s)		

for i in range(N_min, N + 1):
	s = ['' for _ in range(i)]
	counting(i - 1, abc, tip, hash0, s)