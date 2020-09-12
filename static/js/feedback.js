"use strict";

/*
    Feedback
*/

function postFeedback() {
    $.ajax({
        type: "POST",
        url: document.getElementById("feedback_post_url").value,
        dataType: "json",
        data: {
            feedback: getFeedback()
        },
        success: function (data) {
            document.getElementById("feedback_row").remove();
            // document.getElementById("feedback-thankYou-message").style.display = "block";
        },
    }).done(function (data) {
        console.log(data);
    });
}

function getFeedback() {
    if (document.getElementById("feedback_very_sad").checked) {
        return "Very Sad";
    } else if (document.getElementById("feedback_sad").checked) {
        return "Sad";
    } else if (document.getElementById("feedback_happy").checked) {
        return "Happy";
    } else if (document.getElementById("feedback_very_happy").checked) {
        return "Very Happy";
    } else if (document.getElementById("feedback_loved").checked) {
        return "Loved";
    } else {
        return "None";
    }
}