var getStats = function(){
	location.reload(true)	
}

$(document).ready(function(){
	var time = setInterval(getStats(),2000)
})
