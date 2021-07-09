$("#login").submit(async function(event){
	event.preventDefault()
	console.log(event)
	let name = $("#text").val()
	let password = $("#password").val()
	console.log(name)
	console.log(password)
	let toSend = JSON.stringify({
		"name": name,
		"password" : password
	})
	console.log(toSend)
	let response = await fetch('http://127.0.0.1:5000/auth', {
		method: 'POST',
		mode: 'no-cors',
		headers: {
			'Access-Control-Allow-Origin':'*',
			'Content-Type': 'json'
		},
		body: toSend
	}).then(response => {
		response.json().then((data) =>{
			if (data.redirect) {
				window.location.href = data.redirect
			} else {
				alert(data["Error"])
			}
		})
	})
})