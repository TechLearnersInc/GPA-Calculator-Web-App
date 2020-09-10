"use strict";

/*
    Button Effect
*/

$(document).ready(function () {
    $(".load-button").on("click", function () {
        $(".loading-icon").removeClass("hide");
        $(".load-button").attr("disabled", true);

        $(".close-button").on("click", function () {
            $(".loading-icon").addClass("hide");
            $(".load-button").attr("disabled", false);
        });
    })
})