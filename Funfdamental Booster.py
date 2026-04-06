print("welcome to the interactive personal data collector")
name=input("enter your name :-")
age=int(input("enter you age :-"))
height=float(input("enter you height:-"))
fav_number=int(input("enter you fav_number:-"))
print("Thank You! Here Is The Information We Collected:")

print(f"name:{name} ,type= {type(name)},memory address = {id(name)}")
print(f"name:{height} ,type= {type(height)},memory address = {id(height)}")
print(f"name:{age} ,type= {type(age)},memory address = {id(age)}")
print(f"name:{fav_number} ,type= {type(fav_number)},memory address = {id(fav_number)}")
year=2025
Man=year-age
print(Man)