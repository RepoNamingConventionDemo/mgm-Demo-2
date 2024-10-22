// secretsTest3.js

// Intentionally exposing a hardcoded Stripe API key
const stripeApiKey = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"; // Example Stripe API key

function processPayment() {
    console.log(`Processing payment with Stripe API key: ${stripeApiKey}`);
}

processPayment();
