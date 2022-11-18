#testcase1
import math
Panjang = int(input('Masukkan panjang : '))
Lebar = int(input('Masukkan lebar : '))
Jari = int(input('Masukkan jari-jari : '))
setlir = int((3.14*Jari**2)/2)
pinjing = int(Panjang*Lebar)
kaleng=(setlir+pinjing)/15
print(f"Area tersebut membutuhkan {math.ceil(kaleng)} kaleng cat")



