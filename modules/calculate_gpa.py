
def get_value(key, grades_dict):
    if key == 'A+':
        return grades_dict.get("A_PLUS")
    elif key == 'A':
        return grades_dict.get("A")
    elif key == 'A-':
        return grades_dict.get("A_MINUS")
    elif key == 'B+':
        return grades_dict.get("B_PLUS")
    elif key == 'B':
        return grades_dict.get("B")
    elif key == 'B-':
        return grades_dict.get("B_MINUS")
    elif key == 'C+':
        return grades_dict.get("C_PLUS")
    elif key == 'C':
        return grades_dict.get("C")
    elif key == 'C-':
        return grades_dict.get("C_MINUS")
    elif key == 'D+':
        return grades_dict.get("D_PLUS")
    elif key == 'D':
        return grades_dict.get("D")
    elif key == 'D-':
        return grades_dict.get("D_MINUS")
    elif key == 'F':
        return grades_dict.get("F")


def calculate(grades_credits_list, grades_dict):
    # write code from here
    total_grade_credit = 0
    total_credit = 0

    for course_info in grades_credits_list:
        # print(course_info[0], course_info[1])
        total_credit += course_info[1]
        temp_grade_point = get_value(course_info[0], grades_dict)
        try:
            total_grade_credit += temp_grade_point * course_info[1]
        except TypeError:
            print('Error')
    try:
        gpa = total_grade_credit / total_credit
        return '{:.2f}'.format(gpa)
    except ZeroDivisionError:
        return "error"


if __name__ == "__main__":
    # grades_dict = {
    #     'A_PLUS': None,
    #     'A': 4.0,
    #     'A_MINUS': 3.7,
    #     'B_PLUS': 3.3,
    #     'B': 3.0,
    #     'B_MINUS': 2.7,
    #     'C_PLUS': 2.3,
    #     'C': 2.0,
    #     'C_MINUS': 1.7,
    #     'D_PLUS': 1.3,
    #     'D': 1.0,
    #     'D_MINUS': None,
    #     'F': 0.0
    # }
    # grades_credits_list = [('A', 3.0), ('A-', 3.5), ('D', 4.0), ('B-', 2.5)]
    # print(calculate(grades_credits_list, grades_dict))

    print("It's a module!")
