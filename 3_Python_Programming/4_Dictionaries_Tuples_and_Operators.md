# Dictionaries, Tuples and Operators

---

## <ins> Practicals </ins>

### Practical 1 - XOR Gate

- An XOR gate is a digital logic gate that gives a true (1 or HIGH) output when the number of true inputs is odd
- You can build it using an AND gate whose inputs are the output of a NAND gate and the output of an OR gate
- If a = True and b = False Use logical operators to:
  - Check the output of an OR gate and store the value in a variable "c"
  - Check the out put of an AND gate and store the value in a variable "D"
  - Negate the value of D and store the value in a variable "D_Not"
  - Check the output of an AND gate if the inputs are C and D_Not
  - Can you do all these steps in one line?

```python
# >>> is used to represent stdout
a = True
b = False
c = a or b
>>> True
D = a and b
>>> False
D_not = not D
>>> True
xor_gate = D_not and c
>>> True

# In one line

xor_gate = (not(a and b)) and (a or b)
>>> True
```

### Practical 2 - Comparing Integers

- You have one variable:

```python
x = 10
```

- Use the function input() to ask the user for a number and store it in a variable n
- Print n is greater than 10 if the input is greater than 10 and the opposite if input is less than 10

```python
# >>> is used to represent stdout
x = 10

n = int(input("Choose a number: "))
if n > x:
    print(f"{n} is greater than 10")
else:
    print(f"{n} is less than 10")

>>> "Choose a number:" 9
>>> "9 is less than 10"
```

### Practical 3 - Comparing Different Data Types

- Test the evaluation of the following operations:
  - 99 > 5
  - 0 == False
  - 1 == True
  - 6.2 < 7
  - 9 >= 9
  - False < True

```python
# >>> is used to represent stdout
print(99 > 5)
>>> True
print(0 == False)
>>> True
print(1 == True)
>>> True
print(6.2 < 7)
>>> True
print(9 >= 9)
>>> True
print(False < True)
>>> True
```

### Practical 4 = Comparing Strings

- Test the result of these comparisons:
  - 'AAA' > 'BBB'
  - 'AAB' > 'AAA'
  - 'aaa' > 'AAB'

```python
# >>> is used to represent stdout
print('AAA' > 'BBB')
>>> False
print('AAB' > 'AAA')
>>> True
print('aaa' > 'AAA')
>>> True
```

- Why is this?

```txt
In python, characters in a string are a representation of a decimal number using ASCII encoding. 
The values of which are in the table below
Therefore:
    aaa = 97 + 97 + 97 = 291
    AAA = 65 + 65 + 65 = 195
```

![image](ASCII-Table-wide.svg.png)

### [Image Source](https://commons.wikimedia.org/wiki/File:ASCII-Table-wide.svg)
