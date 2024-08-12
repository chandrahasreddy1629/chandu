data = {
    "first_name" : "ram",
    "last_name" : "krishna",
    "age" : 22
      }
print(data)


student_data = {
    "h_no" : 22,
    "street" : "dilsuknagar",
    "city" : "hyderabad",
    "percentage": 88.66,
    "marks" :[88,44,66,88,99]
}
print(student_data)
print(student_data["marks"])
print(student_data["marks"][2])
print(student_data.keys())
k=student_data.keys()
print(k)

student_data["h_no"] = 101
print(student_data)

student_data["fav_color"] = "red"
print(student_data)

student_data.pop("marks")
print(student_data)