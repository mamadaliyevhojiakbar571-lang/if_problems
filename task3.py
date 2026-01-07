# if3. Butun son berilgan. Agar, berilgan son musbat bo'lsa, 1 ga oshiring, agar manfiy bo'lsa 2 ga
# kamaytiring. Agar 0 ga teng bo'lsa, 10 ni o'zlashtirsin. Hosil bo'lgan sonni ekranga chiqaruvchi
# programma tuzilsin.
n = int(input("n = "))
if n > 0:
    n += 1
elif n < 0:
    n -= 2
else:
    n = 10
print(n)