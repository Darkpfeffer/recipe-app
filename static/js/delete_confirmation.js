let yesButton = document.getElementById("yes-button");
let noButton = document.getElementById("no-button");
let deleteCheckbox = document.getElementById("delete-checkbox");
let deleteForm = document.getElementById("delete-form");


yesButton.addEventListener('click', (event) => {
    event.preventDefault();

    deleteCheckbox.checked = true;

    deleteForm.submit();
})

noButton.addEventListener('click', (event) => {
    event.preventDefault();

    deleteCheckbox.checked = false;

    deleteForm.submit();
})