from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, keyword=None, max_extra_alphabets=None, max_extra_numbers=None, max_special_chars=None):
    characters = string.ascii_letters + string.digits + string.punctuation

    if keyword:
        keyword = keyword[:6]
        remaining_length = length - len(keyword)
    else:
        remaining_length = length

    if remaining_length <= 0:
        raise ValueError("Password length should be greater than the keyword length.")

    num_count = min(int(max_extra_numbers) if max_extra_numbers else 0, remaining_length - 2) 
    remaining_length -= num_count

    alpha_count = min(int(max_extra_alphabets) if max_extra_alphabets else 0, remaining_length - 1) 
    remaining_length -= alpha_count

    special_char_count = min(int(max_special_chars) if max_special_chars else 0, remaining_length)

    password = (
        (keyword or '') +
        random.choice(string.ascii_uppercase) +
        ''.join(random.choice(string.digits) for _ in range(num_count)) +
        ''.join(random.choice(string.ascii_letters) for _ in range(alpha_count)) +
        ''.join(random.choice(string.punctuation) for _ in range(special_char_count)) +
        ''.join(random.choice(characters) for _ in range(remaining_length))
    )

    additional_characters = list(password[len(keyword) if keyword else 0:])
    random.shuffle(additional_characters)
    password = (keyword or '') + ''.join(additional_characters)

    return password


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate():
    keyword = request.form.get('keyword')
    length = int(request.form['length'])
    max_extra_alphabets = request.form.get('max_extra_alphabets', 0)
    max_extra_numbers = request.form.get('max_extra_numbers', 0)
    max_special_chars = request.form.get('max_special_chars', 0)

    max_extra_alphabets = int(max_extra_alphabets) if max_extra_alphabets.isdigit() else 0
    max_extra_numbers = int(max_extra_numbers) if max_extra_numbers.isdigit() else 0
    max_special_chars = int(max_special_chars) if max_special_chars.isdigit() else 0

    try:
        password = generate_password(length, keyword, max_extra_alphabets, max_extra_numbers, max_special_chars)
        return render_template('index.html', password=password)
    except ValueError as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
