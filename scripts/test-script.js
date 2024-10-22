// secretsTest.js

// Intentionally exposing a secret token
const secretToken = "ghp_16cHn0w..."; // Example GitHub token

function authenticate() {
    console.log(`Authenticating with token: ${secretToken}`);
}

authenticate();
