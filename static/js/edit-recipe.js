
let checkButton = document.querySelector("#check-button");
let checkIngredientsForm = document.querySelector("#check-ingredients-form");
let ingrToDatabase = document.getElementsByClassName("ingr-to__database");
let addIngredientsForm = document.querySelector("#add-ingredients__form"); 
let addIngredients = document.querySelector("#add-ingredients");
let addedForms = document.querySelector("#added-forms");
let ingrFormButton = addIngredientsForm.lastElementChild
.querySelectorAll(".ingredient-form__button");
let ingredientListContainer = document.querySelector("#ingredient-list");
let ingredientList = ingredientListContainer.innerText
    .toLowerCase().split(", ");

ingredientListContainer.classList.add("hidden");

checkButton.addEventListener('click', (event) => {
    event.preventDefault();

    let checkIngredients = document.querySelector("#check-ingredients")
    .value.toLowerCase().split(", ");



    if (checkIngredients[0].length === 0) {
        console.warn("Input can't be empty");
    } else {
        
        for(i = 0; i < checkIngredients.length; i++) {
            if (ingredientList.includes(checkIngredients[i])){
                if (addIngredients.value.length === 0) {
                    addIngredients.value = checkIngredients[i];
                } else {
                    addIngredients.value += ", " + checkIngredients[i];
                }
            } else {
                if (addIngredients.value.length === 0) {
                    addIngredients.value = checkIngredients[i];
                } else {
                    addIngredients.value += ", " + checkIngredients[i];
                }
                addedForms.innerHTML += `
                    <div class="hidden ingr-to__database">
                        <label for="name${i}">
                            Ingredient name: ${checkIngredients[i]}
                        </label>
                        <input 
                            name="name${i}" id="name${i}" ` +
                            `maxlength="120" value="${checkIngredients[i]}"` + 
                            `class="hidden" required
                        ><br>
                        <label for="price${i}">
                            Price: 
                        </label>
                        <input 
                            name="price${i}" id="price${i}" ` +  
                            `type="number" class="price-tag"
                        ><span>$/</span>
                        <select 
                            name="ingredient_unit_type${i}" ` + 
                            `id="ingredient_unit_type${i}" 
                        >
                            <option value="liter">Liter</option>
                            <option value="kilogram">Kilogram</option>
                        </select><br>
                        <label for="id_pic${i}">Picture: </label>
                        <input 
                            type="file" name="pic${i}" ` +  
                            `accept="image/*" id="id_pic${i}"
                        ><br>
                    </div>
                `;
            }

            console.log(addIngredients.value)
        }
    }

    checkIngredientsForm.classList.add("hidden");

    let addIngredientsButton = document.querySelector(
        "#add-ingredients__button"
    );

    if(ingrToDatabase.length > 0) {
        ingrToDatabase[0].classList.remove("hidden");
        addIngredientsButton.classList.remove("hidden");
    }

    addIngredientsButton.addEventListener('click', (e) => {
        e.preventDefault()

        let currentIngredientForm = document.querySelector(
            ".ingr-to__database"
        );

        if (currentIngredientForm) {
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
                        console.log(priceTags[i].value)
                    }
                } else {
                    currentIngredientForm.classList.remove("hidden");
                }
            }
        } else {
            //addIngredientsForm.submit();
        }
    })
})