import hashlib

def md5_creator(input_string):
    # Create an MD5 hash object
    md5_obj = hashlib.md5()
    
    # Update the hash object with the bytes of the input string
    md5_obj.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal representation of the digest
    return md5_obj.hexdigest()

# User input
user_input = input("Enter a string to generate its MD5 hash: ")

# Generate MD5 hash
hash_result = md5_creator(user_input)
print(f"The MD5 hash of the string is: {hash_result}")
