function changeColor (fix, value) {
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", '/setColor/' + fix + '/' + value, true);
	xmlhttp.send();
};

function setDMX(channel, value) {
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", '/setDMX/' + channel + '/' + value, true);
	xmlhttp.send();
};

$("#fix0").spectrum({
	//flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(0, color.toHex()); }
});

$('#fix1').spectrum({
	//flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(1, color.toHex()); }
});

$('#fix2').spectrum({
	//flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(2, color.toHex()); }
});

$('#fix3').spectrum({
	//flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(3, color.toHex()); }
});

$('#fix4').spectrum({
	//flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(4, color.toHex()); }
});

$('#fix5').spectrum({
	//flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(5, color.toHex()); }
});

var colorCopy;

function copyColor(fixNum) {
	var fix = '#fix' + fixNum;
	colorCopy = $(fix).spectrum("get");

};

function pasteColor(fixNum) {
	var fix = '#fix' + fixNum
	$(fix).spectrum("set", colorCopy);
	changeColor(fixNum, colorCopy.toHex());
};

function allOff() {
	for (var i =0; i <= 5; i++) {
		changeColor(i, '000000');
	};
};

function allOn() {
	for (var i =0; i <= 5; i++) {
		changeColor(i, 'FFFFFF');
	};
};