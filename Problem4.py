def menyu(a , b):
	open_f = open('/users/mac/Desktop/{menyu}.txt', 'w')
	open_f.write(a)
	open_f.write(b)
	open_f.close()
a = input('Что будете кушать?')
b = input('А что выпить?')
print('Ок, ваш меню записан!')
menyu (a, b)	