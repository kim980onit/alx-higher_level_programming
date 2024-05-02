#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -2):
    print("{}{}".format(char(i), chr(i - 33)), end='')
