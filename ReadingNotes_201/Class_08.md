# Reading 6

## Javascript

### Chapter 3 "Object Literals"

<ul>
  <li> What is an "object"?<li>
    <li>Objects group together a set of variables and functions to creat a model of something you would recognize from the real world. in an Object, variables and functions take on new names.</li>
    <ul>
      <li>Variables Become known as properties.</li>
      <li>Functions become known as methods.</li>
      <li>Literal Notation is the easiest and nost popular way to create objects. </li>
      <li> var hotel = {
        name: 'Quay',
        rooms: 40,
        booked: 25,
        CheckAvailability: function() {
          return this.rooms - this.booked;
        }
      };</li>
      <li>Accessing an object and dot notation</li>
      <li>You access the properties or methods of an object using dot notation. You can also access properties using square brackets.</li>
      <li>var hotelName = hotel.name;
          var roomsFree = hotel.checkAvailability();
          //////////
          var hotelName = hotel['name'];
          var roomsFree = hotel['checkAvailability']();</li>
      <li> The name of the property or method contains special characters (such as a dash)</li>
      <li>The name of the property is a number(technically allowed, but should generally be avoided)</li>
      <li>A variable is being used in a place of the property name (you will see this technique used in Chapter 12)</li>
    </ul>
      <li>
        var hotel = {
        name: 'quay',
        rooms: 40,
        booked: 25;
        checkAvailablity: function() {
          return this.room - this.booked;
        }
      };
//
      var elName = document.getElementById('hotelName');
      elName.textContent = hotel.name;
//
      var elRooms = document.getElementById('rooms');
      elRooms.textContect = hotel.checkAvailability();
      //////////////
            var hotel = {
        name: 'park',
        rooms: 120,
        booked: 77;
        checkAvailablity: function() {
          return this.room - this.booked;
        }
      };
//
      var elName = document.getElementById('hotelName');
      elName.textContent = hotel.checkAvailability();
//
      var elRooms = document.getElementById('rooms');
      elRooms.textContect = hotel.checkAvailability();
    </li>
  </li>
</ul>

### Chapter 5 "Document Object Model"

#### Body of an HTML Page.

Document
HTML
BODY
DIV - ATTRIBUTE
