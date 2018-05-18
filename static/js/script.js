
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/monitor');
    var numbers_received = [];

    //receive details from server
    socket.on('newstatus', function(msg) {
        console.log("Received number" + msg.status);
	var dataArray = JSON.parse("[" + msg.status + "]");
	if (dataArray[0] == 1){
		$('#light1').css({fill: "red"});	
	} else {
		$('#light1').css({fill: "green"});
	}
	if (dataArray[1] == 1){
		$('#light2').css({fill: "red"});	
	} else {
		$('#light2').css({fill: "green"});
	}
	if (dataArray[2] == 1){
		$('#light3').css({fill: "red"});	
	} else {
		$('#light3').css({fill: "green"});
	}
	if (dataArray[3] == 1){
		$('#light4').css({fill: "red"});	
	} else {
		$('#light4').css({fill: "green"});
	}
        //maintain a list of ten numbers
        /*if (numbers_received.length >= 10){
            numbers_received.shift()
        }            
        numbers_received.push(msg.status);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        }
        $('#log').html(numbers_string);*/
    });

});
