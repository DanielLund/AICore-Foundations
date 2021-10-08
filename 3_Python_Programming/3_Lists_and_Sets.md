# Lists and Sets

---

## <ins> Practicals </ins>

### Practical 1 - Username List

- Create a list of usernames
- Print the type of the list
- Print the length of the list
- Print the type of the first list item
- Find the length of the last name

```python
# >>> is used to represent stdout
user_list = ['Dan', 'Faiz', 'Harry']
print(type(user_list))
>>> <class 'list'>
print(len(user_list))
>>> 3
print(type(user_list[0]))
>>> <class 'str'>
print(len(user_list[-1]))
>>> 5
```

### Practical 2 - List Elements

- Create a new list of 5 elements with a different data type, name it "list_1"
- Now create a new list (list_2) with 10 zeros, do it using the * operator
- Nest list_1 and list_2 into a new list named list_3
- Access the fourth element of both lists in list_3 and store the elements in a new list named list_4

```python
# >>> is used to represent stdout
list_1 = [True, 'True', 1, 1.0, (1, )]
list_2 = [0] * 10
print(list_2)
>>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list_3 = [list_1, list_2]
print(list_3)
>>> [[True, 'True', 1, 1.0, (1,)], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
list_4 = [list_3[0][3], list_3[1][3]]
print(list_4)
>>> [1.0, 0]
```

### Practical 3 - Car Number Plate Year

- Given the following list of number plates:

```python
["G06 WTR", "WL11 WFL", "QW68 PQR"]
```

- Extract the last two characters, which represent the year of the car
- Print the type of each of them
- Convert each of these years to an integer type

```python
# >>> is used to represent stdout
plates = ["G06 WTR", "WL11 WFL", "QW68 PQR"]
dates = []
for plate in plates:
    plate_split = plates.split()[0]
    date = plate_split[-2:]
    dates.append(date)
print(dates)
>>> ['06', '11', '68']
for n in range(len(dates)):
    print(type(dates[n]))
>>> <class 'str'>
    <class 'str'>
    <class 'str'>
for n in range(len(dates)):
    dates[n] = int(dates[n])
    print(type(dates[n]))
>>> <class 'int'>
    <class 'int'>
    <class 'int'>
```

### Practical 4 - Name Character Intersection

- Create a set of names
- Find the characters which appear in every name

```python
# >>> is used to represent stdout
user_list = ['Dan', 'Harry', 'Faiz']
dan = set(user_list[0])
harry = set(user_list[1])
faiz = set(user_list[2])
common = dan.intersection(harry).intersection(faiz)
print(common)
>>> {'a'}
```

### Practical 5 - Multiplying List Elements

- Create a list of ten zeros using the * operator and name it list_1
- Create a set from list_1 and print its length

```python
# >>> is used to represent stdout
list_1 = [0] * 10
set_1 = set(list_1)
print(len(set_1))
>>> 1
print(set_1)
>>> {0}
```
