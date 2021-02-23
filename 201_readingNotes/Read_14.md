 Read 14

# Transforms

<li> The transform property comes in two different settings, two-dimensional and three-dimensional. Each of these come with their own individual properties and values. </li>

## Transform Syntax

 div {
  -webkit-transform: scale(1.5);
     -moz-transform: scale(1.5);
       -o-transform: scale(1.5);
          transform: scale(1.5);
}

## 2D Transforms

<p> Elements may be distorted, or transformed, on both a two-dimensional plane or a three-dimensional plane. Two-dimensional transforms work on the x and y axes, known as horizontal and vertical axes. Three-dimensional transforms work on both the x and y axes, as well as the z axis </p>

### 2D Rotate
<p> The transform property accepts a handful of different values. The rotate value provides the ability to rotate an element from 0 to 360 degrees. Using a positive value will rotate an element clockwise, and using a negative value will rotate the element counterclockwise. The default point of rotation is the center of the element, 50% 50%, both horizontally and vertically. Later we will discuss how you can change this default point of rotation. </p>

#### HTML
<figure class="box-1">Box 1</figure>
<figure class="box-2">Box 2</figure>

#### CSS
.box-1 {
  transform: rotate(20deg);
}
.box-2 {
  transform: rotate(-55deg);
}

### 2D Scale
<p> Using the scale value within the transform property allows you to change the appeared size of an element. The default scale value is 1, therefore any value between .99 and .01 makes an element appear smaller while any value greater than or equal to 1.01 makes an element appear larger. </p>


 #### HTML
 <figure class="box-1">Box 1</figure>
 <figure class="box-2">Box 2</figure>

#### CSS
.box-1 {
  transform: scale(.75);
}
.box-2 {
  transform: scale(1.25);
}

 ##### Scale specific Axis'
 <p> It is possible to scale only the height or width of an element using the scaleX and scaleY values. The scaleX value will scale the width of an element while the scaleY value will scale the height of an element. To scale both the height and width of an element but at different sizes, the x and y axis values may be set simultaneously. To do so, use the scale transform declaring the x axis value first, followed by a comma, and then the y axis value. </p> 
 
 ###### HTML
<figure class="box-1">Box 1</figure>
<figure class="box-2">Box 2</figure>
<figure class="box-3">Box 3</figure>

###### CSS
.box-1 {
  transform: scaleX(.5);
}
.box-2 {
  transform: scaleY(1.15);
}
.box-3 {
  transform: scale(.5, 1.15);
}

# Transitions & Animations

## Transitions
 <p> With CSS3 transitions you have the potential to alter the appearance and behavior of an element whenever a state change occurs, such as when it is hovered over, focused on, active, or targeted. </p>
 
 <li> change its background color over the course of 1 second in a linear fashion. </li>
 
.box {
  background: #2db34a;
  transition-property: background;
  transition-duration: 1s;
  transition-timing-function: linear;
}
.box:hover {
  background: #ff7b29;
}

### Transitional Property
<p> The transition-property property determines exactly what properties will be altered in conjunction with the other transitional properties. By default, all of the properties within an element’s different states will be altered upon change. However, only the properties identified within the transition-property value will be affected by any transitions. </p>

<p> If multiple properties need to be transitioned they may be comma separated within the transition-property value. Additionally, the keyword value all may be used to transition all properties of an element. </p>

.box {
    background: #2db34a;
    border-radius: 6px
    transition-property: background, border-radius;
    transition-duration: 1s;
    transition-timing-function: linear;
  }
  .box:hover {
    background: #ff7b29;
    border-radius: 50%;
  }

## ***Note not all properties may be transitioned, only properties that have an identifiable halfway point.*** 




## Animations within CSS3 allow the appearance and behavior of an element to be altered in multiple keyframes. Transitions provide a change from one state to another, while animations can set multiple points of transition upon different keyframes.

## Popular Transitioning Properties

<li>background-color</li>
<li>border-width</li>
<li>clip</li>
<li>font-size</li>
<li>left</li>
<li>margin</li>
<li>min-height</li>
<li>outline-color</li>
<li>padding</li>
<li>text-shadow</li>
<li>visibility</li>
<li>z-index</li>
<li>background-position</li>
<li>border-spacing</li>
<li>color</li>
<li>font-weight</li>
<li>letter-spacing</li>
<li>max-height</li>
<li>min-width</li>
<li>outline-offset</li>
<li>right</li>
<li>top</li>
<li>width</li>
<li>border-color</li>
<li>bottom</li>
<li>crop</li>
<li>height</li>
<li>line-height</li>
<li>max-width</li>
<li>opacity</li>
<li>outline-width</li>
<li>text-indent</li>
<li>vertical-align</li>
<li>word-spacing</li>

