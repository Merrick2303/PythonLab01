import math

r = 5
a= math.pi * r**2
v = 4/3 * math.pi * r**3
a_side = 3
b_side = 4
pyt = math.sqrt(a_side**2 + b_side**2)
first_name = "Merrick"
last_name = "Crabb"
full_name = first_name + '' + last_name
name_len = len(full_name)
print(a, v, pyt, name_len, full_name, full_name.upper(),full_name.lower())

age = 18
weight =170
height = 5.10
inches = height * 12

print(type(age), type(weight), type(height))
bmi = weight / (height**2) * 703
print(bmi)
print("goodbye")