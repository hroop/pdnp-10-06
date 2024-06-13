# funkcja wewnętrzna, zagnieżdżona
# dekoratory - uzywaja mechanizmu funkcji wewnętrznej

def fun1():
    print('To jest fun1')

    def fun2():
        print("To jest fun2")

    return fun2  # bez nawiasów, zwracamy tylko adres funkcji


# nazwa funkcji i nawiasy ()
print(fun1)  # <function fun1 at 0x0000021EEBD78B80>
fun1()  # To jest fun1
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x000002E7442D9E40>
xFun()  # To jest fun2
