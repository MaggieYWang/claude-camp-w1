while True:
    name = input("Please enter your name: ").strip().capitalize()
    title = input("What is your preferred title ? Mr., Mrs., Miss, Ms., or Dr.: ").capitalize()
    age = int(input("Please enter your age: "))
    if age < 18:
        greeting = f"Hello {name}! You are so young, keep it up!"
    elif age < 60:
        greeting = f"Hello {title} {name}! Wishing you great success in your career!"
    else:
        greeting = f"Hello {title} {name}! Wishing you a healthy and happy retirement!"
    print(greeting)