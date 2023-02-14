var token = document.querySelector(".token")
var clicker = document.querySelector(".clicker")
var verifyBtn = document.querySelector(".verify-btn")
var title = document.querySelector(".h-title")

let confirm;
confirm = false
let token_id;

function addItemToDOMS(head, text) {
  var list = document.querySelector(".list")

  var item = document.createElement('div')
  item.classList.add('card')
  item.classList.add('bg-primary')
  item.classList.add('mb-3')
  item.classList.add('text-white')

  var items = document.createElement('div')
  items.classList.add('card-header')
  items.innerHTML = head;

  var texts = document.createElement('div')
  texts.classList.add('card-body')
  texts.innerHTML = text;

  item.appendChild(items);
  item.appendChild(texts);

  list.insertBefore(item, list.childNodes[0]);
}

addItemToDOMS("head", "text")
addItemToDOMS("head", "hello1")
token.addEventListener("keydown", (e) => {
  if (token.value.length == 8 && confirm == false){
    token_id = token.value
    clicker.click()
    $.ajax({
      method: "POST",
      url: "http://127.0.0.1:8000/api/check",
      data: {
        "token": token_id,
      },
      // datatype: "dataType",
      success: function (response) {
       console.log(response.status)
      },
      error: function (e) {
        console.log(token_id)
        console.log(e)
      }
    })
  }
  if (token.value.length > 0){
    verifyBtn.classList.remove("disabled")
  }
  else {
    if (!verifyBtn.classList.contains("disabled")) {
      verifyBtn.classList.add("disabled")
    }
  }
})

function negative(){
  token.value = ""
  title.innerText = "Enter A valid token Id at the payment session on the ransomware"
}

function positive() {
  confirm = true
  token.value = ""
  title.innerText = "Enter the Sender Id of the bitcoin for verification"
  verifyBtn.classList.remove("hidden")
  verifyBtn.classList.add("disabled")
}

function confirms() {
  $.ajax({
      method: "POST",
      url: "http://127.0.0.1:8000/api/send",
      data: {
        "token": token_id,
        "sender_id": token.value,
    },
      "Access-Control-Allow-Origin": "http://127.0.0.1:500",
      // datatype: "dataType",
      success: function (response) {
       console.log(response.status)
       token.value = ""
      },
      error: function (e) {
        Swal.fire(
         'Error',
          e.statusText,
          'warning'
        )
        token.value = ""
      }
    })
}