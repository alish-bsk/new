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

let allpage= document.getElementById("user-alllist");
let expage= document.getElementById("user-exdtlist");
let sldpage= document.getElementById("user-sldlist");


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


function allpageopenpop(){
    allpage.classList.add("openuser-alllist");
    divpop.classList.remove("open-divpopup");
    sldpage.classList.remove("openuser-sldlist");
    expage.classList.remove("openuser-exdtlist");


}

function divopenpop(){
    divpop.classList.add("open-divpopup");
    allpage.classList.remove("openuser-alllist");
    sldpage.classList.remove("openuser-sldlist");
    expage.classList.remove("openuser-exdtlist");




}
//for sold button only

function sldpageopenpop(){
    sldpage.classList.add("openuser-sldlist");
    divpop.classList.remove("open-divpopup");
    expage.classList.remove("openuser-exdtlist");
    allpage.classList.remove("openuser-alllist");


}

function sldopenpop(){
    divpop.classList.add("open-divpopup");
    sldpage.classList.remove("openuser-sldlist");
}


//for epiredate button only

function expageopenpop(){
    expage.classList.add("openuser-exdtlist");
    divpop.classList.remove("open-divpopup");
    allpage.classList.remove("openuser-alllist");
    sldpage.classList.remove("openuser-sldlist");





}

function exopenpop(){
    divpop.classList.add("open-divpopup");
    expage.classList.remove("openuser-exdtlist");
}