var data = {
	"param": "test"
};

var getStats = function(){
	//location.reload(true)	
	$.ajax({
		type:"POST",
		url: "/test",
		data: JSON.stringify(data),//JSON.stringify("request":"Sindre"),
		dataType: "json",
		contentType: 'application/json;charset=UTF-8',
		success: function(response) {
			console.log("RESPONSE!!!:", response["response"]);
		},
		error: function(error) {
			console.log(error)
		}
	});
};

$(document).ready(function(){
	var time = setInterval(getStats(),2000)
})
