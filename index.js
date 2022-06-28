const button = document.querySelector('button');
        input = document.querySelector('input');
        button.addEventListener('click', () => sendData(input.value))
        function sendData(sender) {
            const URL = '/post';
            const xhr = new XMLHttpRequest();
            xhr.open('POST', URL);
            xhr.send(sender);
        }