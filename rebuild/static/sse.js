// sseFix0 = new EventSource('/sse/fix0');
// sseFix0.onmessage = function(message) {
// 	$('#fix0').spectrum("set", message.data);
// };

// sseFix1 = new EventSource('/sse/fix1');
// sseFix1.onmessage = function(message) {
// 	$('#fix1').spectrum("set", message.data);
// };

// sseFix2 = new EventSource('/sse/fix2');
// sseFix2.onmessage = function(message) {
// 	$('#fix2').spectrum("set", message.data);
// };

// sseFix3 = new EventSource('/sse/fix3');
// sseFix3.onmessage = function(message) {
// 	$('#fix3').spectrum("set", message.data);
// };

// sseFix4 = new EventSource('/sse/fix4');
// sseFix4.onmessage = function(message) {
// 	$('#fix4').spectrum("set", message.data);
// };

// sseFix5 = new EventSource('/sse/fix5');
// sseFix5.onmessage = function(message) {
// 	$('#fix5').spectrum("set", message.data);
// };

sse = new EventSource('/sse');
sse.addEventListener("fix0", function(event) {
	$('#fix0').spectrum("set", event.data);
}, false);

sse.addEventListener("fix1", function(event) {
	$('#fix1').spectrum("set", event.data);
}, false);