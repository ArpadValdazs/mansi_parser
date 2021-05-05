let initialValues = []
let startValues = []
let indexes = []

parser = function(fetchedData){
	let items = []
	$.each(fetchedData, function (key, val){
		//key - number of sentence
		$("#tbody").append("<tr id="+key+"></tr>")
		$("#"+key).append("<td id="+key+'td'+">"+key+"</td>")
		$("#"+key).append("<td id="+key+'button'+"><button id=reparse>reparse</button></td>")
		$.each(val[0], function (key1, val1){
			//key1 - displays "gramm" or "trans" strings
			$("#"+key).append("<td id="+key+'_'+key1+"></td>")
			$.each(val1, function (key2, val2){
				//key2 - displays all the objects with compounds key2: {compound}
				$.each(val2, function (key3, val3){
					if(val3.length===1){
						$.each(val3, function (key4, val4) {
							$.each(val4, function (key5, val5) {
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
								$("#"+key+"_"+key1+"_"+key3).append("<option>"+val5+"</option>")
							})
						})
					}
				})
			})
		})
	})
	// Вносим данные, чтобы потом при парсинге отдельных строк сравнивать, и отправлять
	// только те значения, которые необходимы, и затем встраивать их обратно
	let data = gatherData()
	initialValues.push(data)
	startValues.push(data)
}

$("#save").click(function(){
	let filename = document.getElementById("exportName").value
	console.log(filename)
	let data = gatherData()
	let obj = {}
	for (let row = 0; row < data.length; row++){
		console.log(row)
		let elem = []
		elem.push([data[row][0].join(' ')])
		elem.push([data[row][1].join(' ')])
		console.log(elem);
		obj[row] = elem
	}
	obj["filename"] = filename
	let json = JSON.stringify(obj)
	saver(json)
})

// Собирает информацию со всей таблицы
let gatherData = function (){
	let table = $("#tbody").children()
	let tableData = []
	for (let row of table){
		array = collectRow(row.childNodes[0].innerHTML)
		tableData.push(array)
	}
	return tableData
}

let collectRow = function(num){
	let grammString = num+'_gramm'
    let transString = num+'_trans'
	let grammArray = []
	let transArray = []
	let grammtable = document.getElementById(grammString).childNodes
	let transtable = document.getElementById(transString).childNodes
	//console.log('grammtable: ', grammtable)
	for (let node of grammtable){
		if (node.nodeName === 'DIV') {
			grammArray.push(node.innerText)
		}
		if (node.nodeName === 'SELECT') {
			grammArray.push(node.value)
		}
	}
	for (let node of transtable){
		if (node.nodeName === 'DIV') {
			transArray.push(node.innerText)
		}
		if (node.nodeName === 'SELECT') {
			transArray.push(node.value)
		}
		if (node.nodeName === 'INPUT') {
			transArray.push(node.value)
		}
	}
	return [grammArray,transArray]
}

$("body").on('click', '#reparse', function(event){
	let num = this.parentElement.id[0]
	let arrayToSend = collectRow(num)
	//console.log("ARRAY", arrayToSend)
	reparse(arrayToSend, num)
	//дальше надо через async await зафигарить отправку
})

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
			console.log("ЁВТАТАНО ПОЗДОРОВТ!")
		});
	})
}

let reparse = async function(arrayToSend, num){
	let obj = {}
	let j = 0
	arrayToSend[0]
	for (let i = 0; i<initialValues[0][num][0].length; i++){
		if (initialValues[0][num][0][i] !== arrayToSend[0][i]){
			indexes.push(i)
			obj[j]=arrayToSend[0][i].replace(/<[^>]+>/g, '').trim()
			j = j + 1
		}
	}
	//console.log(obj)

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
				console.log(sentence[indexes[i]])
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