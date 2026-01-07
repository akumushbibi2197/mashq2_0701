#1-misol
n = int(input("Son kiriting: "))

if n > 0:
    print("Musbat son")
elif n < 0:
    print("Manfiy son")
else:
    print("Nol")

#2-misol
a = float(input("a = "))
b = float(input("b = "))
belgi = input("Amalni kiriting (+, -, *, /): ")

if belgi == "+":
    print(a + b)
elif belgi == "-":
    print(a - b)
elif belgi == "*":
    print(a * b)
elif belgi == "/":
    if b != 0:
        print(a / b)
    else:
        print("0 ga bo‘lish mumkin emas")
else:
    print("Noto‘g‘ri amal")

#3-misol
b1 = int(input("1-baho: "))
b2 = int(input("2-baho: "))
b3 = int(input("3-baho: "))

orta = (b1 + b2 + b3) / 3
print("O‘rtacha baho:", orta)

#4-misol
n = int(input("Son kiriting: "))

if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:
    print("2, 3 va 5 ga bo‘linadi")
else:
    print("2, 3 va 5 ga bir vaqtda bo‘linmaydi")

#5-misol
harf = input("Harf kiriting: ").lower()

if harf in "aeiou":
    print("Unli harf")
elif harf.isalpha():
    print("Undosh harf")
else:
    print("Harf emas")
