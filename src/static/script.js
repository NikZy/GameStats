var addServer = function() {
	var ip = $('input[name="addIp"]').val();
	var port = $('input[name="addPort"]').val();
	SERVERS.add([ip, port]);
}
var getStats = function(){
	// SERVERS is decleared in the template "index"
	// send ajax request for each server
	for (var i = 0; i< SERVERS.length; i++){
		var data = {
			"ip":SERVERS[i][0],
			"port":SERVERS[i][1]
		};
		// query serv and updates DOM
		queryServ(i, data);

	};
	setTimeout(function(){getStats()}, 4000);

};
var queryServ = function(i, data){
	$.ajax({
			type:"POST",
			url: "/getStats",
			data: JSON.stringify(data),//JSON.stringify("request":"Sindre"),
			dataType: "json",
			contentType: 'application/json;charset=UTF-8',
			success: function(response) {

				//update DOM
				updateDOM(i, response);

			},
			error: function(error) {
				console.log(error)
			}
		});

	return true
}
var updateDOM = function(index, srv_info) {
	var index = '#' + index
	console.log(srv_info)

	// remove info
	$(index+" #sname").text("Hostname: unknown");
	$(index+" #sping").text("Ping:(");
	$(index+" #slive").text("Server is offline");
	$(index+" #smap").text("Map:(");

	// remove all players
	$(index+" #team1").find("tr:not(:nth-child(1)):not(:nth-child(2))").remove()
	$(index+" #team2").find("tr:not(:nth-child(1)):not(:nth-child(2))").remove()

	// if server is up
	if (srv_info["info"] != "false") {

		$(index+" #sname").text(srv_info["info"]["Hostname"]);
		$(index+" #sping").text("Ping: "+srv_info["info"]["Ping"])
		$(index+" #smap").text("Map: " +srv_info["info"]["Map"]);
		$(index+" #slive").text("GOTV: "+srv_info["ip"]+":"+(parseInt(srv_info["port"])+1))

		for(var i = 0; i < srv_info["teams"]["team1"].length; i++){
			$(index+" #team1 tr:last").after("<tr><td>"+srv_info['teams']['team1'][i]['Name']+"</td><td>"+srv_info['teams']['team1'][i]['Frags']+"</td></tr>")

		};
		for(var i = 0; i < srv_info["teams"]["team2"].length; i++){
			$(index+" #team2 tr:last").after("<tr><td>"+srv_info['teams']['team2'][i]['Name']+"</td><td>"+srv_info['teams']['team2'][i]['Frags']+"</td></tr>")

		};
		//$(index+" #team1 tr:last").after("<tr><td>"srv_info['teams']</td><td></td></tr>")

	}
	return true

}

$(document).ready(function(){
	//var time = setInterval(getStats(), 6000)
 $("#addServer").click(fucntion() {
	 addServer();
 });
 
	getStats();


})
