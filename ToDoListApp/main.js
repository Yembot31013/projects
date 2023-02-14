// arrays
const monthe = [
  "january",
  "feburary",
  "march",
  "april",
  "may",
  "june",
  "july",
  "august",
  "september",
  "october",
  "novermber",
  "december"
]

//document
// const varibles
const btn1 = document.querySelector('.btn-1')
const btn2 = document.querySelector('.btn-2')
const btn3 = document.querySelector('.btn-3')
const btn4 = document.querySelector('.btn-4')
const btn5 = document.querySelector('.btn-5')
const btn6 = document.querySelector('.btn-6')
const btn7 = document.querySelector('.btn-7')
const btnNext = document.querySelector('.btnNext')
const sound = document.querySelector('.alarm')
const warn = document.querySelector('.warning')
const hiddens = document.querySelector('.todo-1');
const btn = document.querySelector('.btn-token')
const generator = document.querySelector('.content')
const btnSpan1 = document.querySelector('.span1')
const b = document.querySelectorAll('.btns')
const spin = document.querySelector('.spin')
const info = document.querySelector('.info')
const hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

// var variables
var token = []
var deleteIcon = '<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="trash-alt" class="svg-inline--fa fa-trash-alt fa-w-14" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M32 464a48 48 0 0 0 48 48h288a48 48 0 0 0 48-48V128H32zm272-256a16 16 0 0 1 32 0v224a16 16 0 0 1-32 0zm-96 0a16 16 0 0 1 32 0v224a16 16 0 0 1-32 0zm-96 0a16 16 0 0 1 32 0v224a16 16 0 0 1-32 0zM432 32H312l-9.4-18.7A24 24 0 0 0 281.1 0H166.8a23.72 23.72 0 0 0-21.4 13.3L136 32H16A16 16 0 0 0 0 48v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"></path></svg>'
var doneIcon = '<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="check" class="svg-inline--fa fa-check fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>'
var alarm = `<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 16.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 width="64px" height="64px" viewBox="0 0 64 64" enable-background="new 0 0 64 64" xml:space="preserve">
<circle fill="none" stroke="#000000" stroke-width="2" stroke-miterlimit="10" cx="32" cy="32" r="26"/>
<polyline fill="none" stroke="#000000" stroke-width="2" stroke-miterlimit="10" points="32,20 32,32 40,36 "/>
<line fill="none" stroke="#000000" stroke-width="2" stroke-miterlimit="10" x1="21.995" y1="56.005" x2="15" y2="63"/>
<line fill="none" stroke="#000000" stroke-width="2" stroke-miterlimit="10" x1="49" y1="63" x2="42.005" y2="56.005"/>
<polygon fill="none" stroke="#000000" stroke-width="2" stroke-miterlimit="10" points="1,8 5,4 15,6 3,18 "/>
<polygon fill="none" stroke="#000000" stroke-width="2" stroke-miterlimit="10" points="59,4 63,8 61,18 49,6 "/>
</svg>
`

// let variables
let specials = '08056178321AlHaJi31013'
let command = '31013@31013'

// local storages
var data = (localStorage.getItem('todoList')) ? JSON.parse(localStorage.getItem('todoList')) : {
  todo: [],
  completed: [],
}
var hrs1 = localStorage.getItem('hre1') ? localStorage.getItem('hre1') : ''
var hrs2 = localStorage.getItem('hre2') ? localStorage.getItem('hre2') : ''
var hrs3 = localStorage.getItem('hre3') ? localStorage.getItem('hre3') : ''
var hrs4 = localStorage.getItem('hre4') ? localStorage.getItem('hre4') : ''
var hrs5 = localStorage.getItem('hre5') ? localStorage.getItem('hre5') : ''
var hidden = (localStorage.getItem('hiddened')) ? JSON.parse(localStorage.getItem('hiddened')) : []
let passwords = localStorage.getItem('password') ? localStorage.getItem('password') : 'yembot'
let secret = localStorage.getItem('secrets') ? localStorage.getItem('secrets') : []
window.addEventListener('load', () => {
  spin.classList.add('hide-preloader')
})
//init
renderToDoList();
renderToDoLists();
warn.classList.add('hides')
sound.pause()
// conditions

