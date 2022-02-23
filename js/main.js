window.onload = () => { 'use strict';
    if ('serviceWorker' in navigator) { navigator.serviceWorker
        .register('./sw.js').then(function (registration) {
                console.log('ServiceWorker registration successful with scope: ', registration.scope);
            },
            function (err) {
                console.log('ServiceWorker registration failed: ', err); });
    } }





function display_form(){
    document.querySelector('.reserve-form-container').classList.toggle('active');
}

function remove(){
    document.querySelector('.reserve-form-container').classList.remove('active');
}

/*
document.querySelector('#form-btn1').onclick = () =>{
    document.querySelector('.reserve-form-container').classList.toggle('active');
}
document.querySelector('#form-btn2').onclick = () =>{
    document.querySelector('.reserve-form-container').classList.toggle('active');
}
document.querySelector('#form-btn3').onclick = () =>{
    document.querySelector('.reserve-form-container').classList.toggle('active');
}
document.querySelector('#form-btn4').onclick = () =>{
    document.querySelector('.reserve-form-container').classList.toggle('active');
}
document.querySelector('#form-btn5').onclick = () =>{
    document.querySelector('.reserve-form-container').classList.toggle('active');
}
document.querySelector('#form-btn6').onclick = () =>{
    document.querySelector('.reserve-form-container').classList.toggle('active');
}

document.querySelector('#close-reserve-form').onclick = () =>{
    document.querySelector('.reserve-form-container').classList.remove('active');
}

 */
