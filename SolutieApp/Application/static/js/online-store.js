function addFunction(iter, numFunc) {
    document.getElementById(iter).style.display = "inline-block";
    var input = document.getElementsByName("functions")[0];
    input.value += numFunc;
    input.value += "_";
}

function removeFunction(iter, numFunc) {
    document.getElementById(iter).style.display = "none";
    var input = document.getElementsByName("functions")[0];
    numFunc += "_";
    console.log(numFunc)
    input.value = input.value.replace(numFunc,"");
}