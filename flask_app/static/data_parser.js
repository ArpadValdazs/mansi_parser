let initialValues = []

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
									$("#"+key+"_"+key1).append("<input value="+val5+" >")
								} else {
									$("#"+key+"_"+key1).append('<div class = "text_block" id = "text_block" contenteditable="true">'+val5+' '+'</div>')
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
	console.log(initialValues)
}
$("#save").click(function(){
	let data = gatherData()
	console.log(data)
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
	for (let node of grammtable){
		if (node.nodeName === 'DIV') {
			grammArray.push(node.innerHTML)
		}
		if (node.nodeName === 'SELECT') {
			grammArray.push(node.value)
		}
	}
	for (let node of transtable){
		if (node.nodeName === 'DIV') {
			transArray.push(node.innerHTML)
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
	console.log("ARRAY", arrayToSend)
	//дальше надо через async await зафигарить отправку
})

let fetchData = function (url, data){
	fetch(url, {
		method: 'POST',
		mode: 'no-cors',
		headers: {
			'Access-Control-Allow-Origin':'*',
			'Content-Type': 'json'
		},
		body: data
	}).then(response => {
		response.json().then((data) => {
			console.log(data)
			parser(data)
		});
	})
	return "success"
}

let formRequest = async function(){
	let mode = $("#mode").val()
	let text = $("#filename").val()
	console.log(text)
	if (text==="") {
		alert("Ты не ввёл имя файла!")
		return;
	}
	let elem = text.split("\\")
	let sendo = JSON.stringify({
		"parse_mode": mode,
		"text": elem[2]
	})
	console.log("lul ", sendo)
	let response = await fetchData('http://127.0.0.1:5000/parse', sendo)
}
// отправка данных парсеру
$("#parse_file").submit(function(event){
	console.log(initialValues)
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
		}
	}
})