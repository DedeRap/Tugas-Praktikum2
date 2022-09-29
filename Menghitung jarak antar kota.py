# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 08:20:52 2022

@author: ASUS
"""

import math

t1 = float(input("Masukkan lattitude kota pertama = "))
g1 = float(input("Masukkan longitude kota pertama = "))

t2 = float(input("Masukkan lattitude kota kedua = "))
g2 = float(input("Masukkan longitude kota kedua = "))

dlat = t2 - t1
dlon = g2 - g1

a = math.sin(math.radians(dlat/2)) ** 2 + math.cos(math.radians(t1)) * math.cos(math.radians(t2)) * math.sin(math.radians(dlon/2)) ** 2

c = 2 * math.asin(math.sqrt(a))

r = 6371.01

print("Jarak antara dua titik adalah", c*r, "Kilometer")