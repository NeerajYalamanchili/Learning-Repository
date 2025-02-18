# Assignment for week of February 17, 2025

**Refactor and Test Your Hello World**

For this next assignment, you’re required to use **pytest** to test your Python file. Follow these steps:

1. **Refactoring**:
    
    - Refactoring means restructuring your existing code without changing its external behavior. It helps keep your code cleaner, more maintainable, and easier to test.
        
    - Below is an example Python script that has **five** functions using print statements. You need to refactor each function to _return_ its result instead of printing it directly:
        
    
    ```
    # hello_world.py
    
    def greet_user(name):
        # TODO: Convert this to return a string instead of printing
        print("Hello, " + name + "!")
    
    def calculate_sum(a, b):
        # TODO: Convert this to return the sum instead of printing
        print(a + b)
    
    def find_average(numbers):
        # TODO: Convert this to return the average instead of printing
        print(sum(numbers) / len(numbers))
    
    def uppercase_string(s):
        # TODO: Convert this to return the uppercase version instead of printing
        print(s.upper())
    
    def combine_messages(greeting, name):
        # TODO: Convert this to return a combined message (e.g. "Hello, name!") instead of printing
        print(greeting + ", " + name + "!")
    
    if __name__ == "__main__":
        greet_user("Neeraj")
        calculate_sum(2, 3)
        find_average([10, 20, 30, 40])
        uppercase_string("refactor me")
        combine_messages("Greetings", "Neeraj")
    ```
    
    - Your job is to transform these functions so they **return** their respective results rather than using `print`. For example, your final `greet_user` might look like:
        
    
    ```
    def greet_user(name):
        return f"Hello, {name}!"
    ```
    
    and you would handle printing (if desired) outside the function.
    
2. **Testing**:
    
    - Install pytest in your conda environment if you haven’t yet. For example:
        
        ```
        conda install pytest
        ```
        
        or
        
        ```
        mamba install pytest
        ```
        
    - Create a test file (e.g., `test_hello_world.py`) in the same directory and write tests that check these newly refactored functions. For example:
        
        ```
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
        ```
        
    - Run your tests using:
        
        ```
        pytest
        ```
        
        (or `python -m pytest` in the project folder)
        
3. **Commit and Push**:
    
    - Commit your updated `hello_world.py` and the new test file to your branch.
        
    - Push your changes and tag me as a reviewer on the Pull Request.
        

This process will help you get comfortable with writing testable functions in Python and verifying their correctness with a simple test. Remember, the goal is to keep your code clean, which is why we’re introducing the concept of **refactoring**.

As always, let me know if you have any questions or run into issues!