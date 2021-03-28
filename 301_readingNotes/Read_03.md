# Read 03

## Lifting State Up

Often, several components need to reflect the same changing data. We recommend lifting the shared state up to their closest common ancestor. Let’s see how this works in action.

It accepts the celsius temperature as a prop, and prints whether it is enough to boil the water
---------------------------------------------
function BoilingVerdict(props) {
  if (props.celsius >= 100) {
    return <p>The water would boil.</p>;
  }
  return <p>The water would not boil.</p>;
}
----------------------------------------------
create a component called Calculator. It renders an <input> that lets you enter the temperature, and keeps its value in this.state.temperature.

----------------------------------------------
class Calculator extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.state = {temperature: ''};
  }

  handleChange(e) {
    this.setState({temperature: e.target.value});
  }

  render() {
    const temperature = this.state.temperature;
    return (
      <fieldset>
        <legend>Enter temperature in Celsius:</legend>
        <input
          value={temperature}
          onChange={this.handleChange} />
        <BoilingVerdict
          celsius={parseFloat(temperature)} />
      </fieldset>
    );
  }
}
---------------------------------------------

## Adding a Second Input

extracting a TemperatureInput component from Calculator.
add a new scale prop to it that can either be "c" or "f"

-------------------------------------------------------------------
const scaleNames = {
  c: 'Celsius',
  f: 'Fahrenheit'
};

class TemperatureInput extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.state = {temperature: ''};
  }

  handleChange(e) {
    this.setState({temperature: e.target.value});
  }

  render() {
    const temperature = this.state.temperature;
    const scale = this.props.scale;
    return (
      <fieldset>
        <legend>Enter temperature in {scaleNames[scale]}:</legend>
        <input value={temperature}
               onChange={this.handleChange} />
      </fieldset>
    );
  }
}
--------------------------------------------------------------------


change the Calculator to render two separate temperature inputs

--------------------------------------------
class Calculator extends React.Component {
  render() {
    return (
      <div>
        <TemperatureInput scale="c" />
        <TemperatureInput scale="f" />
      </div>
    );
  }
}
-------------------------------------------

## Writing Conversion Functions

two functions to convert from Celsius to Fahrenheit and back

------------------------------------------
function toCelsius(fahrenheit) {
  return (fahrenheit - 32) * 5 / 9;
}

function toFahrenheit(celsius) {
  return (celsius * 9 / 5) + 32;
}
-------------------------------------------

Functions will convert the numbers. Another function that takes a string 'temparture' and a cenverter function as arguments and returns a string. we will us it to calculate the value of one input based on the other input. 

It returns an empty string on an invalid temperature, and it keeps the output rounded to the third decimal place

------------------------------------------------
function tryConvert(temperature, convert) {
  const input = parseFloat(temperature);
  if (Number.isNaN(input)) {
    return '';
  }
  const output = convert(input);
  const rounded = Math.round(output * 1000) / 1000;
  return rounded.toString();
}
-------------------------------------------------

** - tryConvert('abc', toCelsius) returns an empty string, and tryConvert('10.22', toFahrenheit) returns '50.396' -**


## Lifting State Up

