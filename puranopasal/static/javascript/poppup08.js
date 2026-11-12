let popup= document.getElementById("popup");


function openpop(){
    popup.classList.add("open-popup");
    overlay.style.display = "block";
    popup.style.display = "block";



}
function closepop(){
    popup.classList.remove("open-popup");
    overlay.style.display = "none";
    popup.style.display = "none";
}