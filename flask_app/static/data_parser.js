let initialValues = []
let startValues = []
let indexes = []

parser = function(fetchedData, rowKey = null){
	console.log("FETHCED", fetchedData)
	let items = []
	if (rowKey !== null){
		let obj = {}
		obj[rowKey] = fetchedData[0]
		// fetchedData.key = rowKey

		//console.log(fetchedData)
		//console.log("rowkey ", obj)
		//console.log("keys ", Object.keys(fetchedData))
		fetchedData = obj
		// console.log("value ", Object.value(fetchedData))
	}
	$.each(fetchedData, function (key, val){
	    //console.log(val)
		if (rowKey !== null){
			let initKey = key
			// как-то нужно заменить ключ
			$("#"+key+"_gramm").remove()
			$("#"+key+"_trans").remove()
			$("#"+key+"_button").remove()
			$("#"+key+"_comment").remove()
			key = initKey
		} else {
			$("#tbody").append("<tr id="+key+"></tr>")
			$("#"+key).append("<td id="+key+'td'+">"+key+"</td>")
			$("#"+key).append("<td id="+key+"><button id=reparse>reparse</button></td>")
		}
		//console.log("KEY ", key)
		//key - number of sentence
		$.each(val[0], function (key1, val1){
			//key1 - displays "gramm" or "trans" strings
            //console.log(key, " ", key1)

            //console.log($("#"+key)[0].nodeName)
            //console.log($("#"+key)[0])
            $("#"+key).append("<td id="+key+'_'+key1+"></td>")
            //console.log($("#"+key+'_'+key1))
			$.each(val1, function (key2, val2){
				//key2 - displays all the objects with compounds key2: {compound}
				$.each(val2, function (key3, val3){
					if(val3.length===1){
						$.each(val3, function (key4, val4) {
							$.each(val4, function (key5, val5) {
								//console.log("key ", key, "key1 ", key1, "val5 ", val5)
								if(val5.indexOf("(??)")+1){
									val5 = val5.substr(0, val5.length-4)
									$("#"+key+"_"+key1).append('<div class = "text_block" id = "text_block" contenteditable="true"><span class = "notfound">'+val5+'</span></div>')

								} else {
									$("#"+key+"_"+key1).append('<div class = "text_block" id = "text_block" contenteditable="true">'+val5+'</div>')
								}

							})
						})
					}
					if(val3.length>1){

						$("#"+key+"_"+key1).append("<select id="+key+"_"+key1+"_"+key3+"></select>")
						$.each(val3, function (key4, val4) {
							$.each(val4, function (key5, val5) {
								//console.log("key ", key, "key1 ", key1, "val5 ", val5)
								$("#"+key+"_"+key1+"_"+key3).append("<option>"+val5+"</option>")
							})
						})
					}
				})
			})

			
		})
		$("#"+key).append('<td id='+key+'_comment><div class = "comment_block" id = "comment_block" contenteditable="true"></td>')
		$("#"+key).append("<td id="+key+"_button><button id=reparseHard>reparse hard!</button></td>")
	})
	// Вносим данные, чтобы потом при парсинге отдельных строк сравнивать, и отправлять
	// только те значения, которые необходимы, и затем встраивать их обратно
	// if($("head").children("meta[name=description]").length > 0){
	// 	$("meta[name=description]").remove()
	// }
	// let mode = $("#mode").val()
	// let text = $("#filename").val()
	// let toMeta = "mode: "+ mode+"filename: " + text
	// let meta_array = []
	// meta_array.push('<meta name = "description" content = "')
	// 	meta_array.push(toMeta)
	// meta_array.push('">')
	// let meta = meta_array.join('')
	// $("head").append(meta)
	let data = gatherData()
    console.log("INITIAL: ", data)
	initialValues.push(data)
	startValues.push(data)
}

document.querySelector("select").addEventListener('change', function (e){
	console.log(e.target.value)
})

$("#save").click(function(){
	if(confirm('Сохранить изменения?')){
		let filename = document.getElementById("exportName").value
		//console.log(filename)
		let data = gatherData()
		let obj = {}
		for (let row = 0; row < data.length; row++){
			console.log(row)
			console.log(data[row][2])
			let elem = []
			for (let i = 0; i < 2; i++){
				elem.push([data[row][i].join(' ')])
			}
			elem.push([data[row][2]])
			console.log("elem: ", elem);
			obj[row] = elem
		}
		obj["filename"] = filename
		let json = JSON.stringify(obj)
		saver(json)
	} else {
	}

})

