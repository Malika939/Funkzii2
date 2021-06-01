def isprime(n):
    for i in range (2, n):
        sum = 0
        for j in range (2, i // 2):
            if (i % j == 0):
                sum += 1
        if (sum == 0):
            print (i)
a = int (input())
isprime (a)