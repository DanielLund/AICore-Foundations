# Arithmetic, Variable Assignment and Strings

---

## <ins>Practicals</ins>

### Practical 1 - String Length

- Print the length of the word:
  
```python
long_word = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
```

- Access the first letter of long_word by indexing the variable and assign it to first_c. Access the last letter of long_word and assign it to last_c. Use an arithmetic operator to append last_c to first_c and print the result

```python
# >>> is used to represent stdout
long_word = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
print(len(long_word))
>>> 45

first_c = long_word[0]
last_c = long_word[-1]
first_c += last_c

print(first_c)
>>> "Ps"
```

### Practical 2 - Basic Arithmetic

- You have two variables:

```python
a = 42
b = 45
```

- Print the sum of a and b
- Print the difference of a and b
- Print the product of a and b
- Print the division of a by b
- Now set a = 4.2
- Print the type of a + b. What happens and why?

```python
# >>> is used to represent stdout
a = 42
b = 45
print(a + b)
>>> 87
print(b - a)
>>> 3
print(a * b)
>>> 1890
print(a / b)
>>> 0.93333333
a = 4.2
print(type(a + b))
>>> <class 'float'>
# float, because 4.2 is a float and therefore 49.2 is a float
```
