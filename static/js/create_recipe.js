createIngredientsForm = document.querySelector(".create-ingredients");
IngredientResults = document.querySelector("#check-all-ingredients");

checkIngredientsContainer =  document.querySelector(".check-ingredient-list");

checkIngredients = checkIngredientsContainer.innerText.toLowerCase().split(", ");

checkIngredientsContainer.classList.add("hidden");

// Shows a text if JavaScript isn't active*/
jsAlert = document.querySelector(".js-alert");

jsAlert.classList.add("hidden");

// Use the search button to check if all the ingredients are in the database */
searchButton = document.querySelector(".search-button");
ingredientForm = document.querySelector("#ingredient-form");
ingrFormButton = document.querySelector("#ingredient-form__button");
ingredientsToDatabase = document.querySelectorAll(".missing");

searchButton.addEventListener("click", (event) => {
    event.preventDefault();

    searchIngredientForm = document.querySelector("#search-ingredient-form")

    searchIngredientForm.classList.add("hidden")

    searchButton.classList.add("hidden")

    IngredientResults.innerHTML = "";

    searchedIngredients = document.querySelector(".searching-ingredient")
    .value.toLowerCase().split(", ");

    temporaryIngredients = [];

    for (let i = 0; i < searchedIngredients.length; i++) {
        if (!temporaryIngredients.includes(searchedIngredients[i])) {
            temporaryIngredients.push(searchedIngredients[i]);
        } 
    }

    searchedIngredients = temporaryIngredients;

    temporaryIngredients = [];

    for (let i = 0; i < searchedIngredients.length; i++) {
        if (searchedIngredients[0] !== "") { 
            IngredientResults.innerHTML += `<p>${searchedIngredients[i]}</p>`;
            ingredientClass = searchedIngredients[i].split(" ").join("-");
            IngredientResults.lastElementChild.classList.add(ingredientClass);
        } 
    }

    // Color the searched ingredients depending on their presence in the database
    for (let i = 0; i < searchedIngredients.length; i++) {
        if (searchedIngredients[0] !== "") {
            ingredientClass = searchedIngredients[i].split(" ").join("-");
            selectIngredient = document.querySelector("." + ingredientClass);
            if(checkIngredients.includes(searchedIngredients[i])) {
                selectIngredient.classList.add("existing");
            }
            else{
                selectIngredient.classList.add("missing");
            }
        }
    }

    /*
    If an ingredient is missing, show text and form to add ingredients to the 
    database
    */

    if (document.querySelectorAll(".missing").length > 0) {
        createIngredientsForm.classList.remove("hidden")
    } else {
        ingredientForm.classList.add("hidden");
        ingrFormButton.classList.add("hidden");
    }

    ingredientsToDatabase = document.querySelectorAll(".missing");

    if (document.querySelectorAll(".missing").length > 0) {
        currentIngredient = ingredientsToDatabase[0];

        ingredientName = currentIngredient.innerText;
        ingredientNameContainer = document.querySelector("#ingredient-name");

        ingredientNameContainer.innerText = ingredientName;

        ingredientNameInput = document.querySelector("#ingredient-name__input")
        .firstElementChild;

        ingredientNameInput.value = ingredientName;
    }
})

temporaryIngredientInput = [];

temporaryPictureInput = [];

//This button adds all the Ingredients to "ingr_to_database.inputs"
ingrFormButton.addEventListener('click', (event) => {
    event.preventDefault();

    ingredientsToDatabase = document.querySelectorAll(".missing");
    currentIngredient = ingredientsToDatabase[0];
    ingredientPriceInput= document.querySelector("#id_price");
    ingredientUnitInput= document.querySelector("#id_ingredient_unit_type");
    ingredientPictureInput = document.querySelector("#id_pic");
    errorMessage = document.querySelector("#create-ingredient__error");

    if (ingredientsToDatabase.length > 0 && ingredientPriceInput.value !== "") {
        errorMessage.innerText = ""
        currentIngredientInput = `${ingredientNameInput.value}, ` +
        `${ingredientPriceInput.value}, ` + 
        `${ingredientUnitInput.value}`

        temporaryIngredientInput.push(currentIngredientInput)
        temporaryPictureInput.push(ingredientPictureInput.value)

        currentIngredient.classList.add("existing");
        currentIngredient.classList.remove("missing");
    } else {
        errorMessage.innerText = "Price field needs to have value."
    }

    ingredientsToDatabase = document.querySelectorAll(".missing");
    currentIngredient = ingredientsToDatabase[0];

    if (ingredientsToDatabase.length > 0) {
        ingredientNameContainer.innerText = currentIngredient.innerText;
        ingredientNameInput.value = currentIngredient.innerText;
    }

    ingredientPriceInput.value = "";
    ingredientPictureInput.value = "";

    if (ingredientsToDatabase.length === 0) {
        createIngredientsForm.classList.add("hidden");
        addIngredients = document.querySelector("#add-ingredients");
        sendIngredients = document.querySelector("#id_inputs")

        sendIngredients.classList.add("hidden");
        addIngredients.classList.remove("hidden")
        for (i = 0; i < temporaryPictureInput.length; i++) {
            console.log(temporaryPictureInput[i])
        }
        sendIngredients.value = temporaryIngredientInput.join("//, ")
    }
})
