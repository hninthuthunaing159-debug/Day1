def greet():
    print("Hello from UCSPyay")

greet()

def greet(name):
    print(f"Hello,{name}!")

greet("Ma Ma")
greet("Mg Mg")


def calculate_average(scores):
    if len(scores)==0:
        return 0
    return sum(scores)/len(scores)
    
scores=[45,70,85]
result=calculate_average(scores)
print("Average",result)

#exercise

def calculate_total(scores):
    if len(scores)==0:
        return 0
    return sum(scores) /len(scores)

marks=[70,80,90]
result=calculate_total(marks)

def calculate_average(scores):
    if len(scores)==0:
        return 0
    return sum(scores) /len(scores)

marks=[70,80,90]
result=calculate_average(marks)

print("calculate_total:",result)
print("calculate_average:",result)

def classify_grade(score):
    if score< 80 or score >100:
        return"A"
    elif score >=60:
        return"B"
    elif score>=40:
        return"C"
    else:
        return "D"
print(classify_grade("85"))
print(classify_grade("49"))


    

