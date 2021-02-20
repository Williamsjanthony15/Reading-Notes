# LOCAL STORAGE

check for HTML5 Storage

function supports_html5_storage() {
  try {
    return 'localStorage' in window && window['localStorage'] !== null;
  } catch (e) {
    return false;
  }
}
Instead of writing this function yourself, you can use Modernizr to detect support for HTML5 Storage.

if (Modernizr.localstorage) {
  // window.localStorage is available!
} else {
  // no native support for HTML5 storage :(
  // maybe try dojox.storage or a third-party solution
}

HTML5 Storage is based on named key/value pairs. You store data based on a named key, then you can retrieve that data with the same key.

key is a string

The data can be any type supported by JavaScript, including strings, Booleans, integers, or floats. However, the data is actually stored as a string. If you are storing and retrieving anything other than strings, you will need to use functions like parseInt() or parseFloat() to coerce your retrieved data into the expected JavaScript datatype

key	string	-- the named key that was added, removed, or modified
oldValue	any	-- the previous value (now overwritten), or null if a new item was added
newValue	any	-- the new value, or null if an item was removed
url*	string	-- the page which called a method that triggered this change

