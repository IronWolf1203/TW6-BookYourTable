
window.onload = () => { 'use strict';
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js',{scope:"/"})
            .then(function (registration) {
                console.log('ServiceWorker registration successful with scope: ', registration.scope);
            },
            function (err) {
                console.log('ServiceWorker registration failed: ', err); });
    } }




/*function display_form(table_size,table_num){
    console.log('tableValue: '+table_size+" n:"+table_num)
    let valueTable=document.getElementById("value_table")
    valueTable.innerText="Tavolo N "+table_num+" "+table_size

    //document.querySelector('.reserve-form-container').classList.toggle('active');
}

function remove(){
    document.querySelector('.reserve-form-container').classList.remove('active');
}

$( document ).ready(function() {

    });
    $(function() {
        $('prenota').click(function (){
            $.ajax({
                url: "/form",
                data: $('form').serialize(),
                type: "POST",
                success: function (response) {
                    console.log(response);
                },
                error: function (error) {
                    console.log(error);
                }
            });

        });

    });*/

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
