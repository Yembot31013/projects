
const cartBtn = document.querySelector(".btn-cart");
const accountBtn = document.querySelector(".btn-account");
const cart = document.querySelector(".yembot")
const productPage = document.querySelector(".article")
const backBtn = document.querySelector('#back-btn')
const deleteBtn = document.querySelector('#delete-btn')
const empty = document.querySelector('.empty')
const items = document.querySelector('.py-5')

cartBtn.addEventListener('click', function(){
 cart.classList.remove('delete')
 productPage.classList.add('delete')
})

accountBtn.addEventListener('click', function(){
  alert('You Haven\'t login Yet')
})

backBtn.addEventListener('click', function(){
  cart.classList.add('delete')
 productPage.classList.remove('delete')

})
deleteBtn.addEventListener('click', function(){
  alert('are you sure you want to delete all you cart items')
  empty.classList.remove('delete')
  items.classList.add('delete')
})
item.addEventListener('click', (e)=>{
  console.log(item.classList.contains(2))
})
