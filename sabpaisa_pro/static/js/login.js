
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (e) {
        e.preventDefault(); 

        const email = document.querySelector('#username').value;
        const password = document.querySelector('#password').value;

        fetch('login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') 
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.access_token) {
                console.log('Login successful');
                localStorage.setItem('access_token', data.access_token);
                localStorage.setItem('refresh_token', data.refresh_token);
                alert('Login Successful');
            } else {
                console.log('Login failed');
                alert(data.errors.non_field_errors[0]);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}); 

/*
document.getElementById('login-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('login/', {     
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const data = await response.json(); 
            if (data.token) {
                // Save the token in localStorage or sessionStorage if needed
                localStorage.setItem('authToken', data.token);
                // Redirect to the user dashboard
                window.location.href = 'dashboard.html';    //dashboard page------------------
            }
            else {
                console.error('Error:', 'Invalid credentials');
                alert('Invalid credentials');
            }
        }  else{
                throw new Error ('network response was not ok');
            }
        }catch(error){
            console.error('Error:',error);
            alert('An error occurred.Please try again.');
        }

    });*/