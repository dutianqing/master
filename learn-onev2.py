#!/usr/local/env python
#coding=utf-8
#judge prime number
#auth lonewolfs
#version v2.0
while True:
    num = raw_input("type an number:")
    try:
        num = float(num)
        #print("Right type")
    except ValueError:
        print("Error type")
        continue

    num = int(num)
    i = 2
    is_prime = False
    while i < num:
        for ii in range(2, i):
            if i % ii == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            print i, 'is prime'
        i += 1
    else:
        break
