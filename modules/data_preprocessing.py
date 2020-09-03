import json


class DataPreProcessingGPA:
    """Pre-processing the GPA Calculation data that was given by frontend"""

    def __init__(self, gpa_json):
        self.__dict__ = json.loads(gpa_json)
        self.all_grades_avail = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
        self.grade_sheet = dict()

    def clean_data(self):
        # Load the grading system
        grade_sheet_dict = json.loads(self.__dict__["gpa_grade_sheet"])
        self.__dict__.pop("gpa_grade_sheet")
        # Store users grades and credits
        grades_list = list()
        credits_list = list()
        try:
            for key, value in self.__dict__.items():
                split_keys = key.split("_")
                if split_keys[0] == "Select" and split_keys[1] == "Field":
                    id = split_keys[2]
                    find_credit = "Input_Field_" + str(id)

                    get_credit = self.__dict__[find_credit]

                    # Validate Grades & Credits
                    if value in self.all_grades_avail:
                        grades_list.append(value)
                        credits_list.append(get_credit)

                else:
                    continue
        except:
            return "ERROR"

        if len(credits_list) != len(grades_list):
            return "ERROR"

        try:
            for key, value in grade_sheet_dict.items():
                if value:
                    # validate the key
                    self.grade_sheet[key] = float(value)
                else:
                    self.grade_sheet[key] = None
        except:
            return "ERROR"

        data_list = [self.grade_sheet, grades_list, credits_list]
        return data_list
