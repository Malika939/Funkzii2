import random
randlist = "1234567890qwertyuiopasdfghjklzxcvbnm-*/+.,?[]}{_\=''"
def my_fun(n):
    my_list = []
    for i in range (1, n):
        x = random.choice(randlist)
        my_list.append (x)
    print (my_list)
n = int (input())
my_fun(n)