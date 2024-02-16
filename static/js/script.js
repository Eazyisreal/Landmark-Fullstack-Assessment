const loginIcon = document.getElementById('login-icon');
const loginContainer = document.getElementById('login-container')
const hamburger = document.getElementById('hamburger');
const messageHamburger = document.getElementById('message-hamburger');
const successAlert = document.getElementById('success-alert');
const nav = document.getElementById('nav');
const navItem = document.getElementById('nav-item');
const active = document.getElementById('active');
const sortActive = document.getElementById('sort-active');
const sortCategory = document.getElementById('sort-category');
const sort = document.getElementById('sort');
const cart = document.querySelectorAll('.add-to-cart');
const wishlist = document.querySelectorAll('.add-to-wishlist');
const absolute = document.querySelector(".absolute")
const cartItemQuantityElements = document.querySelectorAll('.cart-item-quantity');

cartItemQuantityElements.forEach(element => {
    const quantityInput = element.querySelector('input[name="quantity"]');
    const decrementButton = element.querySelector('.decrement');
    const incrementButton = element.querySelector('.increment');

    decrementButton.addEventListener('click', () => {
        let quantity = parseInt(quantityInput.value);
        if (quantity > 1) {
            quantity--;
            quantityInput.value = quantity; 
        }
    });

    incrementButton.addEventListener('click', () => {
        let quantity = parseInt(quantityInput.value);
        quantity++;
        quantityInput.value = quantity; 
    });
});


cart.forEach(img => {
    img.addEventListener('click', addToCart)
})



function addToCart(event){
    const productId = event.target.getAttribute('data-product-id');
    fetch(`/add-to-cart/${productId}/`)
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error(`Error adding to Cart: ${response.statusText}`);
      }
    })
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error('Error adding to cart:', error);
    });
}

function toggleLoginIcon() {
    loginContainer.classList.toggle('visible');
    active.classList.toggle('visible')
};


function closeMessage(){
  successAlert.classList.toggle('visible');
}




function toggleMobile() {
    nav.classList.toggle('visible');
    navItem.classList.toggle('visible');
    hamburger.classList.toggle('visible');
}


function toggleProducts(){
    sortCategory.classList.toggle('visible')
    sortActive.classList.toggle('visible')
}

loginIcon.addEventListener('click', toggleLoginIcon);
hamburger.addEventListener('click', toggleMobile);
sort.addEventListener('click', toggleProducts);
messageHamburger.addEventListener('click', closeMessage);

