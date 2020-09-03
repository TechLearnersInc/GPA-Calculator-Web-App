"use strict";

/*
    Grade Sheet
*/


// Regular Expression for Number Only Input
$(document).ready(function () {
    // Variables
    let grade_sheet_form_id = "grade_sheet_form";
    let grade_sheet_modal_id = "gradeSheetModal";
    let gpa_grade_sheet_input_box_id = "gpa_grade_sheet"

    $(`#${grade_sheet_form_id}`).submit(
        function (event) {
            event.preventDefault();
            $(`#${grade_sheet_modal_id}`).modal('toggle');

            let gradeSheet = {};
            $(`#${grade_sheet_form_id} input`).each(
                function (index) {
                    let input = $(this);
                    gradeSheet[input.attr('name')] = input.val().trim();
                }
            );
            console.log(gradeSheet);

            for (let grade of Object.keys(gradeSheet)) {
                $(`input[id="${grade}"]`).on(
                    "input blur paste",
                    function () {
                        let inputField = $(this);
                        if (isNaN(Number(inputField.val()))) {
                            inputField.val("😠");
                            window.setTimeout(function () {
                                inputField.val("");
                            }, 250);
                        } else {
                            inputField.val(inputField.val().trim());
                        }
                    }
                );
            }

            $(`input[id='${gpa_grade_sheet_input_box_id}']`).val(
                JSON.stringify(gradeSheet)
            );
            console.log(JSON.stringify(gradeSheet));
        }
    );
});

function showGradeSheet() {
    let grade_sheet_form_id = "grade_sheet_form";
    let edit_grade_sheet_button_id = "gradeSheetModal";
    $(`#${grade_sheet_form_id}`).submit();
    $(`#${edit_grade_sheet_button_id}`).modal('show');
}

