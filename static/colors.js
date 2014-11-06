function changeColor(fix, value) {
var xmlhttp;
xmlhttp = new XMLHttpRequest();
xmlhttp.open("GET", '/setColor/'+ fix + '/' + value, true);
xmlhttp.send();
}


$("#fix0").spectrum({
	flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(0,color.toHex()); }
});

$("#fix1").spectrum({
	flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(1,color.toHex()); }
});

$("#fix2").spectrum({
	flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(2,color.toHex()); }
});

$("#fix3").spectrum({
	flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(3,color.toHex()); }
});

$("#fix4").spectrum({
	flat: true,
	showButtons: false,
	clickoutFiresChange: true,
	move: function(color) { changeColor(4,color.toHex()); }
});