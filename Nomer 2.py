# Amalia Ramadhani Amanda Syafi'i
# 20051397080
# D4 MI 2020B

desimal = int(input('Masukkan Bilangan Desimal = '))

biner = bin(desimal) .replace("0b","")
oktal = oct(desimal) .replace("0o","")
hexa = hex(desimal) .replace("0x","")
print(biner,oktal,hexa)
