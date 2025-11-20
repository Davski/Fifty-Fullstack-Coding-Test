const BASE_URL = 'http://localhost:8000/api'

async function registerUser() {
    try {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value.trim();
        const email = document.getElementById('email').value.trim();
	const responseData = document.getElementById('responseData');
	if (!username || !password || !email) {
	    responseData.innerHTML = `There are empty fields`;
	    return;
	}
	const response = await fetch(`${BASE_URL}/register-user`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
		username,
		password,
		email})
        });
        if (!response.ok) {
	    const error = await response.json();
	    if (response.status == 422) {
		throw new Error(`${error.detail[0].msg}`);
	    }
	    throw new Error(`Can't register user: ${error.detail}`);
        }
        const result = await response.json();
        responseData.innerHTML = `User created: ${result.username}<br>email: ${result.email}`;
    } catch (error) {
	responseData.innerHTML = `Error: ${error.message}`;
    }
}

async function loginUser() {
    try {
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();
        const response = await fetch(`${BASE_URL}/login-user`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({username, password})
        });
        if (!response.ok) {              
	    const error = await response.json();
	    throw new Error(`Can't login: ${error.detail}`);
        }
        const responseData = document.getElementById('responseData');
	const result = await response.json();
	responseData.innerHTML = `Access: ${result.access}<br>Refresh: ${result.refresh}`;
    } catch (error) {
	responseData.innerHTML = `Error: ${error.message}`;
    }
}

async function getReadings() {
    try {
        const response = await fetch(`${BASE_URL}/readings`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        if (!response.ok) {
	    const error = await response.json();
            throw new Error(`Can't get readings: ${error.detail}`);
        }
        const result = await response.json();
	const responseData = document.getElementById('responseData');
	responseData.innerHTML = '';
	for (let i = 0; i < 10; i++) {
	    responseData.innerHTML +=
		`Sensor: ${result[i].sensor}: Temperature: ${result[i].temperature}: Humidity: ${result[i].humidity}: Timestamp: ${result[i].timestamp}<br>`;
	}
    } catch (error) {
	responseData.innerHTML = `Error: ${error.message}`;
    }
}
