# Class 7

## Reading Notes 5
## Chapter 5 "Images"

### Chapters learning goals
  <ol>
    <li>Include an image in your web pages using HTML </li>
    <li>pick which image format to use</li>
    <li>Show an image at the right size</li>
    <li>optimize an image for use on the web to make pages load faster</li>
  </ol>
  
  ### Choosing images for your site
  <ol>
    <li>Be relevent</li>
    <li>Convey information</li>
    <li>Convey the right mood</li>
    <li>Be instantly recognisable</li>
    <li>Fit the color pallete</li>
  </ol>

  ### Storing images on your site
  <ul>
    <li> If you are building a site from scratch, it is good practice to create a folder for all of the images the site uses.</li>
    <li>As the website grows keeping those images in a seperate folder keeps all of your pictures organized and able to be easily accessed.</li>
    <li>For bigger websites you may look to using a content management system or a blogging platform. With those, there are usually built in tools to allow you to upload images easier and more conviently</li>
    </ul>

  ### Adding Images
  <ul>
    <li> To add an image into the page you will need to us an <img> element. This is an empty element (not needing to be closed). It must carry the following Elements.
      <ol>
        <li> <src> This tells the browser where it can find the image file. This will usually be a relative URL poointing to an image on your own site.</li>
        <li> <arc> This provides a text description of the image which describes the image if you cannot see it. </li>
        <li> <title> You can also use the title attribute with the <img> element to provide addition information about the image. Most browsers will display the content of this attribute in a tooltip when the use hovers over the image. </li>
      </ol>
  </ul>

  ### Where to place Images in your code
  <ul>
    <li> Where an image is placed in the code will affect how it is displayed.</li>
      <ol>
        <li>Before a paragraph. The paragraph starts on a new line after the image.</li>
        <li>Inside the start of a paragraph. The first row of text aligns with the bottom of the image</li>
        <li>in the middle ofa paragraph. The image is placed between the words of the paragraph that it appears in.</li>
      </ol>
  </ul>

  ### Three Rules to creating images
<ol>
  <li> Save images in the right FORMAT</li>
    <li> Websites mainly use images in JPEG. GIF. or PNG. Format. If you choose the wrong image format than your image might not look as sharp as it should and can make the web page slower to load.</li>
  <li> Save images at the right SIZE</li>
    <li> You should save the image at the same width and height it will appear on the website(pixels). If the image is smaller than the width or heigh that you have specifiedm, the image can be distorted and stretched. if the image is larger than the width and height you have specified, the image will take longer to display on the page.<li>
  <li> Measure images in PIXELS</li>
    <li> Computer screens are made up of tiny squares known as pixels the number of pixels shown per inch of screen can vary if the user increases or decreases the resolution. Therefore, when you are saving images at the right size for use on the web, you should always measure the images in terms of the width and height in pixels(and not in centimeters or inches).</li>
</ol>

## Chapter 11 "Color"

<ol>
  <li> How to specify Colors </li>
  <li> Color terminology and contrast</li>
  <li> Background color</li>
</ol>

### Background Color
  <ul>
    <li>Background-color</li>
    <li>Css treats each HTML element as if it appears in a box, and the background-color property sets the color of the background for that box.</li>
    <li>You can specify your choice of background color in the same three ways you can specify foreground colors: RGB values, hex codes, and color names. </li>
    <li>If you do not specify a background color, then the background is transparent</li>
    <li>By default, most browsers windows have a white background, but browser users can set a background color for their windows, so if you want to be sure that the background is white you can use the background-color property on the <body> element.</li>
    <li> We have also used the padding property to sperate the text for the edges of the boxes. This makes it easier to read.</li>
  </ul>

### Color Terminology and Contrast
  <ul>
    <li> Every Color on a computer screen is created by mixing amounts of red, green, and blue. To find the color you want, you can use a color picker.(most common way to pick colors).</li>
    <li>RGB Values</li>
      <li>Balues for red, green, and blue are expressed as numbers between 0 and 255. RGB(102,205,170) This color is made up of 102 red, 205 green, 170 blue. </li>
    <li>HEX codes</li>
      <li> Hex values represent values for red, green, and blue iin hexadecimal code. #66cdaa This value of the red 102 is expressed as "66" in hexadecimal code. the 205 green is expressed as "cd" and the 170 of blue equates to "aa"</li>
    <li>Color Names</li>
      <li>Colors are represented by predefined names. however, they are very limited in number. There are 147 color names supported by browsers. Most consider this to be a limited color palette, and it is hard to remeber the name for each of the colors so (apart from white and black) they are not commonly used. </li>
    <li>HUE</li>
      <li>Hue is near to the colloquial idea of color. Technically speaking however, a color can also have saturation and brightness as well as hue.</li>
    <li>Saturation</li>
      <li>Saturation refers to the amount of gray in a color. At maximum saturation, there would be no gray in the color. at minimum saturation, the color would be mostly gray.</li>
    <li>Brightness</li>
      <li>Brightness(or "value") refers to how much black is in a color. at maximum brightness, there would be no black in the color. at minimum brightness, the color would be very dark</li>
  </ul>

## Chapter 12 "Text"

  ### Size and typeface of text
  <ol>
    <li>Serif</li>
      <li>Serif fonts have extra details on the ends of the main strokes of the letters. These details are known as serifs.</li>
    <li>Sans-Serif</li>
      <li>Sans-serif fonts have straight ends to letters, and therefore have a much cleaner design.</li>
    <li>MonoSpace</li>
      <li>Every letter in a monospace (or fixed-width) font is the same width (non-monospace fonts have different widths)</li>
    <li>Cursive</li>
      <li>Cursive fonts either have joining strokes or other cursive characteristics, such as handwriting styles.</li>
    <li>Fantasy</li>
      <li>Fantasy fonts are usually decorative fonts and are often used for titles. They're not designed for long bodies of text.</li>
    <li>Weight</li>
      <li>the fonts weight not only adds emphasis but can alos affect the amount of white space and contrast on a page.</li>
    <li>Style</li>
      <li>Italic fonts have a cursive aspect to some of the lettering. Oblique font styles take the normal style and put it on an angle.</li>
    <li>Stretch</li>
      <li>In condensed (or narrow) versions of the font, letters are thinner and closer together. in expanded versionsthey are thicker and further apart.</li>
  </ol>

