function myFunction() {
    let haburgerMenu = document.getElementById("myLinks");
    
    if (haburgerMenu.style.display === "flex") {
        haburgerMenu.style.display = "none";
    } else {
        haburgerMenu.style.display = "flex";
    }
}


let searchBar = document.querySelector(".search-bar")

function getSearchedElement() {
    let searchItems = document.getElementsByClassName("grid-item")

    if (searchBar.value === "") {
        for (i = 0; i < searchItems.length; i++) {
            searchItems[i].classList.remove("hidden");
        }     
    } else {
        for (i = 0; i < searchItems.length; i++) {
            let itemName = searchItems[i].querySelector(".grid-name")
            
            if (itemName.innerText.toLowerCase().includes(searchBar.value)) {
                searchItems[i].classList.remove("hidden");
            } else {
                searchItems[i].classList.add("hidden");
            }
        }
    }
}