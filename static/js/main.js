
window.onload = () => { 'use strict';
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js',{scope:"/"})
            .then(function (registration) {
                console.log('ServiceWorker registration successful with scope: ', registration.scope);
            },
            function (err) {
                console.log('ServiceWorker registration failed: ', err); });
    } }

function display_form(table_size,table_num){
   $.ajax({
        type: 'GET',
        url: "http://localhost:5000/form",
        data: {
            table: table_num,
            size: table_size
        }, success: function (result){
            //console.log(result['Table'])
             $("#test").html("test "+result["Size"]+" "+result["Table"])
            }
        })

    console.log('tableValue: '+table_size+" n:"+table_num)
    let valueTable=document.getElementById("value_table")
    valueTable.innerText= "Tavolo N "+table_num+" "+table_size

    document.querySelector('.reserve-form-container').classList.toggle('active');
}

function remove(){
    document.querySelector('.reserve-form-container').classList.remove('active');
}

	function reserve() {
    $.ajax({
        url: "http://localhost:5000/formdate",
        type: "POST",
        data: {
            name: $("#name").val(),
            surname: $("#surname").val()
        },
        success: function( result ) {
            alert( "La tua prenotazione è stata effettuato con id " + result["post"] );
        }
    });
}