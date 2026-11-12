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
let divpop= document.getElementById("divpopup");


let dividnum= document.getElementById("dividnum_inpt");

let divedt= document.getElementById("divedt_btn");


function divnumopenpop(){
    dividnum.classList.add("open-dividnum");
    divedt.classList.add("opendivedt_btn");


}
function divclosepop(){
    divpop.classList.remove("open-divpopup");
    dividnum.classList.remove("open-dividnum");
    divedt.classList.remove("opendivedt_btn");

    

}
//for all button only
let allpage= document.getElementById("user-alllist");

function allpageopenpop(){
    allpage.classList.add("openuser-alllist");
    divpop.classList.remove("open-divpopup");


}

function divopenpop(){
    divpop.classList.add("open-divpopup");
    allpage.classList.remove("openuser-alllist");


}
//for sold button only
let sldpage= document.getElementById("user-sldlist");

function sldpageopenpop(){
    sldpage.classList.add("openuser-alllist");
    divpop.classList.remove("open-divpopup");


}

function sldopenpop(){
    divpop.classList.add("open-divpopup");
    sldpage.classList.remove("openuser-alllist");
}


//for epiredate button only
let expage= document.getElementById("user-exdtlist");

function expageopenpop(){
    expage.classList.add("openuser-alllist");
    divpop.classList.remove("open-divpopup");



}

function exopenpop(){
    divpop.classList.add("open-divpopup");
    expage.classList.remove("openuser-alllist");
}