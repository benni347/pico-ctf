#!/usr/bin/env python3
hex_num = "0x3D"


def hex_to_dec(n: str):
    if n[0:2] == "0x":
        n = n[2:]
    return int(n, 16)


dec_num = hex_to_dec(hex_num)

print(dec_num)
