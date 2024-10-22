// secretsTest2.js

// Intentionally exposing an AWS secret access key
const awsSecretKey = "AKIAIOSFODNN7EXAMPLE"; // Example AWS secret key

function connectToAWS() {
    console.log(`Connecting to AWS with secret key: ${awsSecretKey}`);
}

connectToAWS();
