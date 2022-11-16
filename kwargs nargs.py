def get_best_student(**kwargs):
    top_students = [] 
    for k, v in kwargs.items():
        if v >= 90:
            top_students.append(k)
    return top_students
top_stud = get_best_student(priya=99,guddu=77,eva=22,yuvan=55,ravi=98)    
print (f"our top students are {top_stud}")
def count_50(*args):
    count = 0
    for i in args:
        if i>50:
            count = count+1
    return count     
total_count = count_50(3,5,6,8,9,9,8,2,3)   
print(f"total count above 50 is {total_count}")           
                 