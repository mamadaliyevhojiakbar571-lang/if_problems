# if11. A va B butun sonlari berilgan. Agar o'zgaruvchilar o'zaro teng bo'lmasa, A va B bu sonlarning
# kattasini o'zlashtirsin. Agar teng bo'lsa, 0 ni o'zlashtirsin. A va B ning qiymati ekranga chiqarilsin.
a = int(input("a = "))
b = int(input("b = "))
if a != b:
    if a > b:
        a = a
        b = a
    else:
        a = b
        b = b
else:
    a = 0
    b = 0
print("A =", a, "B =", b)