// Собирает информацию со всей таблицы
let gatherData = function (){
	let table = $("#tbody").children()
	let tableData = []
	for (let row of table){
		let array = collectRow(row.childNodes[0].innerHTML)
		tableData.push(array)
	}
	console.log(tableData)
	return tableData
}

let collectRow = function(num){
	let grammString = num+'_gramm'
    let transString = num+'_trans'
	let grammArray = []
	let transArray = []
	let grammtable = document.getElementById(grammString).childNodes
	let transtable = document.getElementById(transString).childNodes
	let comment = document.getElementById(num+"_comment").innerText
	// console.log('comment: ', comment)
	for (let node of grammtable){
		if (node.nodeName === 'DIV') {
			grammArray.push(node.innerText.replace(/^(?=\n)$|^\s*|\s*$|\n\n + /gm, ""))
		}
		if (node.nodeName === 'SELECT') {
			// if (mode === "createTable"){
				grammArray.push(node.value)
			// }
		}
	}
	for (let node of transtable){
		if (node.nodeName === 'DIV') {
			transArray.push(node.innerText.replace(/^(?=\n)$|^\s*|\s*$|\n\n + /gm, ""))
		}
		if (node.nodeName === 'SELECT') {
			// if (mode === "createTable"){
				transArray.push(node.value)
			// }
		}
	}
	//console.log(grammArray, transArray)
	return [grammArray, transArray, comment]
}

$("body").on('click', '#reparse', function(event){
	let num = this.parentElement.id
	//console.log("num ", num)
	//console.log("num ", this.parentElement)
	let arrayToSend = collectRow(num)
	let newArray = []
	// this.parentElement[num]
	//
	for (let i = 0; i < arrayToSend[0].length; i++){
		let grammElem = document.getElementById(num+"_gramm").childNodes[i].nodeName
		//console.log(grammElem)
		if(grammElem === 'SELECT'){
			arrayToSend[0][i] = initialValues[0][num][0][i]
		}
	}
	//console.log(newArray)
	reparse(arrayToSend, num)
	//дальше надо через async await зафигарить отправку
}).on('click', "#reparseHard", function (event){
	if(confirm('Ты уверен, что хочешь перепарсить строку?')){
		//console.log(event.target.parentElement.parentElement.id)
		//let meta = document.querySelector("meta[name=description]").content
		//let meta_array = meta.split(" ")
		//let sendo = JSON.stringify({"number": event.target.parentElement.parentElement.id, "mode": meta_array[1]})
		let sendo = JSON.stringify({"number": event.target.parentElement.parentElement.id})
		let response = fetch('http://127.0.0.1:5000/reparse_hard', {
			method: 'POST',
			mode: 'no-cors',
			headers: {
				'Access-Control-Allow-Origin':'*',
				'Content-Type': 'json'
			},
			body: sendo
		}).then(response => {
			response.json().then((data) => {
				parser(data, event.target.parentElement.parentElement.id)
				console.log("joo")
			});
		})

	} else {

	}
})

$(document).on('click', function(event){
	if(event.target.tagName === 'SELECT' && event.target.id !== "mode"){
		event.target.addEventListener("change", function (){
			for(let i = 0; i < event.target.childNodes.length; i++){
				event.target.childNodes[i].id = ""
			}
			if(event.target.childNodes)
				event.target.childNodes[event.target.selectedIndex].id = event.target.selectedIndex + "_checked"
		})
	}

	// const selector = document.getElementById("select")
	// selector.setAttribute("id", event.target.selectedIndex)
	//дальше надо через async await зафигарить отправку
})
document.addEventListener('keydown', function (event){
	if(event.code === 'KeyR' && event.ctrlKey){
		event.preventDefault()
		if(confirm("Вы уверены, что хотите обновить страницу?")){
			window.location.reload()
		}
	}
	if(event.code === "F5"){
			if (!event.ctrlKey){
				if(confirm("Вы уверены, что хотите обновить страницу?")){
				event.preventDefault()
				window.location.reload()
			}
		}
		if (event.ctrlKey){
			if(confirm("Вы уверены, что хотите обновить страницу?")){
				location.reload(true)
			}
		}
	}
})
/*
window.onbeforeunload = function (e) {
	let e = e || window.event;
	if (e) {
		alert("Мāкыӈгысь таӈхēгын кон-минуӈкве?! Пуссын хот-ёрувлаве тах")
	}
}
*/
let saver = async function(jsonToSend){
	let response = await fetch('http://127.0.0.1:5000/saver', {
		method: 'POST',
		mode: 'no-cors',
		headers: {
			'Access-Control-Allow-Origin':'*',
			'Content-Type': 'json'
		},
		body: jsonToSend
	}).then(response => {
		console.log(response)
		response.json().then((data) => {
			alert(data["success"])
		});
	})
}

