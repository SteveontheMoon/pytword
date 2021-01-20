#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


print('\tPYTWORD\n')
numbers = input('Choose the numbers of password to print: (up to 4)')
numbers = int(numbers)
length = input('Choose the password lenght: (1 to 32) ')
length = int(length)

for p in range(numbers):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print( password)


ok ci siamo riusciti