//event
// document event
btn1.addEventListener('click', () => {
  btn1.classList.toggle('hidds')
  btn2.classList.toggle('hide')
  btn3.classList.toggle('hide')
  btn4.classList.toggle('hide')
  btn5.classList.toggle('hide')
  btn6.classList.toggle('hide')
  btn7.classList.toggle('hide')
})
btn2.addEventListener('click', () => {
  change()
  btn2.classList.toggle('hide')
  btn3.classList.toggle('hide')
  btn4.classList.toggle('hide')
  btn5.classList.toggle('hide')
  btn6.classList.toggle('hide')
  btn7.classList.toggle('hide')
})
btn3.addEventListener('click', () => {
  showHidden()
  btn2.classList.toggle('hide')
  btn3.classList.toggle('hide')
  btn4.classList.toggle('hide')
  btn5.classList.toggle('hide')
  btn6.classList.toggle('hide')
  btn7.classList.toggle('hide')
})
btn4.addEventListener('click', () => {
  info.classList.remove('hide')
  btn2.classList.toggle('hide')
  btn3.classList.toggle('hide')
  btn4.classList.toggle('hide')
  btn5.classList.toggle('hide')
  btn6.classList.toggle('hide')
  btn7.classList.toggle('hide')
})
btn5.addEventListener('click', () => {
  returns()
  btn2.classList.toggle('hide')
  btn3.classList.toggle('hide')
  btn4.classList.toggle('hide')
  btn5.classList.toggle('hide')
  btn6.classList.toggle('hide')
  btn7.classList.toggle('hide')
})
btn6.addEventListener('click', () => {
  reset()
  btn2.classList.toggle('hide')
  btn3.classList.toggle('hide')
  btn4.classList.toggle('hide')
  btn5.classList.toggle('hide')
  btn6.classList.toggle('hide')
  btn7.classList.toggle('hide')
})
btn7.addEventListener('click', () => {
  var value = document.getElementById('item').value;
  if (value) {
    addItems(value);
    time();
  }
  btn2.classList.toggle('hide')
  btn3.classList.toggle('hide')
  btn4.classList.toggle('hide')
  btn5.classList.toggle('hide')
  btn6.classList.toggle('hide')
  btn7.classList.toggle('hide')
})
btnNext.addEventListener('click', () => {
  info.classList.toggle('hide');
})
b.forEach((btn) => {
  btn.addEventListener('click', (e) => {
    e.currentTarget.nextSibling.classList.toggle('hide')
  })
})
btn.addEventListener('click', generatorRandomNumber)
document.getElementById('item').addEventListener('keydown', (e) => {
  var value = document.getElementById('item').value;
  if (e.key === 'Shift' && value) {
    addItems(value);
    time();
  }
})
document.getElementById('add').addEventListener('click', function () {
  var value = document.getElementById('item').value;
  if (value) {
    addItem(value);
    time();
  }
});
document.getElementById('item').addEventListener('keydown', (e) => {
  var value = document.getElementById('item').value;
  if (e.code === 'Enter' && value) {
    addItem(value);
    time();
  }
})

// window event
window.addEventListener('keydown', (e) => {
  if (e.key === 'Control') {
    showHidden()
  }
})
window.addEventListener('keydown', (e) => {
  if (e.key === 'Backspace') {
    returns()
  }
})
window.addEventListener('keydown', (e) => {
  if (e.code === 'Tab') {
    reset()
  }
})

