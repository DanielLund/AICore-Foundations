# Object-Oriented Programming

---

## <ins> Practicals </ins>

### Practical 1 - Cylinder Class

- Try defining a class for a cylinder.
- It should contain two parameters:
  - height and radius, which should have a default value of 1.
- Four attributes:
  - height
  - radius
  - surface_area, initialised as None
  - volume, initialised as None
- Two methods:
  - get_surface_area: define surface_area, update attribute surface_area, return surface_area rounded to 2dp.
  - get_volume: define volume, update attribute volume, return volume rounded to 2dp.
- Use google to find the formulae for surface area and volume of a cylinder.
- Use the formulae to create method definitions for these.

```python
from math import pi

class Cylinder:
    def __init__(self, height: int=1, radius: int=1) -> None:
        self.height = height
        self.radius = radius
        self.surface_area = None
        self.volume = None
    
    def get_surface_area(self):
        #2 pi r(r+h)
        self.surface_area = 2 * pi * self.radius * (self.radius + self.height)
        format_surface_area = f"{self.surface_area:.2f}"
        return format_surface_area
    
    def get_volume(self):
        #pi r2 h
        self.volume = pi * (self.radius ** 2) * self.height
        format_volume = f"{self.volume:.2f}"
        return format_volume

# Test
# >>> is used to represent stdout
cyl = Cylinder(1, 2)
print(cyl.get_surface_area())
>>> 37.70
print(cyl.get_volume())
>>> 12.57
```

### Practical 2 - Car Class

- Create a car class
- Define the initialiser:
  - It should take in two arguments (other than `self`), and assign these as attributes of the instance:
    - One called model (e.g. Tesla), which has no default
    - One called year, which is an integer, which defaults to the current year (just hard code the current year in)
- It should also define a new attribute, one called miles_driven, which is set to zero
- Create a method called drive
- It should `print('vroom')` and increment the instance's miles_driven attribute by 1
- Create a method called info
- It should then print the number of miles driven, the model name and the year
- Initialiase the class
- call all of the methods

```python
class Car:
    def __init__(self, model: str, year: int=2021, miles_driven: int=0):
        self.model = model
        self.year = year
        self.miles_driven = miles_driven
    
    def drive(self):
        self.miles_driven += 1
        print('vroom')  

    def info(self):
        print(self.__dict__)


# test
# >>> is used to represent stdout

car_1 = Car('Tesla', 2009, 1)

car_1.drive()
>>> vroom

car_1.info()
>>> {'model': 'Tesla', 'year': 2009, 'miles_driven': 2}
```

### Practical 3 - Person Class

- Create a class called Person
- Define its initialiser
  - it must take in a name, and a date of birth in ISO format (YYYY-MM-DD), and optionally a list of "friends"
  - it should initialise attributes for each of those
- Instantiate your class and test that it works before
  continuing - do this for every section going forward
- Define a magic method which prints a string representation
  of the person, detailing their name, DOB and number of friends
