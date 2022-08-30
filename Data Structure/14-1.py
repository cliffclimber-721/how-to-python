def student_names(student_list, student_no):
    if student_no in student_list:
        return student_list[student_no]
    else:
        return "?"

student_info = {
    39: "Justin", 
    14: "John", 
    67: "Mike", 
    105: "Summer"
}

print(student_names(student_info, 14))
print(student_names(student_info, 10))