console.log('Dragdrop');

// function allowDrop(ev) {
//     ev.preventDefault();
// }

// function drag(ev) {
//     ev.dataTransfer.setData("text", ev.target.id);
//     //console.log(ev.dataTransfer.getData("text"));
//     ev.target.parentElement.id += "source";
// }

// function drop(ev) {
//     ev.preventDefault();
//     var source = document.getElementById("source");
//     console.log(ev.target.childNodes);
//     source.appendChild(ev.target.childNodes[0]);
//     source.id = '';
//     var data = ev.dataTransfer.getData("text");
//     console.log(data);
//     ev.target.appendChild(document.getElementById(data));
//   }

let dragged;
let id;
let index;
let indexDrop;
let list;

document.addEventListener("dragstart", ({target}) => {
    console.log("Drag");
    dragged = target;
    id = target.id;
    list = target.parentNode.children;
    for(let i = 0; i < list.length; i += 1) {
        if(list[i] === dragged){
            index = i;
        }
    }
});

document.addEventListener("dragover", (event) => {
    event.preventDefault();
});

document.addEventListener("drop", ({target}) => {
    if(target.className == "dropzone card" && target.id !== id) {
        dragged.remove( dragged );
        for(let i = 0; i < list.length; i += 1) {
            if(list[i] === target){
                indexDrop = i;
            }
        }
        console.log(index, indexDrop);
        if(index > indexDrop) {
            target.before( dragged );
        } else {
            target.after( dragged );
        }
    }
});