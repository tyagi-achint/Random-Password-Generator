# Random Password Generator

This is a simple Flask web application that generates random passwords based on user input.

## Getting Started

### Prerequisites

- Docker: Make sure you have Docker installed on your machine.

### Running the Application

1. Clone the repository:

    ```bash
    git clone https://github.com/tyagi-achint/Random-Password-Generator.git
    cd Random-Password-Generator
    ```

2. Build the Docker image:

    ```bash
    docker build -t password-generator .
    ```

3. Run the Docker container:

    ```bash
    docker run -it -p 5000:5000 password-generator
    ```

4. Access the application in your web browser at [http://localhost:5000](http://localhost:5000).

## Usage

- Enter a keyword (optional, 6 characters max).
- Specify the total length of the password.
- Optionally, set the maximum number of extra alphabets, numbers, and special characters.
- Click the "Generate Password" button.

The generated password will be displayed on the page.

