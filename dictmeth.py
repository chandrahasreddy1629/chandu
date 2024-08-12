student_data ={
    "name" : "ram",
    "age" : 22,
    "college" : "dps",
    "city" : "hyderabad"
}

print(student_data.items())
x = student_data.items()
k= student_data.keys()
print(k)

v= student_data.values()
print(v)

student_data.update({"state":"ap"})
print(student_data)
