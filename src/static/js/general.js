function myFunction() {
    let haburgerMenu = document.getElementById("myLinks");
    
    if (haburgerMenu.style.display === "flex") {
        haburgerMenu.style.display = "none";
    } else {
        haburgerMenu.style.display = "flex";
    }
}