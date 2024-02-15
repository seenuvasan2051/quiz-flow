function userValidation() {
    var admincontact = document.getElementById("contact").value;
    var adminpassword = document.getElementById("password").value;

    if (!admincontact.trim()) {
        alert("Please enter a contact number");
        return false;
    }

    if (!/^\d{10}$/.test(admincontact)) {
        alert("Please enter a valid 10-digit phone number");
        return false;
    }

    if (!adminpassword.trim()) {
        alert("Please enter a password");
        return false;
    }

    return true;
}