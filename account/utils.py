import random
import string

def generate_random_alphanumeric_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
