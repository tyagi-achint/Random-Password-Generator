import random
import string

def generate_password(length, keyword, max_extra_alphabets, max_extra_numbers, max_special_chars):
    characters = string.ascii_letters + string.digits + string.punctuation
    keyword = keyword[:6]  # Ensure the keyword is at most 6 characters
    remaining_length = length - len(keyword)
    
    if remaining_length < 3:
        raise ValueError("Password length should be at least 3 characters more than the keyword length.")

    # If total length is greater than 8, include more than 2 numbers
    num_count = min(max_extra_numbers, remaining_length - 2)  # Ensure at least 1 number is left for other characters
    remaining_length -= num_count

    # Determine the count of extra alphabets and special characters
    alpha_count = min(max_extra_alphabets, remaining_length - 1)  # Ensure at least 1 character is left for other characters
    remaining_length -= alpha_count

    special_char_count = min(max_special_chars, remaining_length - 1)  # Ensure at least 1 character is left for other characters
    remaining_length -= special_char_count

    password = (
        keyword +
        random.choice(string.ascii_uppercase) +
        ''.join(random.choice(string.digits) for _ in range(num_count)) +
        ''.join(random.choice(string.ascii_letters) for _ in range(alpha_count)) +
        ''.join(random.choice(string.punctuation) for _ in range(special_char_count)) +
        ''.join(random.choice(characters) for _ in range(remaining_length))
    )

    # Shuffle the additional characters, leaving the keyword intact
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
