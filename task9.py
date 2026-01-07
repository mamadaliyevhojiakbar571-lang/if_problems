# if9. A va B hagiqiy sonlari beringan. Shu sonlarni shunday o'zgartirish kerakki, A son kichik B son katta
# bo'lsin. A va B ning giymati ekranga chigarilsin.
a = float(input("a = "))
b = float(input("b = "))
if a > b:
    a, b = b, a
print("A =", a, "B =", b)