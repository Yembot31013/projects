let productInCart = [];
const parentElement = document.querySelector('.buyItems');
const cartSumPrice = document.querySelector('.btn-cart')
const products = document.querySelectorAll('.product-under');
const empty = document.querySelector('.empty')

const updateShoppingCartHTML = function(){
  if(productInCart.length > 0){
    let result = productInCart.map(product =>{
      return`
      <li class="container buyItem">
      <div class="testimonial bg-primary buy-item">
        <img src="${product.image}" alt="">
        <p class="cart-item-name">${product.name}</p>
        <div>
          <button class="button-minus" data-id='${product.id}'>-</button>
          <span class="countOfProduct">${product.count}</span>
          <button class="button-plus" data-id='${product.id}'>+</button>
        </div>
        <p class="cart-item-name">$${product.price}</p>
      </div>
    </li>
      `
    })
    parentElement.innerHTML = result.join('');
    empty.classList.add('delete');
  }
  else{
   empty.classList.remove('delete'); 
   cartSumPrice.innerHTML='';
  }
}

function updateProductInCart(product){
  for(let i = 0; i < productInCart.length; i++){
    if(productInCart[i].id == product.id){
      productInCart[i].count += 1;
      productInCart[i].price = productInCart[i].basePrice * productInCart[i].count;
      return;
    }
  }
  productInCart.push(product);
}


products.forEach(product => {
  product.addEventListener('click', (e)=>{
   if(e.target.classList.contains('addToCart')){
     alert('clicked')
     const productId = e.target.dataset.productId;
     const productName = product.querySelector('.productName').innerHTML;
     const productPrice = product.querySelector('.priceValue').innerHTML;
     const productImg = product.querySelector('img').src;
     let productToCart = {
       name: productName,
       image: productImg,
       id: productId,
       count: 1,
       price: +productPrice,
       basePrice: +productPrice 

     }
     updateProductInCart(productToCart);
     updateShoppingCartHTML();
   } 
  })
})