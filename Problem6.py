def fun1():
    print ("Я главная функция")
    def fun2():
        print ("Я вложенная функция")
    fun2()
    
fun1()