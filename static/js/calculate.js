"use strict";

/*
    Calculate
*/


$(document).ready(function () {
    // Variables
    let calculate_form_id = "calculate_gpa_form";
    let calculate_modal_id = "calculatesheet";
    let calculated_gpa_id = "calculated_gpa";
    let gpa_grade_sheet_input_box_id = "gpa_grade_sheet"

    $(`#${calculate_form_id}`).submit(function (event) {
        event.preventDefault();
        if ($(`#${gpa_grade_sheet_input_box_id}`).val().trim().length === 0) {
            showCheckAlert("Please, take a look at the Grade Sheet first");
            return;
        } else {
            let form = $(this);
            let formData = $(this).serializeArray()
            let preparedData = {};
            for (let i in formData) {
                let fieldName = String(formData[i].name);
                if (fieldName.match(/^Select\_Field\_\d+/g)) {
                    if (formData[i].value === "Select Grade") {
                        showCheckAlert("You've missed to select Grade. Plesae, take a look at the Grade Selection fields.");
                        return;
                    }
                }
                preparedData[fieldName] = formData[i].value.trim();
            }
            $.ajax({
                type: form.attr('method'),
                url: form.attr('action'),
                dataType: 'json',
                data: preparedData,
                success: function (data) {
                    $(`b[id='${calculated_gpa_id}']`).text(`GPA: ${data.GPA}`);
                    $(`#${calculate_modal_id}`).modal("show");
                }
            }).done(function (data) {
                console.log(data)
            });
        }
    });
});


// Grade Sheet Warning
function showCheckAlert(alertMessage) {
    let wrapper = $("#showCheckAlert");
    let alertTimeout = 5;
    let alertMessageID = "check_alert";
    let alert_html_code = `
        <div id="${alertMessageID}" class="alert alert-danger" role="alert">
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>${alertMessage}
        </div>
    `;

    // Adding Alert on Page
    $(wrapper).append(alert_html_code);

    // Auto removing alert
    window.setTimeout(function () {
        $(`#${alertMessageID}`).remove();
    }, alertTimeout * 1000);
};


function displayGradeTable() {
    let grade_sheet_calculator_modal_id = "grade_sheet_calculator_modal";
    let table = document.getElementById(grade_sheet_calculator_modal_id);
    switch (table.style.display) {
        case "none":
            table.style.display = "block";
            break;
        default:
            table.style.display = "none";
            break;
    }
}