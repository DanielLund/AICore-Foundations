# Control Flow

---

## <ins> Practicals </ins>

### Practical 1 - BMI Checker

- Given 2 parameters, height and weight, calculate the parameter BMI (Google the formula) (For simplicity, work in metres and kg)
- Using the parameter BMI, write a series of if statements that print the following outcomes:
  - below 18.5 –-> 'Your BMI is x. You're in the underweight range.'
  - between 18.5 and 24.9 –-> 'Your BMI is x. You're in the healthy weight range.'
  - between 25 and 29.9 –-> 'Your BMI is x. You're in the overweight range.'
  - between 30 and 39.9 –-> 'Your BMI is x. You're in the obese range.'
- Test your code with the following cases:
  - Height = 1.83m, weight = 85kg
  - Height = 1.55m, weight = 61kg
  - Height = 2.09m, weight = 135kg
  - Height = 1.71m, weight = 70kg
  - Height = 1.71m, weight = 95kg
  - Height = 1.71m, weight = 55kg
- **Hint:** Run as a cell and change the input for each test case to make things less tedious.

```python
height = float(input('input height: '))
weight = float(input('input weight: '))

BMI = weight/(height**2)

if BMI < 18.5:
    print(f"Your BMI is {BMI:.2f}. You are in the underweight range.")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI:.2f}. You are in the healthy range.")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI:.2f}. You are in the overweight range.")
elif 30 <= BMI <40:
    print(f"Your BMI is {BMI:.2f}. You are in the obese range.")
else:
    print("Unable to calculate BMI")
```

### Practical 2 - Flight Safety Checker

- Given 2 parameters, altitude(ft) and airspeed(knots), write a program that categorises entries into 'safe flying' and 'unsafe flying' based on the following criteria:
  - An altitude of below 100ft or above 50000ft is considered unsafe flying
  - An airspeed of 60 knots and below or 500 knots and above is considered unsafe flying
  - Altitudes and airspeeds outside these ranges are considered sage flying
- Try to write your code as cleanly as possible and use the following cases to test your program:
  - altitude 25000ft, airspeed 300kn
  - altitude 50001ft, airspeed 250kn
  - altitude 90ft, airspeed 125kn
  - altitude 500ft, airspeed 45kn
  - altitude 1000ft, airspeed 600kn
  - altitude 65000ft, airspeed 700kn

```python
altitude = int(input('input altitude: '))
airspeed = int(input('input airspeed: '))

if altitude < 100 or altitude > 50000:
    print("This is unsafe flying, adjust your altitude")
elif: airspeed <=60 or airspeed >= 500:
    print("This is unsafe flying, adjust your airspeed")
else:
    print("Thank you for practicing safe flying)
```
