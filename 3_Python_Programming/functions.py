#%%
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

def profile_valid(name: str, email: str, age: int) -> str:
    if name_valid(name) == False:
        print("Sorry your name must not contain any of the following characters: !, @, £, $, %, ^, &, *, ( or )" )
    elif email_valid(email) == False:
        print("Please use a valid email format")
    elif age_valid(age) == False:
        print("Sorry you must be 13 or older in order to create a profile")
    else:
        print("Profile creation succesful!")

# %%
name = "da!niel"
email = "daniel.lund@bath.edu"
age = 23
profile_valid(name, email, age)

# %%
