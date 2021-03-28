# READING NOTES

## State and Lifecycle

In this section, we will learn how to make the Clock component truly reusable and encapsulated. It will set up its own timer and update itself every second. 
____________________________________________________
function Clock(props) {
  return (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {props.date.toLocaleTimeString()}.</h2>
    </div>
  );
}

function tick() {
  ReactDOM.render(
    <Clock date={new Date()} />,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);
_____________________________________________________

Updates the UI every second should be an implementation detail of the CLOCK

Write this once and have the clock update itself:
_____________________________
ReactDOM.render(
<Clock />
document.getElementById('root')
);

______________________________

Now to implemenet this we add a "state" to the clock component
state and props are really similiar but **state is private and fully controlled by that compent.** 



### Converting a Function to a Class

Converting the clock into a class in 5 steps

<ol>
  <li> create an ES6 class, with the same name, that extends React.Component </li>
  <li> Add a simple empty method to it called render() </li>
  <li> Move the body of the function to the render() method </li>
  <li> Replace props with this.props in the render() body </li>
  <li> delete the remaining empty function declaration </li>
</ol>

______________________________________________________________
class Clock extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.props.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
_____________________________________________________________


### Adding Local State to a Class

Replace this.props.date with this.state.date in the render() method:

______________________________________________________________
class Clock extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
______________________________________________________________

Add a class constructor that assigns the initial this.state:

______________________________________________________________
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
______________________________________________________________

Note how we pass props to the base constructor:
____________________________________
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }
  __________________________________
Class components should always call the base constructor with props.



Remove the date prop from the <Clock /> element:
__________________________________
ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
__________________________________

The result looks like this:
_______________________________________________________________
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}

ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
______________________________________________________________



### Using State Correctly
There are three things you should know about setState().

#### Do Not Modify State Directly
For example, this will not re-render a component:

// Wrong
this.state.comment = 'Hello';

**Instead, use setState():

// Correct
this.setState({comment: 'Hello'});

**The only place where you can assign this.state is the constructor.



## HANDLING EVENTS

**Handling events with React elements is very similar to handling events on DOM elements.

React events are named using camelCase, rather than lowercase.
With JSX you pass a function as the event handler, rather than a string.

you cannot return false to prevent default behavior in React. You must call preventDefault explicitly.

When using React, you generally don’t need to call addEventListener to add listeners to a DOM element after it is created. Instead, just provide a listener when the element is initially rendered.

For example, this Toggle component renders a button that lets the user toggle between “ON” and “OFF” states:

**You have to be careful about the meaning of this in JSX callbacks. In JavaScript, class methods are not bound by default. If you forget to bind this.handleClick and pass it to onClick, this will be undefined when the function is actually called. 

### Passing Arguments to Event Handlers

Inside a loop, it is common to want to pass an extra parameter to an event handler. For example, if id is the row ID, either of the following would work:

___________________________________________________________________

<button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>
<button onClick={this.deleteRow.bind(this, id)}>Delete Row</button>

___________________________________________________________________


In both cases, the e argument representing the React event will be passed as a second argument after the ID. With an arrow function, we have to pass it explicitly, but with bind any further arguments are automatically forwarded.


## Conditional Rendering

you can create distinct components that encapsulate behavior you need. Then, you can render only some of them, depending on the state of your application

Conditional rendering in React works the same way conditions work in JavaScript. Use JavaScript operators like if or the conditional operator to create elements representing the current state, and let React update the UI to match them.


We’ll create a Greeting component that displays either of these components depending on whether a user is logged in

_________________________________________

function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

ReactDOM.render(
  // Try changing to isLoggedIn={true}:
  <Greeting isLoggedIn={false} />,
  document.getElementById('root')
);

_________________________________________

This example renders a different greeting depending on the value of isLoggedIn prop.

Element Variables
You can use variables to store elements. This can help you conditionally render a part of the component while the rest of the output doesn’t change.

Consider these two new components representing Logout and Login buttons:

function LoginButton(props) {
  return (
    <button onClick={props.onClick}>
      Login
    </button>
  );
}

function LogoutButton(props) {
  return (
    <button onClick={props.onClick}>
      Logout
    </button>
  );
}
In the example below, we will create a stateful component called LoginControl.

It will render either <LoginButton /> or <LogoutButton /> depending on its current state. It will also render a <Greeting /> from the previous example:

#### All together coding for login and logout 

_________________________________________________________________
class LoginControl extends React.Component {
  constructor(props) {
    super(props);
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
    this.state = {isLoggedIn: false};
  }

  handleLoginClick() {
    this.setState({isLoggedIn: true});
  }

  handleLogoutClick() {
    this.setState({isLoggedIn: false});
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    let button;
    if (isLoggedIn) {
      button = <LogoutButton onClick={this.handleLogoutClick} />;
    } else {
      button = <LoginButton onClick={this.handleLoginClick} />;
    }

    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn} />
        {button}
      </div>
    );
  }
}

ReactDOM.render(
  <LoginControl />,
  document.getElementById('root')
);

___________________________________________________________________


While declaring a variable and using an if statement is a fine way to conditionally render a component, sometimes you might want to use a shorter syntax. There are a few ways to inline conditions in JSX, explained below.




#### Inline If with Logical && Operator
You may embed expressions in JSX by wrapping them in curly braces. This includes the JavaScript logical && operator. It can be handy for conditionally including an element:

___________________________________________________________
function Mailbox(props) {
  const unreadMessages = props.unreadMessages;
  return (
    <div>
      <h1>Hello!</h1>
      {unreadMessages.length > 0 &&
        <h2>
          You have {unreadMessages.length} unread messages.
        </h2>
      }
    </div>
  );
}

const messages = ['React', 'Re: React', 'Re:Re: React'];
ReactDOM.render(
  <Mailbox unreadMessages={messages} />,
  document.getElementById('root')
);
____________________________________________________________


It works because in JavaScript, true && expression always evaluates to expression, and false && expression always evaluates to false.

Therefore, if the condition is true, the element right after && will appear in the output. If it is false, React will ignore and skip it.

Note that returning a falsy expression will still cause the element after && to be skipped but will return the falsy expression. In the example below, <div>0</div> will be returned by the render method.





