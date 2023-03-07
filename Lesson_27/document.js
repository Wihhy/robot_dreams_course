// creating buttons
const buttonsDiv = document.createElement('div');
buttonsDiv.className = 'buttons';
buttonsDiv.style.textAlign = 'center';

let friends = Math.floor(Math.random() * 101);
document.getElementById("friends").textContent = `Кількість друзів: ${friends}`;

['Додати в друзі', 'Написати повідомлення', 'Запропонувати роботу'].map(buttonName => {
    let button = document.createElement('button');
    button.className = 'btn btn-success';
    button.innerText = buttonName;
    button.style.margin = '10px';
    buttonsDiv.appendChild(button);
})

document.getElementsByTagName('body')[0].appendChild(buttonsDiv);

// events
const addFriendButton = document.getElementsByTagName("button")[0];
addFriendButton.addEventListener('click', (event) => {
    ++friends;
    event.target.style.background = 'grey';
    event.target.disabled =true;
    event.target.innerText = 'Очікується підтвердження';
    document.getElementById("friends").textContent = `Кількість друзів: ${friends}`;
    console.log(friends);
});

















