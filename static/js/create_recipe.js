//Declare global variables
let createIngredientsForm = document.querySelector(".create-ingredients");
let IngredientResults = document.querySelector("#check-all-ingredients");
let addIngredients = document.querySelector("#add-ingredients");
let recipeForm = document.querySelector("#recipe-form");
let checkIngredientsContainer =  document.querySelector(".check-ingredient-list");
let checkIngredients = checkIngredientsContainer.innerText.toLowerCase().split(", ");
//Buttons with event listeners
let searchButton = document.querySelector(".search-button");
let ingrFormButton = document.querySelector("#ingredient-form__button");
// variable for JS requirement
let jsAlert = document.querySelector(".js-alert");

checkIngredientsContainer.classList.add("hidden");

// Shows a text if JavaScript isn't active*/
jsAlert.classList.add("hidden");

// Check if all the ingredients are in the database */
searchButton.addEventListener("click", (event) => {
    event.preventDefault();

    //Declaring local variables
    let ingredientForm = document.querySelector("#ingredient-form");
    let searchIngredientForm = document.querySelector("#search-ingredient-form");
    let searchedIngredients = document.querySelector(".searching-ingredient")
        .value.toLowerCase().split(", ");
    let temporaryIngredients = [];
    let searchIngrError = document.querySelector("#search-ingredient__error")

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
            let ingredientClass = searchedIngredients[i].split(" ").join("-");
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
            let selectIngredient = document.querySelector("." + ingredientClass);

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

    let ingredientsToDatabase = document.querySelectorAll(".missing");

    if (ingredientsToDatabase.length > 0) {
        createIngredientsForm.classList.remove("hidden")
    } else if (ingredientsToDatabase.length <= 0 && searchedIngredients[0]) {
        //Preparing for creating a new recipe
        let ingredientsLabel = document.querySelector("#ingredients-label")
        let chooseIngredients = document.querySelector("#id_ingredients").children

        ingredientsLabel.innerText += `${searchedIngredients.join(", ")}`

        document.querySelector("#id_ingredients").classList.add("hidden")

        recipeForm.classList.remove("hidden")

        for( i = 0; i < chooseIngredients.length; i++) {
            let ingredientName = chooseIngredients[i].firstElementChild
                .innerText.split(", ")[1].substring(7).toLowerCase()

            if (searchedIngredients.includes(ingredientName)) {
                chooseIngredients[i].firstElementChild.firstElementChild.checked = true
            }
        }
    }

    if (ingredientsToDatabase.length > 0) {
        let currentIngredient = ingredientsToDatabase[0];

        let ingredientName = currentIngredient.innerText;
        let ingredientNameContainer = document.querySelector("#ingredient-name");

        ingredientNameContainer.innerText = ingredientName;

        let ingredientNameInput = document.querySelector("#id_name");

        ingredientNameInput.value = ingredientName;

        ingredientNameInput.classList.add("hidden")
    }

    for (i = 0; i < ingredientsToDatabase.length; i++) {
        addIngredients.innerHTML += `<br><label for="pic${i}">Name: ${ingredientsToDatabase[i].innerText}<br> ` + 
            `Picture: </label>` + 
            `\n<input type="file" name="pic${i}" accept="image/*" id="id_pic${i}"><br>`

        if (i === ingredientsToDatabase.length -1) {
            addIngredients.innerHTML += `<p>Copy this list before you press the button: ` + 
                ` ${searchedIngredients.join(", ")}</p>`
            addIngredients.innerHTML += `<br><button type="submit">Add ingredients to the database</button>`
            
        }
    }
})

let temporaryIngredientInput = [];

//This button adds all the Ingredients to "ingr_to_database.inputs"
ingrFormButton.addEventListener('click', (event) => {
    event.preventDefault();

    let ingredientsToDatabase = document.querySelectorAll(".missing");
    let currentIngredient = ingredientsToDatabase[0];
    let ingredientNameInput = document.querySelector("#id_name");
    let ingredientPriceInput= document.querySelector("#id_price");
    let ingredientUnitInput= document.querySelector("#id_ingredient_unit_type");
    let errorMessage = document.querySelector("#create-ingredient__error");

    if (ingredientsToDatabase.length > 0 && ingredientPriceInput.value !== "") {
        errorMessage.innerText = ""
        let currentIngredientInput = `${ingredientNameInput.value}, ` +
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
        let sendIngredients = document.querySelector("#id_inputs");
        sendIngredients.classList.add("hidden");
        addIngredients.classList.remove("hidden");
        sendIngredients.value = temporaryIngredientInput.join("//, ");
    }
})
