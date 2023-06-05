import random
import string

def generate_otp(length=8):
    # Choose random characters from the set of letters and digits
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

# Example usage
print(generate_otp())

