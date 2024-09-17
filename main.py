# Roller Coaster 1
print("Welcome to the roller coaster")
height = int(input("Input your height (cm):\t"))
if height >= 120:
    print("You're good to go")
else:
    print("Sorry, but you're too short")

""" Operator
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
== equal to
!= not equal to """

# Roller Coaster 2
print("Welcome to the roller coaster")
height = int(input("Input your height (cm):\t"))
age = int(input("Input your age:\t"))
if height >= 120:
    print("You're good to go")
    if age <= 18:
        print("Please pay $7 ticket")
    else:
        print("Please pay $12 ticket")
else:
    print("Sorry, but you're too short")

# Roller Coaster 3
print("Welcome to the roller coaster")
height = int(input("Input your height (cm):\t"))
age = int(input("Input your age:\t"))
if height >= 120:
    print("You're good to go")
    if age <= 12:
        print("Please pay $5 ticket")
    elif age <= 18:
        print("Please pay $7 ticket")
    else:
        print("Please pay $12 ticket")
else:
    print("Sorry, but you're too short")

''' Coding exercise 5 (BMI) '''
weight = 85
height = 1.85

bmi = weight / (height ** 2)

''' Roller Coaster 4 '''
print("Welcome to the roller coaster")
height = int(input("Input your height (cm):\t"))
age = int(input("Input your age:\t"))
bill = 0
if height >= 120:
    print("You're good to go")
    if age <= 12:
        bill += 5
    elif age <= 18:
        bill += 7
    else:
        bill += 12
    photos = input("Do you want to take the photos? [Y/N]:\t").lower()
    if photos == 'y':
        bill += 3
    print(f"Your total bill is: {bill}")
else:
    print("Sorry, but you're too short")

"""
    !!! HOMEWORK !!!
    Kamu adalah seorang IT support yang diminta untuk membuat sistem kasir di toko pizza.
    Ini adalah daftar harganya:
        - Pizza Kecil (S): $15
        - Pizza Sedang (M): $20
        - Pizza Besar (L): $25
        - Add on Peperoni utk ukuran kecil (S): +$2
        - Add on Peperoni utk ukuran sedang (M) dan besar (L): +$3 (sisanya +$3)
        - Add on Keju untuk semua ukuran: +$1
    Task:
        1. Buatlah flowchart untuk cara kerja perhitungan total harga.
        2. Buatlah program untuk menghitung total harga. Gunakan semua materi yang sudah diajarkan.
"""

print('welcome to "loe mau beli pizza kaga?"')
print('loe mau ukuran ape')
print('1.small 15$ ')
print('2.medium 20$ ')
print('3.large 25$ ')

bill = 0

# Nanyain ini mau pizza ukuran apa
size = input("Masukkan ukuran (s/m/l):\t").lower()
if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
else:
    bill += 25

# Add on peperoni
'''Kalau dia small dia ditambah $2, sisanya (medium & large) $3'''
pep = input("Pake peperoni? (y/n):\t").lower()
if pep == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

# Add on keju
cheese = input("Pake keju? (y/n):\t").lower()
if cheese == 'y':
    bill += 1

# Print total harga
print(f"Total: {bill}")
