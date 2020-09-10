"use strict";

/*
    Dynamic Form
*/

let rowNo = 1;
let count = 1;
let input_field_wrap_class_name = "input_field_wrap";

$(document).ready(function () {

    // Variables
    let wrapper = $(`.${input_field_wrap_class_name}`);
    let add_button = $(".add_field_button");
    // let count = 1;
    let max_fields = 10;
    let fieldLimitAlertID = "feildLimitAlert";

    // Add New Field
    $(add_button).click(function (e) {
        e.preventDefault();
        if (count < max_fields) {
            rowNo += 1;
            count += 1;
            let input_field_name = `Input_Field_${rowNo}`;
            let select_field_name = `Select_Field_${rowNo}`;
            let new_gpa_row_htmlCode = `
                <div class="form-group form-row" id="row${rowNo}">
                    <div class="col-5 col-sm-5">
                        <select class="form-control" name="${select_field_name}" required>
                            <option>Grade</option>
                            <option>A+</option>
                            <option>A</option>
                            <option>A-</option>
                            <option>B+</option>
                            <option>B</option>
                            <option>B-</option>
                            <option>C+</option>
                            <option>C</option>
                            <option>C-</option>
                            <option>D+</option>
                            <option>D</option>
                            <option>D-</option>
                            <option>F</option>
                        </select>
                    </div>
                    <div class="col-4 col-sm-4">
                        <input
                            type="text"
                            class="form-control"
                            name="${input_field_name}"
                            id="${input_field_name}"
                            placeholder="Credit Hours, Ex:3.5"
                            required
                        />
                        <script type="text/javascript">
                            $("input[name='${input_field_name}']").on(
                                'input blur paste',
                                function() {
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
                        </script>
                    </div>
                    <div class="col-3 col-sm-3">
                        <a href="#" class="btn btn-danger btn-block remove_field" id="${rowNo}">
                            <i class="far fa-trash-alt"></i>
                            <span class="d-none d-sm-none d-md-none d-lg-inline">DELETE</span>
                        </a>
                    </div>
                </div>
            `;

            // Adding New GPA Field
            $(wrapper).append(new_gpa_row_htmlCode);
        }
        else if (document.getElementById(fieldLimitAlertID)) { // If already alert is showing
            /* empty */;
        }
        else { // If Limit Reached
            let limitAlertMessage = "Limit 10 is reached";
            let limitAlertTimeout = 3;
            let limit_alert_html_code = `
                <div id="feildLimitAlert" class="alert alert-danger" role="alert">
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                    <strong>${limitAlertMessage}</strong>
                </div>
            `;

            // Adding Alert on Page
            $(wrapper).append(limit_alert_html_code);

            // Auto removing alert
            window.setTimeout(function () {
                $(`#${fieldLimitAlertID}`).remove();
            }, limitAlertTimeout * 1000);
        }
    });

    // Delete
    $(document).on("click", ".remove_field", function (e) {
        e.preventDefault();
        if (document.getElementById("feildLimitAlert")) {
            $(`#${fieldLimitAlertID}`).remove();
        }
        let buttonID = $(this).attr("id");
        $(`#row${buttonID}`).remove();
        count -= 1;
    });
});


// Clear Fields Button
function clearFields() {
    let rowListObject = document.getElementsByClassName(input_field_wrap_class_name)[0].children;

    let rowList = [];
    for (let key of Object.keys(rowListObject)) {
        rowList.push(rowListObject[key].id);
    }

    rowList.forEach(function (row) {
        if (row !== 'row1') {
            document.getElementById(row).remove();
        }
    });

    rowNo = 1;
    count = 1;
}