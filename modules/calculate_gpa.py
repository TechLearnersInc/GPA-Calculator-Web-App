# calculate gpa

def calculate(grades_credits_list, grades_dict):
    # write code from here

    return

if __name__ == "__main__":
    grades_dict = {
        'A_PLUS': None,
        'A': 4.0,
        'A_MINUS': 3.7,
        'B_PLUS': 3.3,
        'B': 3.0,
        'B_MINUS': 2.7,
        'C_PLUS': 2.3,
        'C': 2.0,
        'C_MINUS': 1.7,
        'D_PLUS': 1.3,
        'D': 1.0,
        'D_MINUS': None,
        'F': 0.0
    }
    grades_credits_list = [('A', 3.0), ('A-', 3.5), ('D', 4.0), ('B-', 2.5)]
    calculate(grades_credits_list, grades_dict)