let reparse = async function(arrayToSend, num){
	let obj = {}
	let j = 0
	console.log(arrayToSend)
	console.log(initialValues[0][num][0])
	for (let i = 0; i<initialValues[0][num][0].length; i++){
		if (initialValues[0][num][0][i] !== arrayToSend[0][i]){
			indexes.push(i)
			obj[j]=arrayToSend[0][i].replace(/<[^>]+>/g, '').trim()
			j = j + 1
		}
	}
	console.log("meta", document.querySelector("meta").content)
	//obj["mode"]
	console.log(arrayToSend)
	console.log('obj ',obj)

	let sendo = JSON.stringify(obj)
	let response = await fetch('http://127.0.0.1:5000/sentence', {
		method: 'POST',
		mode: 'no-cors',
		headers: {
			'Access-Control-Allow-Origin':'*',
			'Content-Type': 'json'
		},
		body: sendo
	}).then(response => {
		response.json().then((data) => {
			inputData(data, num)
		});
	})
}

let inputData = function (data, num){
	let row = document.getElementById(num).childNodes
	let gramm = []
	let trans = []
	$.each(data, function (key, val){
		$.each(val[0], function (key1, val1){
			if (key1 === "gramm"){
				for (let i = 0; i<val1.length; i++){
					$.each(val1[i], function (key2, val2){
						if (val2.length===1){
							$.each(val2, function (key3, val3){
								$.each(val3, function (key4, val4){
									gramm.push([val4])
								})
							})
						} else {
							let omonyms = []
							$.each(val2, function (key3, val3){
								$.each(val3, function (key4, val4){
									omonyms.push(val4)
								})
							})
							gramm.push(omonyms)
						}
					})
				}
			} if (key1 === "trans"){
				for (let i = 0; i<val1.length; i++){
					$.each(val1[i], function (key2, val2){
						if (val2.length===1){
							$.each(val2, function (key3, val3){
								$.each(val3, function (key4, val4){
									trans.push([val4])
								})
							})
						} else {
							let omonyms = []
							$.each(val2, function (key3, val3){
								$.each(val3, function (key4, val4){
									omonyms.push(val4)
								})
							})
							trans.push(omonyms)
						}
					})
				}
			}
		})
	})
	for (let node of row){
		//console.log("for", node)
		if (node.id === num+'_gramm') {
			let sentence = node.childNodes
			for (let i = 0; i<indexes.length; i++){
				console.log("index: ", indexes, "gramm: ", gramm)
				if(gramm[i].length===1){
					sentence[indexes[i]].innerHTML = gramm[i][0]
				} else {
					const newSelector = document.createElement("select")
					newSelector.setAttribute("id", num+"_gramm_compound"+indexes[i])
					sentence[indexes[i]].replaceWith(newSelector)
					let selector = document.getElementById(num+"_gramm_compound"+indexes[i])
					for (let j = 0; j < gramm[i].length; j++){
						selector.insertAdjacentHTML("beforeend", "<option>"+gramm[i][j]+"</option>")
					}
				}
			}
		} if(node.id === num+'_trans') {
			let sentence = node.childNodes
			for (let i = 0; i<indexes.length; i++){
				//console.log(sentence[indexes[i]])
				if(trans[i].length===1){
					if(trans[i][0].indexOf("(??)")+1){
						let string = trans[i][0].substr(0, trans[i][0].length-4)
						sentence[indexes[i]].innerHTML = '<span class="notfound">'+string+'</span>'
					} else {
						sentence[indexes[i]].innerHTML = trans[i][0]
					}

				} else {
					const newSelector = document.createElement("select")
					newSelector.setAttribute("id", num+"_trans_compound"+indexes[i])
					sentence[indexes[i]].replaceWith(newSelector)
					let selector = document.getElementById(num+"_trans_compound"+indexes[i])
					for (let j = 0; j < trans[i].length; j++){
						selector.insertAdjacentHTML("beforeend", "<option>"+trans[i][j]+"</option>")
					}
				}}
			}
		if (node.id === num+'_trans') {
			let word = node.childNodes
			//console.log("if2", word)
		}
		}
	let new_data = gatherData()
	initialValues=[]
	indexes = []
	initialValues.push(new_data)
	gramm = []
	trans = []
}



