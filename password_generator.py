import random
import string

def generate_password(length, keyword, max_extra_alphabets, max_extra_numbers, max_special_chars):
    characters = string.ascii_letters + string.digits + string.punctuation
    keyword = keyword[:6] 
    remaining_length = length - len(keyword)
    
    if remaining_length <= 0:
        raise ValueError("Password length should be greater than the keyword length.")

    num_count = min(max_extra_numbers, remaining_length - 2) 
    remaining_length -= num_count

    alpha_count = min(max_extra_alphabets, remaining_length - 1) 
    remaining_length -= alpha_count

    special_char_count = min(max_special_chars, remaining_length)

    password = (
        keyword +
        random.choice(string.ascii_uppercase) +
        ''.join(random.choice(string.digits) for _ in range(num_count)) +
        ''.join(random.choice(string.ascii_letters) for _ in range(alpha_count)) +
        ''.join(random.choice(string.punctuation) for _ in range(special_char_count)) +
        ''.join(random.choice(characters) for _ in range(remaining_length))
    )

    additional_characters = list(password[len(keyword):])
    random.shuffle(additional_characters)
    password = keyword + ''.join(additional_characters)

    return password

if __name__ == "__main__":
    keyword = input("Enter a keyword (6 characters max): ")
    length = int(input("Enter the total length of your password: "))
    max_extra_alphabets = int(input("Enter the max number of extra alphabets: "))
    max_extra_numbers = int(input("Enter the max number of extra numbers: "))
    max_special_chars = int(input("Enter the max number of special characters: "))

    try:
        password = generate_password(length, keyword, max_extra_alphabets, max_extra_numbers, max_special_chars)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)
