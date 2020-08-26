
eel.voiceThread()();

async function run(){

    let a = await eel.test_func()();
    var d = document.getElementById('text');
    d.innerHTML = a; 
}

eel.expose(changeText);
function changeText(newtext){
    var text = document.getElementById('text');
    text.innerHTML = newtext;
}