def get_user_info():
    # Asking Name
    name = input("What is your name: ")
    # Asking Age
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print("Please enter a valid age.")
    # Asking City
    city = input("Where do you live: ")
    # Asking Interests
    interests = input("What are things that you love: ")
    # Output
    output = f"Hai {name}, you are {age} years old and you live in {city}, and the things you like are {interests}."
    print(output)

get_user_info()
