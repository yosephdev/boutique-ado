/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Get the Stripe public key and client secret from the hidden elements
var stripe_public_key = document.getElementById('id_stripe_public_key').textContent.trim();
var client_secret = document.getElementById('id_client_secret').textContent.trim();

// Initialize Stripe and create an instance of elements
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

// Custom styling for the Stripe card element
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create a card element
var card = elements.create('card', { style: style });

// Mount the card element to the card-element div
card.mount('#card-element');