console.log("lul!")
$.getJSON("data_file.json", function(data){
	console.log(data)
	let items = []
	$.each(data, function (key, val){
		console.log(key, " ", val)
		$.each(val[0], function (key1, val1){
			console.log(key1, " ", val1)
			$.each(val1[0], function (key2, val2){
				console.log(key2, " ", val2)
				//$("#tbody").append("<tr id="+key2+"></tr>")
				for(let i = 0; i<val2.length; i++){
					$.each(val2[i], function (key3, val3){
						console.log(key3, " ", val3)
					})
				}

			})
		})
	})

})
$("parse_file").submit(function(){

})