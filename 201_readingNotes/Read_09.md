# Reading 09

# Html & CSS

## Chapter 7: Forms

### Forms

<li> The term 'form' has referred to a printed document thjat contains spaces for you to fill in information. Html Borrows the concept of a form to refer to different elements that allow you to collect information from vistors to your site.</li>
#### Why Forms?
<ul>
<li>Form Controls</li>
<p>There are several types of form controls that you can use to collect information from visitors to your site.</p>
<ol>
<li>Adding Text</li>
<p> Text Input - Used for a single line of text such as an email address or names.</p>
<p> Password Input - Like a single line text box but it masks the characters entered. </p>
<p> Text Area - For longer areas of text, such as a message or comment. </p>
 
<li>Making Choices</li>
<p> Radio Buttons - for use when a user must select one of a number of options.</p>
<p> Check Boxes - When a user can select and unselect one or more options.</p>
<p> Drop-Down Boxes - When a user must pick one of a number of options from a list.</p>
 
<li>Submitting Forms</li>
<p> Submit Buttons - To submit data from your form to another web page.</p>
<p> Image Buttons - Similar to submit button but they allow you to use an image.</p>
 
<li>Uploading Files</li>
<p> File Upload - Allows users to upload files (IE: images) to a website.</p>
</ol>
 
#### <li> How forms work</li>
 
<ol>
<li> A user filles in a form, and then presses a button to submit the information to the server. </li>
<li>The name of each form control is sent to the server along the value the user enters or selects. </li>
<li>The Server processes the information using a programming language such as PHP, C#, VB.net, or java. It may also store the information in a database. </li>
</ol>
 
#### <li> Form Structure </li>
<p> Form Controls live inside a < form > element. This element should always carry hte action attribute and will usually have a method and id attribute too.
 
<ul>
#### <li> Action - Ever < form > element requires an action attribute. Its value is the url for the page and the server that will receive the information in the form when it is submitted. </li>
 
#### <li> Method - Forms can be sent using one of two methods:</li>
<ul>
<li> Get </li>
##### <p> Get method, the values from the form are added to the end of the URL specified in the action attribute. The get method is ideal for:
<ol>
<li> Short Forms (such as search boxes)</li>
<li> When you are just retrieving data from the web server (not sending formation that should be added to or deleted from a database).</li>
</ol>
##### <li> Post - method the values are sent in what are known as HTTP headers. As a rule of thumb you should use the post method if your form: </li>
<ol>
<li> Allows users to upload a file </li>
<li> Is very long </li>
<li> Contains Sensitive Data (IE: passwords) </li>
<li> Adds information to, or deletes information from, a database.</li>
</ol>
##### <li>  ID - the value is used to identify the form distincly from other elements on the page (and is often used by scripts - such as those that check you have entered information into fields that require values)</li>
##### <li> Size - The size attribute should not be used on new forms. it was used in older forms to indicate the width of the text input ( measured by the number of characters that would be seen). Any new forms that are created should use CSS to control them.
</ul>
</ul>
</ul>
 
## Chapter 14: lists, tables, and forms
<p> Thre are several CSS properties that were created to work with specific types of HTML elements, Such as lists, Tables, and Forms. </p>
 
### List's
<p> Specify the type of bullet point or numbering on lists </p>
<ul>
<li> Unordered lists </li>
<li> Ordered Lists</li>
<li> Decimal </li>
<li> Decimal - leading - zero </li>
<li>Lower - Alpha </li>
<li> Upper - Alpha </li>
<li> Lower - Alpha </li>
<li> Upper - Roman </li>
</ul>
 
### Table's
<p> Add borders and backgrounds to table cells</p>
<ul>
<li> Width </li>
<li> Padding </li>
<li> Text-transform</li>
<li> Letter spacing, font size</li>
<li> Border-top, border-bottom </li>
<li> Text - align</li>
<li> Background - color</li>
<li> :hover </li>
</ul>
 
<ul>
<p> tips for styling your table and keeping clean and easy to follow data. </p>
<li> Give cells padding - if the text in a table cell either touches a border (or another cell), it becomes much harder to read. adding a padding helps to improved readability.</li>
<li> Distinguish headings - Putting all thable headings in bold (the default style for the < th > element makes them easier to read. you can also make headings uppercase and then either add abackground color or an underline to clearly distinguish them from the content.</li>
<li> Share Alternate Rows - Shading every other row can help users follow along the lines. use a sublet distinction from the normal color of the rows to keep the table looking clean. </li>
<li> Align Numerals - you can use the text align property to align the content of any column that contains numbers to the right, so that large numbers are cleary distinguished from smaller ones. </li>
</ul>
 
### Form's
<p> control the appereance of form controls  </p>
<ul>
<p> Css is commonly used to control the appearnce of form elements. this is bot to make them more attractive and to make them more consistent across different browsers. It is most common to style:
<ol>
<li> Text inputs and text areas </li>
<li> Submit Buttons </li>
<li> labels on forms, to get the form controls to align nicely </li>
</ol>
 
<li> Styling text inputs</li>
<ol>
<li> font-size sets the size of the text entered by the user.</li>
<li> Color sets the text color, and background-color sets the background color of the input.</li>
<li> Border adds a border around the edge of the input box, and border radius can be used to create rounded corners (for browsers that support this property).</li>
<li> Focus psuedo class is used to change the background color of the text input when it is being used, and the hover psuedo class applies the same styles when the user hovers over them. </li>
<li> Background image adds a backgorund image to the box. because there is a different image for each input, we are using an attribute selector looking for the value of the id attribute on each input. </li>
</ol>
<li>Styling Submit Buttons</li>
<li>Styling FieldSets and legends</li>
<li> Aligning form controls: problem</li>
<li> Aligning form controlsL: solution</li>
</ul>
 
 
# JavaScript
 
## Chapter 6: Events
 
### Events
<p> When you browse the web, your browser registers different types of events. its the browsers way of saying, "hey, this just happened." Your script can then respond to these events. </p>
<ul>
<p> main thing to know </p>
<li> Event Flow P(pg 260)</li>
<li> Why Flow Matters (pg 261)</li>
<li> Different types of events (pg 271)</li>
<li> User interface events (pg 272)</li>
<li> Moust events (pg 276)</li>
<li> Where events occur (pg 278)</li>
<li> Keyboard events (280)</li>
<li></li>
<li></li>
</ul>
