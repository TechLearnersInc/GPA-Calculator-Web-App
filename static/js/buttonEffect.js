"use strict";

/*
    Button Effect
*/

$(document).ready(function () {

    // Edit Grading System Button
    $(".load-button-gradesheet").on("click", function () {
        $(".loading-icon-gradesheet").removeClass("hide");
        $(".load-button-gradesheet").attr("disabled", true);

        $(".close-button").on("click", function () {
            $(".loading-icon-gradesheet").addClass("hide");
            $(".load-button-gradesheet").attr("disabled", false);
        });
    })

    // CalculateButton
    $(".load-button-calculate").on("click", function () {
        $(".loading-icon-calculate").removeClass("hide");
        $(".load-button-calculate").attr("disabled", true);

        $(".close-button").on("click", function () {
            $(".loading-icon-calculate").addClass("hide");
            $(".load-button-calculate").attr("disabled", false);
        });
    })
})