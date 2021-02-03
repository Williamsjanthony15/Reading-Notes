# Read 7

## Chapter 6: “Tables” (pp.126-145)
 ### What is a table.
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

<ul>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
</ul
