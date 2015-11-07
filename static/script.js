var getStats = function(){
	//location.reload(true)	

	// SERVERS is decleared in the template "index"

	// send ajax request for each server
	for (var i = 0; i< SERVERS.length; i++){
		var data = {
			"ip":SERVERS[i][0],
			"port":SERVERS[i][1]
		};
		
		$.ajax({
			type:"POST",
			url: "/getStats",
			data: JSON.stringify(data),//JSON.stringify("request":"Sindre"),
			dataType: "json",
			contentType: 'application/json;charset=UTF-8',
			success: function(response) {
				console.log("RESPONSE!!!:", response);
			},
			error: function(error) {
				console.log(error)
			}
		});
	};
};

$(document).ready(function(){
	var time = setInterval(getStats(),2000)
})
