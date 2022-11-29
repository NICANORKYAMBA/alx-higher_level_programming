#!/usr/bin/python3
for letter in range(97, 122):
    if chr(letter) != 'e' and chr(letter) != 'q':
        print("{}".format(chr(letter)), end="")