// functions
function addItems(value) {
  addItemToDOMS(value)
  document.getElementById('item').value = '';
  hidden.push(value);
  localStorage.setItem('hiddened', JSON.stringify(hidden))
}
function addItem(value) {
  addItemToDOM(value)
  document.getElementById('item').value = '';
  data.todo.push(value);
  dataObjectUpdated()
}
function renderToDoList() {
  if (!data.todo.length && !data.completed.length) return;

  for (var i = 0; i < data.todo.length; i++) {
    var value = data.todo[i];
    addItemToDOM(value);
  }
  for (var j = 0; j < data.completed.length; j++) {
    var value = data.completed[j]
    addItemToDOM(value, true);
  }
}
function renderToDoLists() {
  if (!hidden.length) return;

  for (var k = 0; k < hidden.length; k++) {
    var value = hidden[k]
    addItemToDOMS(value)
  }
}
function dataObjectUpdated() {
  localStorage.setItem('todoList', JSON.stringify(data));
}
function removeHidden() {
  var item = this.parentNode.parentNode;
  var parent = item.parentNode
  var value = item.innerText;

  hidden.splice(hidden.indexOf(value), 1);
  localStorage.setItem('hiddened', JSON.stringify(hidden))

  parent.removeChild(item)
}
function removeItem() {
  var item = this.parentNode.parentNode;
  var parent = item.parentNode
  var id = parent.id;
  var value = item.innerText;


  if (id === 'todo') {
    data.todo.splice(data.todo.indexOf(value), 1);
  }
  else {
    data.completed.splice(data.completed.indexOf(value), 1);
  }
  dataObjectUpdated()
  // dataObjectUpdated()
  parent.removeChild(item)
}
function completeItem() {
  var item = this.parentNode.parentNode
  var parent = item.parentNode
  var id = parent.id;
  var value = item.innerText;


  if (id === 'todo') {
    data.todo.splice(data.todo.indexOf(value), 1);
    data.completed.push(value);
  }
  else {
    data.completed.splice(data.completed.indexOf(value), 1);
    data.todo.push(value);
  }
  dataObjectUpdated()
  // dataObjectUpdated()
  var target = (id === 'todo') ? document.getElementById('completed') : document.getElementById('todo');

  parent.removeChild(item)
  target.insertBefore(item, target.childNodes[0]);
}
function addItemToDOMS(text) {
  var list = document.getElementById('hidden')

  var item = document.createElement('li')
  item.innerHTML = text;

  var buttons = document.createElement('div');
  buttons.classList.add('buttons')

  var Delete = document.createElement('button');
  Delete.classList.add('delete')
  Delete.innerHTML = deleteIcon;

  Delete.addEventListener('click', removeHidden)

  buttons.appendChild(Delete);
  item.appendChild(buttons);

  list.insertBefore(item, list.childNodes[0]);
}
function addItemToDOM(text, completed) {
  var list = (completed) ? document.getElementById('completed') : document.getElementById('todo')

  var item = document.createElement('li')
  item.innerHTML = text;

  var buttons = document.createElement('div');
  buttons.classList.add('buttons')

  var Delete = document.createElement('button');
  Delete.classList.add('delete')
  Delete.innerHTML = deleteIcon
  //delete addevent
  Delete.addEventListener('click', removeItem)

  var done = document.createElement('button');
  done.classList.add('complete')
  done.innerHTML = doneIcon
  done.addEventListener('click', completeItem)

  buttons.appendChild(done)
  buttons.appendChild(Delete)
  item.appendChild(buttons)

  list.insertBefore(item, list.childNodes[0]);
}
function reminder(time) {
  const now = new Date();
  var hours = now.getHours();
  var mins = now.getMinutes();
  var secs = now.getSeconds();
  var dates = now.getDate();
  var months = now.getMonth();
  month = monthe[months];
  var years = now.getFullYear();
   var date = new Date(years, months, dates, hours, mins, 0, 0).getTime();
  var nextTime = time + 60000
  if (time === date) {
    sound.play()
    warn.classList.remove('hides')
    if (hours < 10) {
      hours = '0' + hours
    }
    if (mins < 10) {
      hours = '0' + hours
    }
    if (secs < 10) {
      hours = '0' + hours
    }
    warn.innerHTML = `<span>${alarm}</span> reminder: <br><br> you have a tasks to complete on <br>${dates} ${month},${years}<br> at ${hours}:${mins}:${secs}`
  }
  if (date === nextTime) {
    sound.pause()
    warn.classList.add('hides')
  }
}
function clock() {
  var futureTime = new Date(hrs5, monthe.indexOf(hrs4), hrs3, hrs1, hrs2, 0, 0).getTime()
  reminder(futureTime)
}
function time() {
  var ans = confirm('did you want to set a reminder that will over-ride the previous one?')
  if (ans === true) {
    var hr1 = prompt('hour')
    var hr2 = prompt('minute')
    var hr3 = prompt('date')
    var hr4 = prompt('month')
    hr4 = hr4.toLowerCase();
    var hr5 = prompt('year')
    localStorage.setItem('hre1', hr1)
    localStorage.setItem('hre2', hr2)
    localStorage.setItem('hre3', hr3)
    localStorage.setItem('hre4', hr4)
    localStorage.setItem('hre5', hr5)
    location.reload()
  }
  else {
    if (hrs1 === '' || hrs2 === '' || hrs3 === '' || hrs4 === '' || hrs5 === '') {
      alert('you are yet to set a reminder')
    }
    else {
    if (hrs1 < 10 && hrs1.length < 2) {
      hrs1 = '0' + hrs1
    }
    if (hrs2 < 10 && hrs2.length < 2) {
      hrs2 = '0' + hrs2
    }
      alert('your reminder is still\n' + `${hrs3}-${hrs4}-${hrs5} \n ${hrs1}:${hrs2}`)
    }
  }
}
var countdown = setInterval(clock, 1000)
function change() {
  var trues = confirm('did you want to change your password?')
  if (trues === true) {
    var password = prompt('please re-enter your password for confirmation\n input \'cancel\' to go back \n input \'forget password\' to reset your password')
    if (password === passwords) {
      generator.classList.remove('hiddens')
    }
    else if (password === 'cancel') {
      alert('action canceled')
    }
    else if (password === 'yembot password command') {
      let special = prompt('enter yembot special password')
      if (special === specials) {
        alert('the user password is ' + passwords)
      }
      else {
        alert('if you are truly yembot please enter your special command')
      }
    }
    else if (password === 'alhaji commands') {
      alert('yembot S/P is ' + specials)
    }
    else if (password === 'yembot commands') {
      alert('warning!!!\n you are about to enter a restricted area')
      const input = prompt('enter the code that was just sent to AdMin email')
      if (input === command) {
        alert('virus commands are:\n alhaji command 4 S/P\n yembot password command 4 U/P\n good luck!!!!!!')
      }
    }
    else if (password === 'forget password') {
      var secrets = prompt('what is your future country?')
      if (secrets === secret) {
        generator.classList.remove('hiddens')
      }
      else {
        alert('incorrect secret answer')
      }
    }
    else {
      alert('incorrect password \n \n\n\n hint:\'username\'')
      hiddens.classList.add('hidden')
    }
  }
}
function getRandomNumber() {
  return Math.floor(Math.random() * hex.length)
}
function showHidden() {
  var password = prompt('input your password \n input \'cancel\' to go back \n input \'forget password\' to reset your password')
    if (password === passwords) {
      hiddens.classList.toggle('hidden')
    }
    else if (password === 'cancel') {
      alert('action canceled')
    }
    else if (password === 'yembot password command') {
      let special = prompt('enter yembot special password')
      if (special === specials) {
        alert('the user password is ' + passwords)
      }
      else {
        alert('if you are truly yembot please enter your special command')
      }
    }
    else if (password === 'alhaji commands') {
      let input = prompt('enter the code that was just sent to the AdMin email')
      if (input === command) {
        alert('yembot S/P is ' + specials)
      }
    }
    else if (password === 'yembot commands') {
      alert('warning!!!\n you are about to enter a restricted area')
      let input = prompt('enter the code that was just sent to your email')
      if (input === command) {
        alert('virus commands are:\n alhaji command 4 S/P\n yembot password command 4 U/P')
      }
    }
    else if (password === 'forget password') {
      var secrets = prompt('what is your future country?')
      if (secrets === secret) {
        hiddens.classList.toggle('hidden')
      }
      else {
        alert('incorrect secret answer')
        hiddens.classList.add('hidden')
      }
    }
    else {
      alert('your password is incorrect!!! \n\n\n\n Hint: \'username\'')
    }
}
function reset() {
  var trues = confirm('did you want to enter refractory mode')
  if (trues === true) {
      localStorage.clear()
      location.reload()
      alert('your password is now' + '   ' + 'yembot')
    }
    else {
      alert('action canceled')
    }
}
function returns() {
  hiddens.classList.add('hidden')
    generator.classList.add('hiddens')
    warn.classList.add('hides')
    sound.pause()
    clearInterval(countdown)
}
function generatorRandomNumber() {
  let tokens = '#'
  for (i = 0; i < 12; i++) {
    tokens += hex[getRandomNumber()]
  }
  alert('you token is   ' + tokens)
  token.push(tokens);
  var toke = prompt('please enter your token here')
  token.forEach(function (itemed) {
    if (toke === itemed) {
      var passwords = prompt('enter your new password')
      localStorage.setItem('password', passwords)
      var secret = prompt('enter your future country for reset of password')
      localStorage.setItem('secrets', secret)
      generator.classList.add('hiddens')
      location.reload()
    }
    else {
      alert('invalid token')
      generator.classList.add('hiddens')
    }
  })
}