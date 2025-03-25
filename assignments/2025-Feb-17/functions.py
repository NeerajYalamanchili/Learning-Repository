

def greet_user(name):
    # TODO: Convert this to return a string instead of printing
    return f"Hello, {name}!"

def calculate_sum(a, b):
    # TODO: Convert this to return the sum instead of printing
    return a + b

def find_average(numbers: list[int]):
    # TODO: Convert this to return the average instead of printing
    return sum(numbers) / len(numbers)

def uppercase_string(s):
    # TODO: Convert this to return the uppercase version instead of printing
    return s.upper()

def combine_messages(greeting, name):
    # TODO: Convert this to return a combined message (e.g. "Hello, name!") instead of printing
    # Another comment!!!!!!
    return f"{greeting}, {name}!"

def say_hello():
    return "hello!"

def f(x):
    x += 10
    return 3 * x + 2

def g(x):

    return f(x) * 10

def new_function_for_git_learning():
    pass

if __name__ == "__main__":
    # print(greet_user("Neeraj"))
    # print(calculate_sum(2, 3))
    # print(find_average([10, 20, 30, 40]))
    # print(uppercase_string("refactor me"))
    # print(combine_messages("Greetings", "Neeraj"))
    # print(f(10))
    # print(x)
    numbers = [1,2,3,4,5]
    for i, number in enumerate(numbers):
        if number % 2 != 0:
            print(i)
            print(number)
        if i >=2:
            break