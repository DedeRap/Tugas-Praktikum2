# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:17:27 2022

@author: ASUS
"""
import math

print("Kalkulator Semua Operator")

a = int(input("Masukkan variabel pertama(a) = "))
b = int(input("Masukkan variabel kedua(b) = "))

print("\nPenjumlahan")
h = a + b
print("Rumusnya : a + b")
print("Hasilnya = ", h)

print("\nPengurangan")
h = b - a
print("Rumusnya : b - a")
print("Hasilnya = ", abs(h))

print("\nPerkalian")
h = a * b
print("Rumusnya : a * b")
print("Hasilnya =", h)

print("\nSisa Pembagian")
h = a % b
print("Rumusnya : a % b")
print("Hasilnya =", h)

print("\nPembagian")
h = a / b
print("Rumusnya : a / b")
print("Hasilnya =", h)



print("\nHasil log(a)")
print("Hasil log: ", math.log10(a))

print("\nPerpangkatan")
h = a ** b
print("Rumusnya : a ** b")
print("Hasilnya =", h)
