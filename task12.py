# if12. Uchta son berilgan. Shu sonlarni kichigini aniglovchi programma tuzilsin.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)