sharing state is accomplished by moving it up to the closest common ancestor of the components that need it.
remove the local state from the TemperatureInput and move it into the Calculator instead.
replace this.state.temperature with this.props.temperature in the TemperatureInput component.
----------------------------- 
render() {
// Before: const temperature = this.state.temperature;
// After:  const temperature = this.props.temperature;
---------------------------------

When the temperature was in the local state, the TemperatureInput could just call this.setState() to change it.
However, now that the temperature is coming from the parent as a prop, the TemperatureInput has no control over it.

This is usually solved by making a component “controlled”.
Just like the DOM <input> accepts both a value and an onChange prop, so can the custom TemperatureInput accept both temperature and onTemperatureChange props from its parent Calculator.

** Note:

There is no special meaning to either temperature or onTemperatureChange prop names in custom components. We could have called them anything else, like name them value and onChange which is a common convention.

**

The onTemperatureChange prop will be provided together with the temperature prop by the parent Calculator component. It will handle the change by modifying its own local state, thus re-rendering both inputs with the new values.

Before diving into the changes in the Calculator, let’s recap our changes to the TemperatureInput component. We have removed the local state from it, and instead of reading this.state.temperature, we now read this.props.temperature. Instead of calling this.setState() when we want to make a change, we now call this.props.onTemperatureChange(), which will be provided by the Calculator

-------------------------------------------------------------
class TemperatureInput extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    this.props.onTemperatureChange(e.target.value);
  }

  render() {
    const temperature = this.props.temperature;
    const scale = this.props.scale;
    return (
      <fieldset>
        <legend>Enter temperature in {scaleNames[scale]}:</legend>
        <input value={temperature}
               onChange={this.handleChange} />
      </fieldset>
    );
  }
  }
  ------------------------------------------------------------
  
  store the current input’s temperature and scale in its local state. This is the state we “lifted up” from the inputs, and it will serve as the “source of truth” for both of them. It is the minimal representation of all the data we need to know in order to render both inputs.
  
  
Now, when the TemperatureInput wants to update its temperature, it calls this.props.onTemperatureChange:

   
----------------------------------------------
** If we enter 37 into the Celsius input, the state of the Calculator component will be:
{
  temperature: '37',
  scale: 'c'
}
** If we later edit the Fahrenheit field to be 212, the state of the Calculator will be:

{
  temperature: '212',
  scale: 'f'
}

-----------------------------------------------

FINAL CODE ****-------------------------------------------------------------------------------------****

class Calculator extends React.Component {
  constructor(props) {
    super(props);
    this.handleCelsiusChange = this.handleCelsiusChange.bind(this);
    this.handleFahrenheitChange = this.handleFahrenheitChange.bind(this);
    this.state = {temperature: '', scale: 'c'};
  }

  handleCelsiusChange(temperature) {
    this.setState({scale: 'c', temperature});
  }

  handleFahrenheitChange(temperature) {
    this.setState({scale: 'f', temperature});
  }

  render() {
    const scale = this.state.scale;
    const temperature = this.state.temperature;
    const celsius = scale === 'f' ? tryConvert(temperature, toCelsius) : temperature;
    const fahrenheit = scale === 'c' ? tryConvert(temperature, toFahrenheit) : temperature;

    return (
      <div>
        <TemperatureInput
          scale="c"
          temperature={celsius}
          onTemperatureChange={this.handleCelsiusChange} />
        <TemperatureInput
          scale="f"
          temperature={fahrenheit}
          onTemperatureChange={this.handleFahrenheitChange} />
        <BoilingVerdict
          celsius={parseFloat(celsius)} />
      </div>
    );
  }
}

FINAL CODE ****-------------------------------------------------------------------------------------****

# Lessons Learned Recap

React calls the function specified as onChange on the DOM <input>. In our case, this is the handleChange method in the TemperatureInput component.

The handleChange method in the TemperatureInput component calls this.props.onTemperatureChange() with the new desired value. Its props, including onTemperatureChange, were provided by its parent component, the Calculator.

When it previously rendered, the Calculator had specified that onTemperatureChange of the Celsius TemperatureInput is the Calculator’s handleCelsiusChange method, and onTemperatureChange of the Fahrenheit TemperatureInput is the Calculator’s handleFahrenheitChange method. So either of these two Calculator methods gets called depending on which input we edited.

Inside these methods, the Calculator component asks React to re-render itself by calling this.setState() with the new input value and the current scale of the input we just edited.

React calls the Calculator component’s render method to learn what the UI should look like. The values of both inputs are recomputed based on the current temperature and the active scale. The temperature conversion is performed here.

React calls the render methods of the individual TemperatureInput components with their new props specified by the Calculator. It learns what their UI should look like.

React calls the render method of the BoilingVerdict component, passing the temperature in Celsius as its props.

React DOM updates the DOM with the boiling verdict and to match the desired input values. The input we just edited receives its current value, and the other input is updated to the temperature after conversion.

Every update goes through the same steps so the inputs stay in sync.



https://reactjs.org/docs/lifting-state-up.html
