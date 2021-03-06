import json


class DataPreProcessingGPA:
    """Pre-processing the GPA Calculation data that was given by frontend"""

    def __init__(self, gpa_dict):
        self.__dict__ = gpa_dict
        self.all_grades_avail = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
        self.grade_sheet = dict()
        self.error = False

    def clean_data(self):
        # Load the grading system
        grade_sheet_dict = json.loads(self.__dict__["gpa_grade_sheet"])
        self.__dict__.pop("gpa_grade_sheet")
        # Store users grades and credits
        grades_credits_list = list()

        try:
            for key, value in self.__dict__.items():
                split_keys = key.split("_")
                if split_keys[0] == "Select" and split_keys[1] == "Field":
                    index = split_keys[2]
                    find_credit = "Input_Field_" + str(index)
                    get_credit = self.__dict__[find_credit]
                    # Validate Grades & Credits
                    if value in self.all_grades_avail and get_credit:
                        grades_credits_list.append((value, float(get_credit)))

                else:
                    continue
        except (TypeError, IndexError, KeyError) as e:
            print(e)
            return -1

        try:
            for key, value in grade_sheet_dict.items():
                if value:
                    # Validate the key
                    self.grade_sheet[key] = float(value)
                else:
                    self.grade_sheet[key] = -1
        except (TypeError, KeyError) as e:
            print(e)
            return -1

        data_list = [self.grade_sheet, grades_credits_list]
        return data_list


if __name__ == '__main__':
    print("This is a module written for data preprocessing")