- Define a magic method that defines how to use the greater
  than sign to compare the age of two people (hint: it's not complicated - does ">" work on strings? what does it do? hence why is the ISO format important?)
- Create a method called `add_friend`, which takes in another
  instance of the person class and adds it to this instance's friends attribute. Assume that every relationship goes both ways: this method should append each friend to the other's list, in just one call
- Assert that the type of the object passed into `add_friend`
  is an instance of the Person class. What's an assertion error?
- Safely handle the assertion error

```python
import dateutil.parser as parser
class Person:
    def __init__(self, name: str, DOB: str, friends=[]):
        date = parser.parse(DOB)
        self.name = name
        self.DOB = date.isoformat().split('T')[0]
        self.friends = friends

    def __gt__(self, other):
        try: 
            isinstance(other, Person)
        except AssertionError as e:
            print(e)
        else:
            if self.DOB < other.DOB:
              print(f'{self.name} is older than {other.name}')
        else:
          print(f'{other.name} is older than {self.name}')

    def __repr__(self):
        return f'{self.name}, {self.DOB}, Current number of friends: {len(self.friends)}'

    def add_friend(self, other):
        try: 
          assert isinstance(other, Person)
        except AssertionError as e:
          print(e)
        else:
          self.friends.append(other.name)
          self.friends += other.friends
          other.friends += self.friends
          #Cast both friends attributes into a set then back into a list to drop duplicates
          return list(set(self.friends)), list(set(other.friends))
```

### Practical 4 - Shape Class

- Define a class called `Shape`
- Define it's initialiser and initialise two attributes:
  - `num_sides`, which is required
  - `tesselates`, which is optional
  - raise an error if `num_sides` is zero
- Define a method called get_info which RETURNS a string
  telling us the number of sides of the shape and whether it tesselates or not.
- For now, make this function raise a `NotImplementedError` if
  called.
- That's because this is an "abstract base class", which means
  it should only be used when inherited from by other classes.
- I.e. there should be no instances of this generic Shape class
- Create the following classes which inherit from shape
  - `Circle`
  - `Triangle`
  - `Square`
  - `Pentagon`
  - `Hexagon`
  - `ManySidedPolygon`
- Make sure to remember to use the `super()` method in the
  initialiser of each of them to initialise the parent class
- For each of them, overwrite the `get_info` function and make
  it return the correct info mentioned earlier. Overwriting this will prevent the `NotImplementedError` being raised.
- Define the correct magic method which defines what is
  printed when we print an instance of the Shape class. It should probably just call the `get_info` method
- Define a magic method of the Shape class which defines how
  to "add" two instances of the Shape class together and returns a new shape with as many sides as the sum of the individual shapes added

```python
class Shape:
    def __init__(self, num_sides, tesselates=None):
        self.num_sides = num_sides
        self.tesselates = tesselates
        if self.num_sides == 0:
          raise ValueError('num_sides must be > 0')
  
    def get_info(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, num_sides, tesselates=None):
        super().__init__(num_sides, tesselates)
    
    def _get_info(self):
        return f'Number of sides: {self.num_sides}, Tesselates: {"yes" if self.tesselates else "no"}'
    
    def __repr__(self):
        return self._get_info()
    
    def __add__(self, other):
        new_sides = self.num_sides + other.num_sides
        if new_sides == 4:
            new_shape = Square(new_sides, tesselates=True)
        elif new_sides == 5:
            new_shape = Pentagon(new_sides)
        elif new_sides == 6:
            new_shape = Hexagon(new_sides)
        else:
            new_shape = ManySidedPolygon(new_sides)  
        return new_shape
    
class Triangle(Shape):
    def __init__(self, num_sides, tesselates=None):
        super().__init__(num_sides, tesselates)
    
    def _get_info(self):
        return f'Number of sides: {self.num_sides}, Tesselates: {"yes" if self.tesselates else "no"}'
    
    def __repr__(self):
        return self._get_info()
    
    def __add__(self, other):
        new_sides = self.num_sides + other.num_sides
        if new_sides == 4:
            new_shape = Square(new_sides, tesselates=True)
        elif new_sides == 6:
            new_shape = Hexagon(new_sides)
        else:
            new_shape = ManySidedPolygon(new_sides)
        return new_shape

class Square(Shape):
    def __init__(self, num_sides, tesselates=None):
        super().__init__(num_sides, tesselates)
    
    def _get_info(self):
        return f'Number of sides: {self.num_sides}, Tesselates: {"yes" if self.tesselates else "no"}'
    
    def __repr__(self):
        return self._get_info()
    
    def __add__(self, other):
        new_sides = self.num_sides + other.num_sides
        if new_sides == 5:
            new_shape = Pentagon(new_sides)
        else:
            new_shape = ManySidedPolygon(new_sides)
        return new_shape

class Pentagon(Shape):
    def __init__(self, num_sides, tesselates=None):
        super().__init__(num_sides, tesselates)
    
    def _get_info(self):
        return f'Number of sides: {self.num_sides}, Tesselates: {"yes" if self.tesselates else "no"}'
    
    def __repr__(self):
        return self._get_info()
    
    def __add__(self, other):
       def __add__(self, other):
        new_sides = self.num_sides + other.num_sides
        if new_sides == 6:
            new_shape = Hexagon(new_sides)
        else:
            new_shape = ManySidedPolygon(new_sides)
            
        return new_shape

class Hexagon(Shape):
    def __init__(self, num_sides, tesselates=None):
        super().__init__(num_sides, tesselates)
    
    def _get_info(self):
        return f'Number of sides: {self.num_sides}, Tesselates: {"yes" if self.tesselates else "no"}'
    
    def __repr__(self):
        return self._get_info()
    
    def __add__(self, other):
        new_sides = self.num_sides + other.num_sides
        new_shape = ManySidedPolygon(new_sides)
        return new_shape

class ManySidedPolygon(Shape):
    def __init__(self, num_sides, tesselates=None):
        super().__init__(num_sides, tesselates)
    
    def _get_info(self):
        return f'Number of sides: {self.num_sides}, Tesselates: {"yes" if self.tesselates else "no"}'
    
    def __repr__(self):
        return self._get_info()
    
    def __add__(self, other):
        new_sides = self.num_sides + other.num_sides
        new_shape = ManySidedPolygon(new_sides)
        return new_shape
```

- There is no 2 sided shape so n+2 for num_sides is not
  possible
- You also can't have shapes with smaller num sides than the
  original shape
- So you can have n+1, n+3, n+4....2n sides where n != 2
- Therefore no way of creating a triangle using add method
- Also, should change square, triangle to tesselates == True

### Practical 5 - Create your own game of hangman

- It's up to you how you implement it
- You don't have to actually visualise the drawing of the man
  hanging
- Start simple, with everything running cell by cell
- Group code which works together to perform a single task
  into a single function
- When you have a simple working mvp, try and put your code
  into a `Hangman` class
- It is expected you use
  - OOP
- Extra points for
  - using unpacking
  - using magic methods

```python
import random
WORDS = ['deadpool', 'titanic', 'seven', 'django']


class Hangman():
    """
    The hangman game class with its methods
    """

    def __init__(self, words: list[str], lives: int):
        self.failed_attempts = 0
        self.lives = lives
        self.words = words
        self.word_to_guess = random.choice(self.words)
        self.game_progress = list('_' * len(self.word_to_guess))

    def find_indexes(self, letter: str):
        """
        Method that takes a letter and returns a list with his indexes in
        the word to guess
        :param letter: String, Letter to find his indexes
        """
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]

    def is_invalid_letter(self, input_):
        """
        Method to validate if an user input is not just a letter (it means the
        input is a number or a text with more than 1 char)
        :param input_: String, user input to be validated
        """
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    def print_game_status(self):
        """
        Method to print the word to guess blankspaces with the remaining
        attempts and the guessed letters
        """
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes):
        """
        Method to update the game progress with the guessed letters
        :param letter: String, Letter to be added to the game progress
        :param indexes: List, found occurrences (as indexes) of the given
                        letter in the word
        """
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        user_input = input('\nPlease type a letter: ')
        return user_input

    def play(self):
        """
        Method to play the game, it prompts the user for a letter and plays
        the game until the user guesses the word or lose his attempts
        """
        while self.failed_attempts < self.lives:
            self.print_game_status()
            user_input = self.get_user_input()

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print('The input is not a letter!')
                continue
            
            # Check if the letter is not already guessed
            elif user_input in self.game_progress:
                print('You already have guessed that letter')
                self.failed_attempts += 1
                continue

            elif user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                # If there is no letter to find in the word
                if self.game_progress.count('_') == 0:
                    print('You win!')
                    print(f'The word is: {self.word_to_guess}')
                    break
        
            else:
                print('Sorry, wrong letter!')
                self.failed_attempts += 1
        if self.failed_attempts == self.lives:
            print('Sorry, you lost!')
if __name__ == '__main__':
    hangman = Hangman(WORDS, 5)
    hangman.play()

```
