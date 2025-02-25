from hello_world import greet_user, calculate_sum, find_average, uppercase_string, combine_messages

def test_greet_user():
    assert greet_user("Neeraj") == "Hello, Neeraj!"

def test_calculate_sum():
    assert calculate_sum(2, 3) == 5

def test_find_average():
    assert find_average([10, 20, 30, 40]) == 25

def test_uppercase_string():
    assert uppercase_string("refactor me") == "REFACTOR ME"

def test_combine_messages():
    assert combine_messages("Greetings", "Neeraj") == "Greetings, Neeraj!"