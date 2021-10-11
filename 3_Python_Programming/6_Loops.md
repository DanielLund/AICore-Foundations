# Loops

## <ins> Practicals </ins>

### Practical 1 - Counting Even and Odd Numbers

- Write a for loop to count how many even and odd numbers between 1 and 100.

```python
# >>> is used to represent stdout
odd_count = 0
even_count = 0
for num in range(101):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(odd_count)
print(even_count)
>>> 50
>>> 51
```

### Practical 2 - Palidrome?

- Create a function which checks whether a word is a palindrome or not

```python
def palindrome(word: str) -> str:
    if word[::-1] == word:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
```

### Practical 3 - Budget Calculator

- Using the names dictionary and order_list shown below, write a program that fits the following conditions:
  - It should produce an order by adding items to receipt from order_list sequentially.
  - It should Print "Current Total: £x" with each iteration
  - If the order value exceeds the budget value, it should stop adding items and print "Budget Exceeded!".
  - If not, each time it adds items, it should:
  - Print "Adding *full name of item* (quantity)".
  - Subtract the price from budget.
  - Add the price to running_total.
  - It should print out running_total, order and budget formatted into print statements (done for you).

```python
order_list = [("tom", 0.87, 4), 
            ("sug", 1.09, 3), 
            ("ws", 0.29, 4), 
            ("juc", 1.89, 1), 
            ("fo", 1.29, 2)]

names = {"tom":"Tomatoes",
            "sug":"Sugar",
            "ws":"Washing Sponges",
            "juc":"Juice",
            "fo":"Foil"
        }
budget = 10.00

running_total = 0

receipt = []
```

```python
def create_order(order_list, names):
    running_total = 0
    budget = 10
    receipt = []
    for order in order_list:
        this_order_price = order[1] * order[2]
        budget -= this_order_price
        print(f"Current Total: £{running_total:.2f}")
        if budget  <= 0.0:
            print("Budget Exceeded")
            break
        else:
            running_total += this_order_price
            print(f"Budget Remaining: £{budget:.2f}")
            receipt.append(names[order[0]])
            receipt.append(f"£{this_order_price:.2f}")
            pass
    print(f"Receipt: {receipt}, Total: £{running_total:.2f}")

# Result using the given names and order_list
# >>> is used to represent stdout

create_order(order_list, names)

>>> 
Current Total: £0.00
Budget Remaining: £6.52
Current Total: £3.48
Budget Remaining: £3.25
Current Total: £6.75
Budget Remaining: £2.09
Current Total: £7.91
Budget Remaining: £0.20
Current Total: £9.80
Budget Exceeded
Receipt: ['Tomatoes', '£3.48', 'Sugar', '£3.27', 'Washing Sponges', '£1.16', 'Juice', '£1.89'], Total: £9.80
```

### Practical 4 - Even and Odd List Comprehension

- Create a list comprehension that squares even arguments, and adds 1 to and squares odd arguments
- Test on my_list:
    my_list = [34,52,71,39,22,73,92]

```python
# >>> is used to represent stdout
def even_odd(ls: list) -> list:
    return [n**2 if n % 2 == 0 else (n + 1) ** 2 for n in ls]
even_odd(my_list)
>>> [1156, 2704, 5184, 1600, 484, 5476, 8464]
```

### Practical 5 - Dictionaries and List Comprehensions

- Create a dictionary with 2 keys
  - name: a string of your name
  - skills: a list of strings
- Make another one of these and put both of them in a list
- Now index that list of dictionaries to find the last letter of the first skill of the last dictionary
- Create a list comprehension which maps that list to a list of the length of names
- Add that list together to get the total number of characters in all of the names

```python
# >>> is used to represent stdout
dict_1 = {
    "name": "Dan",
    "skills": ["Python", "Machine Learning", "Maths"]
}
dict_2 = {
    "name": "Harry",
    "skills": ["Python", "Machine Learning", "Maths", "Teaching"]
}

list_of_dicts = [dict_1, dict_2]

first_letter = list_of_dicts[-1]["skills"][0][0]

len_names = [len(dict_item['name']) for dict_item in list_of_dicts]
print(len_names)
>>> [3, 5]
total_length = sum(len_names)
print(total_length)
>>> 8
```

### Practical 6 - Shop Item Filter

- Filter shop_dict using list comprehension to find only items with values of over 1.00
- Assign them to a list called filtered_shop by their full names, not their codes, using names_dict.

```python
shop_dict = {
    "tom":0.87,
    "sug":1.09,
    "ws":0.29,
    "cc":1.89,
    "ccz":1.29
    }

names_dict = {
    "tom":"Tomatoes",
    "sug":"Sugar",
    "ws":"Washing Sponges",
    "cc":"Coca-Cola",
    "ccz":"Coca-Cola Zero"
    }

shop_list = [(k, v) for k, v in shop_dict.items() if v > 1.00]
print(shop_list)
>>> [('sug', 1.09), ('cc', 1.89), ('ccz', 1.29)]

filtered_shop = [(names_dict[shop_list[n][0]], shop_list[n][1]) for n in range(len(shop_list))]
print(filtered_shop)
>>> [('Sugar', 1.09), ('Coca-Cola', 1.89), ('Coca-Cola Zero', 1.29)]
```

### Practical 7 - Shape Maker

- Write a program to produce the following pattern.
- CLUE: Use nested for loops, using one nested loop to increase in size and another to decrease.
- Start with n=5
- Example:

```txt
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
```

#### Code

```python
def shape_maker():
    rows = int(input('input rows: '))
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")

    for i in range(rows, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print("\r")

# Example
# >>> is used to represent stdout
shape_maker()
>>> "input rows: "
7
>>> 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
```
