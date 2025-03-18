def calculate_class_averages(classrooms):
    class_averages = {}
    for classroom, students in classrooms.items():
        if not students:
            class_averages[classroom] = 0
            continue
        scores = 0
        num_grades = 0
        for grades in students.values():
            for grade in grades:
                scores += grade
                num_grades += 1
        avg = scores / num_grades
        class_averages[classroom] = avg
        
    return class_averages  
         
# create result dict
# for loop throuh classriom to get each class and its student
# create veraiabke to store all scores
# loop through students abd get eac grade abd add tgem t the sum variabke
# find average by deviding sum by number of scires
# add key value pair into reslut dict(class: avg_score)
#return result
