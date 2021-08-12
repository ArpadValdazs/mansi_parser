import {link} from './config.js'

$("document").ready(function(){
	let response = fetch(link+ '/get_info', {
			method: 'GET',
			mode: 'no-cors',
			headers: {
				'Access-Control-Allow-Origin':'*',
				'Content-Type': 'json'
			},
		}).then(response => {
			response.json().then((data)=> {
				console.log(data["response"])

				let selector1 = document.getElementById("fileList")
				data["response"][0].sort();
				for (let i = 0; i < data["response"][0].length; i++){
					let j = i+1
					selector1.insertAdjacentHTML("beforeend", '<option value = "'+j+'">'+data["response"][0][i]+'</option>')
				}
				data["response"][1].sort();
				let selector2 = document.getElementById("tempList")
				for (let i = 0; i < data["response"][1].length; i++){
					let j = i+1
					selector2.insertAdjacentHTML("beforeend", '<option value = "'+j+'">'+data["response"][1][i]+'</option>')
				}
			})
		})
})/*

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
})*/