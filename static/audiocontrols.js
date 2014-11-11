function changeFader (fader, value) {
	var xmlhttp;
	xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", '/setFader/' + fader + '/' + value, true);
	xmlhttp.send();
}

function mute (fader, state) {
	var xmlhttp;
	xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", '/setMute/' + fader + '/' + state, true);
	xmlhttp.send();
}