sse = new EventSource('/sseColor');
sse.onmessage = function(message) {
	data = JSON.parse(message.data);
	$('#fix0').spectrum("set", data.fix0);
	$('#fix1').spectrum("set", data.fix1);
	$('#fix2').spectrum("set", data.fix2);
	$('#fix3').spectrum("set", data.fix3);
	$('#fix4').spectrum("set", data.fix4);
	$('#fix5').spectrum("set", data.fix5);
};

sseAudio = new EventSource('/sseBlu');
sseAudio.onmessage = function(message) {
	data = JSON.parse(message.data);
	document.querySelector('#backstageFader').value = data.backstage;
};
