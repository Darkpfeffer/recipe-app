let checkIngredientsForm = document.querySelector("#check-ingredients-form");

let usedIngredientsContainer = document.querySelector("#used-ingredients");
let usedIngredients = usedIngredientsContainer.innerText.split(", ");

let addIngredientsForm = document.querySelector("#add-ingredients__form"); 
let addIngredients = document.querySelector("#add-ingredients");
let createIngredients = document.querySelector("#create-ingredients");
let addedForms = document.querySelector("#added-forms");

let ingrToDatabase = document.getElementsByClassName("ingr-to__database");

let ingredientListContainer = document.querySelector("#ingredient-list");
let ingredientList = ingredientListContainer.innerText
    .toLowerCase().split(", ");

let addIngredientsToRecipe = document.querySelector("#add-ingredients__to--recipe");
let removeIngredientsFromRecipe = document.querySelector("#remove-ingredients__from--recipe");

let addIngredientsMethod = document.querySelector("#ingredients-to__recipe");
let removeIngredientsMethod = document.querySelector("#ingredients-from__recipe");

ingredientListContainer.classList.add("hidden");
addIngredientsForm.classList.add("hidden");

addIngredientsMethod.classList.add("hidden");
removeIngredientsMethod.classList.add("hidden");

console.log(ingredientList)

addIngredientsToRecipe.addEventListener('click', (event) => {
    event.preventDefault()

    addIngredientsMethod.classList.remove('hidden');
    removeIngredientsMethod.classList.add('hidden');
})

removeIngredientsFromRecipe.addEventListener('click', (event) => {
    event.preventDefault()

    removeIngredientsMethod.classList.remove('hidden');
    addIngredientsMethod.classList.add('hidden');
})

checkIngredientsForm.addEventListener('submit', (event) => {
    event.preventDefault();

    let checkIngredients = document.querySelector("#check-ingredients")
    .value.toLowerCase().split(", ");

    if (checkIngredients[0].length === 0) {
        console.warn("Input can't be empty");
    } else {
        
        for(i = 0; i < checkIngredients.length; i++) {
            if(
                ingredientList.includes(checkIngredients[i]) && 
                usedIngredients.includes(checkIngredients[i])
            ) {
                console.log("Ingredient is already included.")

            } else if (ingredientList.includes(checkIngredients[i])){
                if (addIngredients.value.length === 0) {
                    addIngredients.value = checkIngredients[i];

                } else {
                    addIngredients.value += ", " + checkIngredients[i];

                }

            } else {
                if (createIngredients.value.length === 0) {
                    createIngredients.value = checkIngredients[i];

                } else {
                    createIngredients.value += ", " + checkIngredients[i];

                }
            }
        }

        if(createIngredients.value.length > 0) {
            for(i = 0; i < createIngredients.value.split(", ").length; i++) {

                addedForms.innerHTML += `
                        <div class="hidden ingr-to__database">
                            <label for="ingredient_name${i}">
                                Ingredient name: ${checkIngredients[i]}
                            </label>
                            <input 
                                name="ingredient_name${i}" id="ingredient_name${i}" ` +
                                `maxlength="120" value="${checkIngredients[i]}"` + 
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
                            <label for="ingredient_pic${i}">Picture: </label>
                            <input 
                                type="file" name="ingredient_pic${i}" ` +  
                                `accept="image/*" id="ingredient_pic${i}"
                            ><br>
                        </div>
                    `;
            };
        };
        console.log("addIngredients: " + addIngredients.value)
        console.log("createIngredients: " + createIngredients.value)
    };

    checkIngredientsForm.classList.add("hidden");
    addIngredientsForm.classList.remove("hidden");

    let addIngredientsButton = document.querySelector(
        "#add-ingredients__button"
    );

    if(ingrToDatabase.length > 0) {
        ingrToDatabase[0].classList.remove("hidden");
    };

    addIngredientsButton.classList.remove("hidden");

    if (!createIngredients[0]) {
        addIngredientsButton.innerText = "Submit changes";
    };

    addIngredients.classList.add('hidden');
    createIngredients.classList.add('hidden');

    addIngredientsForm.addEventListener('submit', (e) => {
        e.preventDefault()

        let currentIngredientForm = document.querySelector(
            ".ingr-to__database"
        );

        if (currentIngredientForm) {

            console.log(currentIngredientForm)
            
            let currentPriceTag = currentIngredientForm.querySelector(".price-tag")
            .value;

                if (currentPriceTag.length === 0) {
                    console.warn("Price can't be empty.");

                } else {
                    currentIngredientForm.classList.add("hidden");
                    currentIngredientForm.classList.remove("ingr-to__database");

                    currentIngredientForm = document.querySelector(
                        ".ingr-to__database"
                    );

                    if (!currentIngredientForm) {
                        priceTags = document.getElementsByClassName("price-tag")
                        for(i = 0; i < priceTags.length; i++) {
                            console.log(`Price tag ${i}: ` + priceTags[i].value)
                        }
    
                        addIngredientsButton.innerText = "Submit changes"
                    } else {
                        currentIngredientForm.classList.remove("hidden");
                    }
                }

        } else {
            addIngredientsForm.submit();
        }
    })
})

let removeIngredients = document.getElementById('remove-ingredients')
let ingredientCheckbox = document.querySelector("#ingredient-checkbox");

let checkboxButton = document.querySelector("#checkbox-button");

checkboxButton.addEventListener('click', (event) => {
    event.preventDefault()

    let removeInput = document.getElementById("remove-input")

    let checkboxIngredients = ""

    for (i = 0; i < ingredientCheckbox.childElementCount; i++) {
        let input = ingredientCheckbox.children[i].querySelector(".checkbox-input").checked;
        let ingredientName = ingredientCheckbox.children[i]
            .querySelector(".checkbox-label").innerText;

        if (!checkboxIngredients) {
            checkboxIngredients = ingredientName
        } else {
            checkboxIngredients += ", " + ingredientName
        }
        
        if (input) {
            if (!removeInput.value) {
                removeInput.value = ingredientName
            } else {
                removeInput.value += ', ' + ingredientName
            }
        }

        if (removeInput.value === checkboxIngredients) {
            console.warn("You can't delete all ingredients.")
        } else if (!removeInput.value) {
            console.warn("You have to select one or more ingredients.")
        } else {
            removeIngredients.submit()
        }
    }
})
