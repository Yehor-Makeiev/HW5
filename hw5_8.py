grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    n = 1
    result = []
    for student in students:
        result.append("{:>4}|{:<10}|{:^5}|{:^5}".format(n, student, students[student], grades[students[student]]))    
        n += 1
    return print(result)
    
    
# formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"})     


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}  
for el in formatted_grades(students):
    print(el)        