const button = document.querySelector('button');
        input = document.querySelector('input');
        button.addEventListener('click', () => sendData(input.value))
        function sendData(sender) {
            if(input.value != "" && input.value != " ") {
                input.value = ""
                const URL = '/post';
                const xhr = new XMLHttpRequest();
                xhr.open('POST', URL);
                xhr.send(sender);
            }
        }

const list = document.querySelector('ul');
const data = fetch('http://34.203.247.249:5000/data')
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log()
        object = JSON.parse(data)._default;
        Object.keys(object).forEach(i => {
            const listItem = document.createElement('li');
            listItem.textContent = object[`${i}`].text;
            list.append(listItem);
        })
    });
    