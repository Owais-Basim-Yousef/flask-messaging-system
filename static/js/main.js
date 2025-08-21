document.addEventListener("DOMContentLoaded", function () {
    const emailInput = document.getElementById("email");
    const phoneInput = document.getElementById("phone");
    const emailIcon = document.getElementById("emailIcon");
    const phoneIcon = document.getElementById("phoneIcon");

    //email validation
    emailInput.addEventListener("input", function () {
        const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
        if (emailInput.value.trim() === "") {
            emailIcon.style.display = "none";
        } else if (emailPattern.test(emailInput.value)) {
            emailIcon.src = "/static/icons/yes.png";
            emailIcon.style.display = "inline";
        } else {
            emailIcon.src = "/static/icons/no.png";
            emailIcon.style.display = "inline";
        }
    });

    //phone validation
    phoneInput.addEventListener("input", function () {
        const phonePattern = /^[0-9]{6,15}$/;
        if (phoneInput.value.trim() === "") {
            phoneIcon.style.display = "none";
        } else if (phonePattern.test(phoneInput.value)) {
            phoneIcon.src = "/static/icons/yes.png";
            phoneIcon.style.display = "inline";
        } else {
            phoneIcon.src = "/static/icons/no.png";
            phoneIcon.style.display = "inline";
        }
    });
});
