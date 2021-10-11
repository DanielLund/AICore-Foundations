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
