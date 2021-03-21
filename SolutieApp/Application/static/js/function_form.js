var popup = document.getElementById("popup");
var cards = document.getElementsByClassName("modal-content");
function ShowContent(index){
    for(var k = 0; k < cards.length; k++){
        cards[k].style.display = "none";
    }
    popup.style.display = "block";
    cards[index].style.display = "block";
}
var functions_btn = document.getElementsByClassName("btn_functions");
for(var i = 0; i < functions_btn.length; i++){
    functions_btn[i].addEventListener('click',ShowContent.bind(null,i));
}
window.onclick = function(event) {
    if (event.target === popup) {
        popup.style.display = "none";
    }
}