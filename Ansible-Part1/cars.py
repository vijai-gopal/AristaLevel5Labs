#! /usr/bin/python3

import itertools 

brand = ["VW", "BMW", "MERCEDES", "AUDI"]
model = [" TIGUAN", " X5", " GLC", " ETRON"]

#for b in brand:
 #   for m in model:
  #      car = b + m
   #     print("The car model is ",car)

for (b, m) in zip(brand, model):
    print("The car model is ",brand, model)