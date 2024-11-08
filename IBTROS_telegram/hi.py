# from flask import Flask

# app = Flask(__name)

# @app.route('/')
# def say_hi():
#     return "Hi"

# if __name__ == '__main__':
#     app.run(debug=True)

import time

numbers = list(range(1, 11))

while numbers:
    print("Numbers available:", numbers)
    try:
        user_input = int(input("Enter a number between 1 and 10: "))
        if user_input in numbers:
            print("You pressed:", user_input)
            numbers.remove(user_input)
            time.sleep(2)  # Introducing a 2-second delay
            numbers.append(user_input)  # Add the number back after 2 seconds
        else:
            print("Number not available. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
