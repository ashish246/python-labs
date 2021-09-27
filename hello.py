age=38
age=39
first_name = "Ashish"
is_online = True
print("Hello World")
print(age)

# name = input("What is your name? ")
# print("Hello " + name)

# birth_year = input("What is your birth year? ")
# age = 2021 - int(birth_year)
# print(age)

# first = float(input("First: "))
# second = float(input("Second: "))
# sum = first + second
# print(" Sum: " + str(sum))

course = "Python for Beginners"
print(course.upper())
print(course.find('y'))
print('Python' in course)
# print(course)

#tuples
numbers = (1,2,3)
#unpacking
x,y,z = numbers
print(x)

# Dictionary
customer = {
    "name": "Ashish",
    "email": "ashish@gmail.com",
    "age": 30
}
print(customer["name"])
print(customer.get("Name", "Ashish T")) # To get around the error

try:
    age = int(input("age? "))
    print(age)
except ValueError:
    print('Invalid Value')