//Declare global variables
let createIngredientsForm = document.querySelector(".create-ingredients");
let IngredientResults = document.querySelector("#check-all-ingredients");
let addIngredientsForm = document.getElementById("add-ingredient__form");
let recipeForm = document.querySelector("#recipe-form");
let sendIngredients = document.querySelector("#id_name_inputs");
let checkIngredientsContainer =  document.querySelector(".check-ingredient-list");
let checkIngredients = checkIngredientsContainer.innerText.toLowerCase().split(", ");

let createRecipeForm = document.getElementById("create-recipe__form");
let createRecipeButton = document.querySelector("#create-recipe__button");

console.log(checkIngredients)
//Buttons with event listeners
let searchButton = document.querySelector(".search-button");
// variable for JS requirement
let jsAlert = document.querySelector(".js-alert");

checkIngredientsContainer.classList.add("hidden");
sendIngredients.classList.add("hidden")

// Shows a text if JavaScript isn't active*/
jsAlert.classList.add("hidden");

// Check if all the ingredients are in the database */
searchButton.addEventListener("click", (event) => {
    event.preventDefault();

    //Declaring local variables
    let searchIngredientForm = document.querySelector(
        "#search-ingredient-form"
    );
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
                if(sendIngredients.value === "") {
                    sendIngredients.value += searchedIngredients[i]

                } else {
                    sendIngredients.value += ", " + searchedIngredients[i]
                }
            }
            else {
                selectIngredient.classList.add("missing");
                if(sendIngredients.value === "") {
                    sendIngredients.value += searchedIngredients[i]

                } else {
                    sendIngredients.value += ", " + searchedIngredients[i]
                }
                addIngredientsForm.innerHTML += `
                <div class="hidden ingr-to__database">
                    <label for="ingredient_name${i}">
                        Ingredient name: ${searchedIngredients[i]}
                    </label>
                    <input 
                        name="ingredient_name${i}" id="ingredient_name${i}" ` +
                        `maxlength="120" value="${searchedIngredients[i]}"` + 
                        `class="hidden" required
                    ><br>
                    <label for="ingredient_price${i}">
                        Price: 
                    </label>
                    <input 
                        name="ingredient_price${i}" id="ingredient_price${i}" ` +  
                        `type="number" class="price-tag"
                    ><span>$/</span>
                    <select 
                        name="ingredient_unit_type${i}" ` + 
                        `id="ingredient_unit_type${i}" 
                    >
                        <option value="liter">Liter</option>
                        <option value="kilogram">Kilogram</option>
                    </select><br>
                </div>
                `
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

        recipeForm.classList.remove("hidden");
        createRecipeForm.classList.remove("hidden");
    }

    if (ingredientsToDatabase.length > 0) {
        let currentForm = document.getElementsByClassName("ingr-to__database");
        
        recipeForm.classList.remove("hidden");
        currentForm[0].classList.remove("hidden");

        createRecipeForm.classList.add("hidden");    
        
        createRecipeButton.innerText = "Add ingredient";
    }
})

//This button adds all the Ingredients to "ingr_to_database.inputs"
createRecipeButton.addEventListener('click', (event) => {
    event.preventDefault();

    let ingredientsToDatabase = document.querySelectorAll(".missing");
    let currentForm = document.getElementsByClassName("ingr-to__database");
    let currentIngredient = ingredientsToDatabase[0];
    let currentPriceTag;
    let errorMessage = document.querySelector("#create-ingredient__error");

    if (currentForm[0]) {
        currentPriceTag = currentForm[0].querySelector(".price-tag");
    }

    if (ingredientsToDatabase.length > 0 && currentPriceTag.value !== "") {
        errorMessage.innerText = ""

        currentIngredient.classList.add("existing");
        currentIngredient.classList.remove("missing");

        currentForm[0].classList.add("hidden");
        currentForm[0].classList.remove("ingr-to__database");

        currentForm = document.getElementsByClassName("ingr-to__database");
        if (currentForm[0]) {
            currentForm[0].classList.remove("hidden");
        }
    } else {
        errorMessage.innerText = "Price field needs to have value.";
    }

    ingredientsToDatabase = document.querySelectorAll(".missing");
    currentIngredient = ingredientsToDatabase[0];

    if (ingredientsToDatabase.length === 0) {
        createIngredientsForm.classList.add("hidden");
        createRecipeForm.classList.remove("hidden");

        let ingredientError = document.getElementById("ingredient-error");
        ingredientError.classList.add("hidden");

        let recipeName = document.getElementById("id_name");
        let recipeCookingTime = document.getElementById("id_cooking_time");
        let recipeNameError = document.getElementById("recipe-name__error");
        let recipeCookingTimeError = document.getElementById(
            "recipe-cooking-time__error");

        if (recipeName.value === "" ) {
            recipeNameError.innerText = "Recipe name must be added.";
        } else {
            recipeNameError.innerText = "";
        }

        if (recipeCookingTime.value === "" ) {
            recipeCookingTimeError.innerText = "Cooking time must be added.";
        } else {
            recipeCookingTimeError.innerText = "";
        }

        
        if (createRecipeButton.innerText !== "Create recipe"){
            createRecipeButton.innerText = "Create recipe";
        }

        if (recipeCookingTimeError.innerText === "" && 
            recipeNameError.innerText === "") {
            recipeForm.submit();
        }
    }
})
