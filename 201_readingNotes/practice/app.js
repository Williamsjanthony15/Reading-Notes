'use strict'


let myForm = document.getElementById('conatiner -two');


function handleSubmit(event) {
  event.preventDefault();
 
  var firstName = event.target.firstname.value;
  console.log(firstName);
 
  var lastName = event.target.lastname.value;
  console.log(lastName);
 
  var pet = event.target.pets.value;
  console.log(pets);
}