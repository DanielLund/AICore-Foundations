# Functions

## <ins> Practicals </ins>

### Practical 1 - Range Checker

- Write a function called in_range which takes in a lower bound, an upper bound, and a number
- If it is, return "number is between lower bound and upper bound."
- If it isn't, return "number is NOT between lower bound and upper bound."
- Call your function to test it

```python
def in_range(lower, upper, num):
    if lower < num < upper:
        print(f"{num} is between {lower} and {upper}")
    else:
        print(f"{num} is not between {lower} and {upper}")

#tests
# >>> is used to represent stdout

in_range(10, 25, 12)
>>> "12 is between 10 and 25"
in_range(10, 50, 100)
>>> "100 is not between 10 and 50"
```

### Practical 2 - Default Arguments

- Create a function which takes in a dictionary of attributes about a piece of clothing and prints each of the key-value pairs on a line
- Define an input to the function called attributes_to_print with a default value of 'all'
- If a list is passed into the function as the attributes_to_print, print only the key-value pairs of the dictionary which the key appears for in that list
- Print a message to tell the user if a key doesn't exist
- Call your function to test it

```python

def dict_attr(clothes: dict, attributes_to_print=all):
    if attributes_to_print == all:
        for k, v in clothes.items():
            print(k, v)
    else:
        for attr in attributes_to_print:
            if attr not in clothes:
                print(f'The key "{attr}" does not exist')
            else:
                print(attr, clothes[attr])
```

### Practical 3 - Profile Validation

- Create a function which takes in the name, age, and email of a user trying to create a new profile on our application
- Check the name does not contain any of "!@£$%^&*()"
- Check the email is valid by making sure it contains "@"
- Check the age > 12
- Turn each step above into a function, so that you have one function, which calls 3 other functions inside
- Print a friendly error to explain the issue to the user if any of these checks does not pass

```python
def name_valid(name: str) -> bool:
    if name.isalpha():
        return True
    else:
        return False

def email_valid(email: str) -> bool:
    if '@' in email:
        return True
    else:
        return False

def age_valid(age: int) -> bool:
    if age > 12:
        return True
    else:
        return False

def profile_valid(name: str, emailL: str, age: int) -> str:
    if name_valid(name) == False:
        print("Sorry your name must not contain any of the following characters: !, @, £, $, %, ^, &, *, ( or )" )
    elif email_valid(email) == False:
        print("Please use a valid email format")
    elif age_valid(age) == False:
        print("Sorry you must be 13 or older in order to create a profile")
    else:
        print("Profile creation succesful!")

```

### Alternative Method Using Regular Expressions

**What are Regular Expressions?**

- Regular expressions (called REs, or regexes, or regex patterns) are essentially a tiny, highly specialized programming language embedded inside Python and made available through the re module.
- Using this little language, you specify the rules for the set of possible strings that you want to match; this set might contain English sentences, or e-mail addresses, or TeX commands, or anything you like.
- You can then ask questions such as “Does this string match the pattern?” or “Is there a match for the pattern anywhere in this string?”. You can also use REs to modify a string or to split it apart in various ways.

**Check out the python documentation on regular expressions:** [Docs](https://docs.python.org/3/howto/regex.html)

```python
import re

name_regex = '[!@£$%^&*()]'
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def name_valid(name: str) -> bool:
    if (re.search(name_regex, name)):
        return True
    else:
        return False

def email_valid(email: str) -> bool:
    if (re.fullmatch(email_regex, email) == None):
        return True
    else:
        return False

def age_valid(age: int) -> bool:
    if age <= 12:
        return True
    else:
        return False

def profile_valid(name: str, email: str, age: int):
    if name_valid(name) == True:
        print("Sorry your name must not contain any of the following characters: !, @, £, $, %, ^, &, *, ( or )" )
    elif email_valid(email) == True:
        print("Please use a valid email format")
    elif age_valid(age) == True:
        print("Sorry you must be 13 or older in order to create a profile")
    else:
        print("Profile creation succesful!")
```

### Practical 4 - Factorial Function

- Define a recursive function called "factorial" that returns the factorial of a given number.

```python
def factorial(num: int) -> int:
    if num == 1:
        return num
    else:
        return num * factorial(num-1)

# test
# >>> is used to represent stdout

factorial(10)
>>> 3628800
```

### Practical 5 - Fibonacci Function

- Create a function which takes in an integer n, and when called, returns a list of the first n Fibonnaci numbers. It should be a recursive function which calls itself inside the function body

```python
def fibonacci(num: int) -> int:
    if num <= 1:
        return num
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

#test
# >>> is used to represent stdout

fibonacci(25)
>>> 75025
```

### Practical 6 - Fibonacci Loop

- Write a for loop that prints the first 100 Fibonnaci numbers

- Create a function which returns true if the number is a multiple of 7 and false otherwise

- Call this function on each number inside your loop

- Add an elif condition to the loop to call another new function which checks if the number is greater than or equal to 100 OR is less than 50. In the case that it is true, format a string that prints the number and either "is larger than 100" or "is less than 50"

```python
# Same fibonacci function as previous practical

def fibonacci(num: int) -> int:
    if num <= 1:
        return num
    else:
        return(fibonacci(num-1) + fibonacci(num-2))

# First lets create our functions

def is_multiple_of_7(n: int) -> bool:
    if fibonacci(n) % 7 == 0:
        return True
    else:
        return False

def fib_greater_or_less(n: int) -> str:
    if fibonacci(n) < 50:
        print(f"{fibonacci(n)} is less than 50")
    elif fibonacci(n) >= 100:
        print(f"{fibonacci(n)} is greater than 100")
    else:
        return fibonacci(n)

# Now for the loop!

for n in range(1, 101):
    if is_multiple_of_7(n):
        print(f"{fibonacci(n)} is a multiple of 7")
    elif fib_greater_or_less(n):
        print(fib_greater_or_less(n))
```
