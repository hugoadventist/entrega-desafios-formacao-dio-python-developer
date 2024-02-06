# test_file.py
import hashlib


def string_to_random_integer(input_string):
    # Use SHA-256 hash function to get a secure hash
    hash_object = hashlib.sha256(input_string.encode())
    hash_hex = hash_object.hexdigest()

    # Take the first 8 characters of the hexadecimal hash and convert to integer
    random_integer = int(hash_hex[:5], 16)

    return random_integer


# Example usage:
input_str = "01352430258"
result = string_to_random_integer(input_str)
print(result)


# 217651
