def sing (name,age):
    print ("Happy Birthday", name)
    print ("I will sing", age, "times")
    age = 19
    return name, age

newage, newname = sing (age = 23, name = "Margie")
print (age)
