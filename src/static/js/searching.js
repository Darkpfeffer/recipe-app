IngredientResults = document.querySelector(".check-all-ingredients")

checkIngredientsContainer =  document.querySelector(".check-ingredient-list")

checkIngredients = checkIngredientsContainer.innerText.toLowerCase().split(", ")

checkIngredientsContainer.classList.add("hidden")

jsAlert = document.querySelector(".js-alert")

jsAlert.classList.add("hidden")

searchButton = document.querySelector(".search-button")

searchButton.addEventListener("click", (event) => {
    event.preventDefault()

    IngredientResults.innerHTML = ""

    searchedIngredients = document.querySelector(".searching-ingredient").value.toLowerCase().split(", ")

    for (let i = 0; i < searchedIngredients.length; i++) {
       IngredientResults.innerHTML += `<p>${searchedIngredients[i]}</p>`
       ingredientClass = searchedIngredients[i].split(" ").join("-")
       IngredientResults.lastElementChild.classList.add(ingredientClass)   
    }

    for (let i = 0; i < searchedIngredients.length; i++) {
        ingredientClass = searchedIngredients[i].split(" ").join("-")
        selectIngredient = document.querySelector("." + ingredientClass)
        if(checkIngredients.includes(searchedIngredients[i])) {
            selectIngredient.classList.add("existing")
        }
        else{
            selectIngredient.classList.add("missing")
        }
    }

    if (document.querySelectorAll(".missing").length > 0) {
        missingIngredient = document.querySelectorAll(".check-error")
        for (i = 0; i < missingIngredient.length; i++) {
            missingIngredient[i].classList.remove("hidden")
        }
    } else {
        missingIngredient = document.querySelectorAll(".check-error")
        for (i = 0; i < missingIngredient.length; i++) {
            missingIngredient[i].classList.add("hidden")
        }
    }
})