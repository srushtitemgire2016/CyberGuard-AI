document.addEventListener("DOMContentLoaded", function () {
    const questionInput = document.getElementById("question");
    const exampleButtons = document.querySelectorAll(".example-question");

    exampleButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            if (questionInput) {
                questionInput.value = button.dataset.question;
                questionInput.focus();
            }
        });
    });
});