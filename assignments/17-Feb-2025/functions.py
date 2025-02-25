def greet_user(name):
    # TODO: Convert this to return a string instead of printing
    return f"Hello, {name}!"

def calculate_sum(a, b):
    # TODO: Convert this to return the sum instead of printing
    return a + b

def find_average(numbers):
    # TODO: Convert this to return the average instead of printing
    return sum(numbers) / len(numbers)

def uppercase_string(s):
    # TODO: Convert this to return the uppercase version instead of printing
    return f"{s.upper()}"

def combine_messages(greeting, name):
    # TODO: Convert this to return a combined message (e.g. "Hello, name!") instead of printing
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    greet_user("Neeraj")
    calculate_sum(2, 3)
    find_average([10, 20, 30, 40])
    uppercase_string("refactor me")
    combine_messages("Greetings", "Neeraj")