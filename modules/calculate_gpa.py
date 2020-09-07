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

        if temp_grade_point == -1:
            return -1
        try:
            total_grade_credit += temp_grade_point * course_info[1]
        except TypeError:
            return -1
    try:
        gpa = total_grade_credit / total_credit
        final_gpa = '{:.2f}'.format(gpa)
    except (ZeroDivisionError, TypeError) as e:
        print(e)
        return -1

    return final_gpa


if __name__ == "__main__":
    print("It's a module!")
