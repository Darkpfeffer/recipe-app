//Declare global variables
createIngredientsForm = document.querySelector(".create-ingredients");
IngredientResults = document.querySelector("#check-all-ingredients");
addIngredients = document.querySelector("#add-ingredients");
recipeForm = document.querySelector("#recipe-form");
checkIngredientsContainer =  document.querySelector(".check-ingredient-list");
checkIngredients = checkIngredientsContainer.innerText.toLowerCase().split(", ");
//Buttons with event listeners
searchButton = document.querySelector(".search-button");
ingrFormButton = document.querySelector("#ingredient-form__button");
// variable for JS requirement
jsAlert = document.querySelector(".js-alert");

checkIngredientsContainer.classList.add("hidden");

// Shows a text if JavaScript isn't active*/
jsAlert.classList.add("hidden");

// Check if all the ingredients are in the database */
searchButton.addEventListener("click", (event) => {
    event.preventDefault();

    //Declaring local variables
    ingredientForm = document.querySelector("#ingredient-form");
    searchIngredientForm = document.querySelector("#search-ingredient-form");
    searchedIngredients = document.querySelector(".searching-ingredient")
        .value.toLowerCase().split(", ");
    temporaryIngredients = [];
    searchIngrError = document.querySelector("#search-ingredient__error")

    IngredientResults.innerHTML = "";

    for (let i = 0; i < searchedIngredients.length; i++) {
        if (!temporaryIngredients.includes(searchedIngredients[i])) {
            temporaryIngredients.push(searchedIngredients[i]);
        } 
    }

    searchedIngredients = temporaryIngredients;
    temporaryIngredients = [];

    if (searchedIngredients[0]) {
        searchIngredientForm.classList.add("hidden")
    } else {
        searchIngrError.innerText = "Ingredient form can't be empty."
    }

    for (let i = 0; i < searchedIngredients.length; i++) {
        if (searchedIngredients[0] !== "") { 
            IngredientResults.innerHTML += `<p>${searchedIngredients[i]}</p>`;
            ingredientClass = searchedIngredients[i].split(" ").join("-");
            IngredientResults.lastElementChild.classList.add(ingredientClass);
        } 
    }

    // Checking searched ingredients presence in the database
    for (let i = 0; i < searchedIngredients.length; i++) {
        if (searchedIngredients[0] !== "") {
            if (searchIngrError !== "") {
                searchIngrError.innerText = ""
            }

            ingredientClass = searchedIngredients[i].split(" ").join("-");
            selectIngredient = document.querySelector("." + ingredientClass);

            if (checkIngredients.includes(searchedIngredients[i])) {
                selectIngredient.classList.add("existing");
            }
            else {
                selectIngredient.classList.add("missing");
            }

        }
    }

    /*
    If an ingredient is missing, show text and form to add ingredients to the 
    database
    */

    ingredientsToDatabase = document.querySelectorAll(".missing");
    existingIngredients = document.querySelector(".existing")

    if (ingredientsToDatabase.length > 0) {
        createIngredientsForm.classList.remove("hidden")
    } else if (ingredientsToDatabase.length <= 0 && searchedIngredients[0]) {
        recipeForm.classList.remove("hidden")
    }

    if (ingredientsToDatabase.length > 0) {
        currentIngredient = ingredientsToDatabase[0];

        ingredientName = currentIngredient.innerText;
        ingredientNameContainer = document.querySelector("#ingredient-name");

        ingredientNameContainer.innerText = ingredientName;

        ingredientNameInput = document.querySelector("#id_name");

        ingredientNameInput.value = ingredientName;

        ingredientNameInput.classList.add("hidden")
    }

    for (i = 0; i < ingredientsToDatabase.length; i++) {
        addIngredients.innerHTML += `<br><label for="pic${i}">Name: ${ingredientsToDatabase[i].innerText}<br> ` + 
            `Picture: </label>` + 
            `\n<input type="file" name="pic${i}" accept="image/*" id="id_pic${i}"><br>`

        if (i === ingredientsToDatabase.length -1) {
            console.log(searchedIngredients)
            addIngredients.innerHTML += `<p>Copy this list before you press the button: ` + 
                ` ${searchedIngredients.join(", ")}</p>`
            addIngredients.innerHTML += `<br><button type="submit">Add ingredients to the database</button>`
            
        }
    }
})

temporaryIngredientInput = [];

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

    if (ingredientsToDatabase.length === 0) {
        createIngredientsForm.classList.add("hidden");
        sendIngredients = document.querySelector("#id_inputs");
        console.log(sendIngredients)
        sendIngredients.classList.add("hidden");
        addIngredients.classList.remove("hidden");
        sendIngredients.value = temporaryIngredientInput.join("//, ");
    }
})
