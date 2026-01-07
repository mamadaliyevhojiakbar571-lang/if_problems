# if5. Uchta butun son berilgan. Shu sonlar orasidan nechta musbat va manfiy son borligini aniglovchi
# programma tuzilsin.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
musbat = 0
manfiy = 0
if a > 0:
    musbat += 1
elif a < 0:
    manfiy += 1
if b > 0:
    musbat += 1
elif b < 0:
    manfiy += 1
if c > 0:
    musbat += 1
elif c < 0:
    manfiy += 1
print("Musbat sonlar soni:", musbat, "Manfiy sonlar soni:", manfiy)