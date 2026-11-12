let popup= document.getElementById("popup");
let prdedt= document.getElementById("prdt-list");
const overlay = document.getElementById("overlay");


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
function prdtopenpop(){
    popup.classList.remove("open-popup");
    prdedt.classList.add("prdt-list-opne-popup");
    overlay.style.display = "block";


}
function prdtopenpopclose(){
    prdedt.classList.remove("prdt-list-opne-popup");
    overlay.style.display = "none";


}




let dividnum= document.getElementById("dividnum_inpt");

let divedt= document.getElementById("divedt_btn");


function divnumopenpop(){
    dividnum.classList.add("open-dividnum");
    divedt.classList.add("opendivedt_btn");





}





