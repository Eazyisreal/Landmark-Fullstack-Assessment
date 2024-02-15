const loginIcon = document.getElementById('login-icon');
const loginContainer = document.getElementById('login-container')
const hamburger = document.getElementById('hamburger');
const nav = document.getElementById('nav');
const navItem = document.getElementById('nav-item');
const active = document.getElementById('active');
const sortActive = document.getElementById('sort-active');
const sortCategory = document.getElementById('sort-category');
const sort = document.getElementById('sort');
const cart = document.querySelectorAll('.add-to-cart');
const wishlist = document.querySelectorAll('.add-to-wishlist');
const absolute = document.querySelector(".absolute")



cart.forEach(img => {
    img.addEventListener('click', addToCart)
})


wishlist.forEach(img => {
    img.addEventListener('click', addToWishlist)
})

function addToWishlist(event) {
  const productId = event.target.getAttribute('data-product-id');
  fetch(`/wishlist/${productId}/`)
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error(`Error adding to wishlist: ${response.statusText}`);
      }
    })
    .then(data => {
      console.log('Response Data:', data);
      // Display the message to the user
      alert(data.message); // Or update the UI in some way
    })
    .catch(error => {
      console.error('Error adding to wishlist:', error);
      console.error(error.stack); // Log the full error stack trace

    });
}



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

setTimeout(function() {
  var successAlert = document.getElementById('success-alert');
  if (successAlert) {
      successAlert.classList.add('hide');
  }
}, 1500);

// Add animation effect when hiding the success message
document.addEventListener('DOMContentLoaded', function() {
  var successAlert = document.getElementById('success-alert');
  if (successAlert) {
      successAlert.addEventListener('transitionend', function() {
          successAlert.style.display = 'none';
      });
  }
