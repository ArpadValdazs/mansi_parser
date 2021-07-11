import {link} from './config.js'

$("document").ready(function(){
	let response = fetch(link+ '/get_text', {
			method: 'GET',
			mode: 'no-cors',
			headers: {
				'Access-Control-Allow-Origin':'*',
				'Content-Type': 'json'
			},
		}).then(response => {
			response.json().then((data)=> {
				console.log(data["response"])
				let selector = document.getElementById("fileList")
				for (let i = 0; i < data["response"].length; i++){
					let j = i+1
					selector.insertAdjacentHTML("beforeend", '<option value = "'+j+'">'+data["response"][i]+'</option>')
				}
			})
		})
})

$("document").ready(function(){
	console.log("ss")
	let response = fetch(link+ '/get_temps', {
			method: 'GET',
			mode: 'no-cors',
			headers: {
				'Access-Control-Allow-Origin':'*',
				'Content-Type': 'json'
			},
		}).then(response => {
			response.json().then((data)=> {
				console.log(data["response"])
				let selector = document.getElementById("tempList")
				for (let i = 0; i < data["response"].length; i++){
					let j = i+1
					selector.insertAdjacentHTML("beforeend", '<option value = "'+j+'">'+data["response"][i]+'</option>')
				}
			})
		})
})