let formRequest = async function(){
	let mode = $("#mode").val()
	let text = $("#filename").val()
	//console.log(text)
	if (text==="") {
		alert("Ты не ввёл имя файла!")
		return;
	}
	if($("head").children("meta[name=description]").length > 0){
		$("meta[name=description]").remove()
	}
	let elem = text.split("\\")
	let sendo = JSON.stringify({
		"parse_mode": mode,
		"text": elem[2]
	})
	//console.log("INFO ", sendo)
	let response = await fetch('http://127.0.0.1:5000/parse', {
		method: 'POST',
		mode: 'no-cors',
		headers: {
			'Access-Control-Allow-Origin':'*',
			'Content-Type': 'json'
		},
		body: sendo
	}).then(response => {
		response.json().then((data) => {
			//console.log(data)
			parser(data)
			$("head").append("<meta name=description content='mode: "+mode+" filename: "+text+"'>")
		});
	})

}


// отправка данных парсеру
$("#parse_file").submit(function(event){
	//console.log(initialValues)
	if (initialValues.length === 0) {
		event.preventDefault()
		formRequest()
	} else {
		if(confirm('Ты уверен, что хочешь всё заново перепарсить?!')){
			event.preventDefault()
			$('#tbody').remove()
			$('table').append('<tbody id="tbody"></tbody>')
			formRequest()
		} else {
			event.preventDefault()
		}
	}
})

$("#save_temp").click(async function (event){
	if(confirm('Сохранить изменения во ВРЕМЕННЫЙ ФАЙЛ?')){
		let table = document.getElementById('main').innerHTML
		let meta = document.querySelector('meta[name="description"]').content
		console.log(meta)
		let fileName = document.getElementById('tempName').value
		//console.log(table.toString())
		let sendo = JSON.stringify({"text": meta+table.toString(), "filename": fileName+".html"})
		let response = await fetch('http://127.0.0.1:5000/create_temp', {
			method: 'POST',
			mode: 'no-cors',
			headers: {
				'Access-Control-Allow-Origin':'*',
				'Content-Type': 'json'
			},
			body: sendo
		}).then(response => {
			response.json().then((data) => {
				console.log(data["response"])
				alert(data["response"])
			});
		})
	} else {
	}

})

$("#open_temp").click(function (event){
	event.target.addEventListener("change", async function (){
		let elem = event.target.value.split("\\")
		let sendo = JSON.stringify({
			"filename": elem[2]
		})
		console.log(sendo)
		//console.log(event.target.value)
		let response = await fetch('http://127.0.0.1:5000/get_file', {
			method: 'POST',
			mode: 'no-cors',
			headers: {
				'Access-Control-Allow-Origin':'*',
				'Content-Type': 'json'
			},
			body: sendo
		}).then(response => {
			response.text().then((arrived_data) => {
				console.log(arrived_data.indexOf("<"))
				let data_array = []
				let meta_array = []
				for (let i = arrived_data.indexOf("<"); i < arrived_data.length; i++){
					data_array.push(arrived_data[i])
				}
				meta_array.push('<meta name = "description" content = "')
				for (let i = 0; i < arrived_data.indexOf("<"); i++){
					meta_array.push(arrived_data[i])
				}
				meta_array.push('">')
				let data = data_array.join('')
				let meta = meta_array.join('')
				$("head").append(meta)

				console.log(data)
				console.log(meta)
				$("main").empty().append(data)
				//$("main")
				let selector = document.getElementsByTagName('select')
				for (let i = 1; i < selector.length; i++) {
					for(let j = 0; j < selector[i].length; j++) {
						if(selector[i].childNodes[j].id !== ""){
							selector[i].value = selector[i].childNodes[j].innerText
							selector[i].childNodes[j]
						}
					}
				}
				let new_data = gatherData()
				initialValues.push(new_data)
				console.log(new_data)
			});
		})
	}, {once: true})

})