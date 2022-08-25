dec = 42
binary = bin(dec)
start_str = "picoCTF{"
mid_str = binary[2:]
end_str = "}"

print(start_str + mid_str + end_str)
