let popup= document.getElementById("popup");

function openpop(){
    popup.classList.add("open-popup");

}
function closepop(){
    popup.classList.remove("open-popup");

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
let allpage= document.getElementById("user-alllist");

function allpageopenpop(){
    allpage.classList.add("openuser-alllist");
    divpop.classList.remove("open-divpopup");


}

function divopenpop(){
    divpop.classList.add("open-divpopup");
    allpage.classList.remove("openuser-alllist");


}




