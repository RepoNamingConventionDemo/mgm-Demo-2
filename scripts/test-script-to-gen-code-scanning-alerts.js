function vulnerableFunction() {
  var userInput = prompt("Enter a number:");
  eval("alert('User input: ' + userInput);"); // CodeQL might flag this for using eval
}
