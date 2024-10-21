function vulnerableFunction() {
  var userInput = prompt("Enter a number:");
  eval("alert('User input: ' + userInput);"); // CodeQL might flag this for using eval
}

function xssVulnerable() {
    var userInput = prompt("Enter some text:");
    document.body.innerHTML += "<div>" + userInput + "</div>"; // Potential XSS
}
