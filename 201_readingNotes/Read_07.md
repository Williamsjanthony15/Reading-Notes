# Read 7

## Chapter 6: “Tables” (pp.126-145)
 ### What is a table?
  <p> A table represents information in a grid format. Examples of tables include financial reports, TV schedules, and sports results. </p>

<ul>
  <li>Each black in the grid is reffered to as a table cell. in HTML a table is written out row by row.</li>
  <li>< table > element is used to create a table/ the contents of the table are written out row by row.</li>
  <li>< tr > You indicate the start of each row using the opening < tr > tag. TR means table row. </li>
  <li>< td > each cell of a table is represented using a TD element. the td stands for table data. at the end of each cell you use a closing < / td > tag.</li>
  <li>the < th > element is used jsut like the < td > element but its purpose is to represent the heading for either a column or a row. (the TH stands for a table heading). Even if a cell has no content you should still use a td or th element to represent the presence of an empty cell otherwise the table will not render correctly.</li>
  
  <table id = "example">
    <tr>
      <th colspan="2">Example</th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th rowspan="2">Example</th>
      <td></td>
      <td></td>
    </tr>
  </table>

  <li>Spanning Coloumns</li>
    <ul>
      <li> Sometimes you may need the entries in a table to stretch across more than on coloumn<li>
      <li>the "colspan" attribute can be used on a "th" or "td" element and indicates how many columns that cell should run accross</li>
      <li> Examples above</li>
    </ul>
  <li>Spanning Rows</li>
    <ul>
      <li>You made also need entries in a table to stretch down across more than one row. The "rowspan" attribute can be used on a "th" or "td" elemeent to indicate how many rows a cell should span dowm the table.
      <li> Examples above</li>
    </ul>
  <li>Long Tables</li>
    <ul>
      <li>There are three elements that help distinguish between the main content of the table and the first and last rows (which cna contain different content).</li>
      <li> < THEAD > the headings of the table should sit inside of the "< THEAD >" element.</li>
      <li> < TBODY > The body should sit inside of the "< TBODY"> element</li>
      <li> < TFOOT > The footer belongs inside of the "< TFOOT >" element.</li>
      <li>By default, browsers rarely treate the content of these elemenets any differently from other elements how ever disginers often use CSS styles to change their appearance.</li>
    </ul>
</ul>

## Chapter 3: “Functions, Methods, and Objects” (pp.106-144)

### Creating an Object: Constructor Notation
    <p> The "new" keyword and the object constructor create a blank object. You can then add properties and methods to the object</p>
#### Exmaple
    var hotel = new object();
    hotel.exampleOne = 'Duckett';           <-- Properties
    hotel.exampleTwo = 42;
    hote.exampleThree = 25;

    hotel.checkAvailability = function() {
      return this.exampleTwo - this.exampleThree;   <--Method
    }:
#### Exmaple 
<ul>
  <li>First, You'll create a new object using a combination of the "new" keyword and the "object()" constructor function. This function is part of the JavaScript language and is used to create objects.</li>
  <li>Updating an Object</li>
    <ul>
      <li>To update the value of properties, use dot notation or square brackets. They work on objects created using literal or constructor notation. To delete a property, use the "delete" keyword.</li>
      <li> To update a propperty use the same technique that was shown on the left-hand page to add properties to the object, but give it a new value.</li>
      <li> You can also update the properties of an object(but not methods) using square bracket syntax. The object name is followed by square brackets, and the property name is inside them</li>
      <li> to delete a property, use the "delete" keyword followed by the object name and property name.</li>
    </ul>
  <li>Creating many objects constructor notation</li>
    <ul>
      <li> Sometimes you will want several objects to represent similar things. Object constructors can use a function as a "template" for creating objects. First, create the template with the object's properties and methods.</li>
    </ul>
  <li>Three Groups of Built-In Objects</li>
    <ul>
      <li> Using built in objects</li>
      <li>The three sets of built-in objects each offer a different range of tools that help you write scripts for web pages.</li>
      <li>Browser Object Model</li>
      <li>The browser object model creates a model of the browser tab or window.</li>
        <ul>
          <li> the topmost object is "window" object, which represents current browser window or tab. Its child objects represent other browser features.</li>
          ***Example***
          <li>Window - Current browser window or tab<li>
            <ul>
              <li> Document - Current Web Page </li>
              <li> History - Pages in Browser History </li>
              <li> Location - URL of current Page </li>
              <li> Navigator - Information About Browser </li>
              <li> Screen  - Device's Display Information </li>
            </ul>
        </ul>
      <li> Document Object Model</li>
        <ul>
          <li>The Document Object Model (DOM) creates a model of the current web page. The topmost object is the "document" object, which represents the page as a whole. Its child objects represents other items on the page.</li>
        </ul>
        <ul>
          <li>Document</li>
          <li>< html > </li>
        </ul>
      <ul>
        <li>< head ></li>
        <li>< title ></li>
      </ul>
                <ul>
                  <li> < body > </li>
                  <li> < div > </li>
                  <li> < p > </li>    <li> attribute</li>
                  <li> text </li>
                </ul>
      </ul>
      <ul>
        <li>Global JavaScript Objects</li>
        <li> The global objects do not form a single model. They are group of individual pobjects that relate to different parts of the JavaScript Language. The names of the global objects usually start with a capital letter. IE: the String and Data objects.</li>
      </ul>
        <li> These Objects are basic data Types:</li>
      <ul>
        <li> String - For Working with string values</li>
        <li> Number - For working the numeric values</li>
        <li> Boolean - For working with boolean values</li>
      </ul>
        <li> These objects help deal with real world concepts</li>
      <ul>
        <li> Date - to represent and handle dates</li>
        <li> Math - for working with numbers and calculations</li>
        <li> Regex - for matching patterns within strings of text</li>
      </ul>
    </ul>
</ul
