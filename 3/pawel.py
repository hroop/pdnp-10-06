n = 24

if n % 2 != 0:
    print("Weird")

elif n % 2 == 0 and n > 20:
    print("Not weird")

elif n == 2 or n == 4:
    print("Not Weird")

elif n == 6 or n == 8 or n == 10 or n == 12 or n == 14 or n == 16 or n == 18 or n == 20:
    print("Weird")
