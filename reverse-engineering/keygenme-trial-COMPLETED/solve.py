import hashlib

def generate_key(username):
    hash_obj = hashlib.sha256(username.encode())
    hash_str = hash_obj.hexdigest()
    
    key_dynamic = ""
    key_dynamic += hash_str[4]
    key_dynamic += hash_str[5]
    key_dynamic += hash_str[3]
    key_dynamic += hash_str[6]
    key_dynamic += hash_str[2]
    key_dynamic += hash_str[7]
    key_dynamic += hash_str[1]
    key_dynamic += hash_str[8]

    key_full = key_part_static1_trial + key_dynamic + key_part_static2_trial
    
    return key_full

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"

username = "PRITCHARD"
print(generate_key(username))

