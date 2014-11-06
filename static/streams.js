// function x(){
// 	sse = new EventSource('/stream');
// 	sse.onmessage = function(message) {
// 		document.querySelector('#fader').value = message.data;
// 		document.querySelector('#fadervalue').value = message.data;
// 	};
// };

//function getStreams() {
//	function {
		sseColor0 = new EventSource('/colorStream/0');
		sseColor0.onmessage = function(message) {
			$('#fix0').spectrum("set", message.data);
		};
//	};

//	function {
		sseColor3 = new EventSource('/colorStream/1');
		sseColor3.onmessage = function(message) {
			$('#fix1').spectrum("set", message.data);
		};
//	};

//	function {
		sseColor6 = new EventSource('/colorStream/2');
		sseColor6.onmessage = function(message) {
			$('#fix2').spectrum("set", message.data);
		};
//	};

//	function {
		sseColor9 = new EventSource('/colorStream/3');
		sseColor9.onmessage = function(message) {
			$('#fix3').spectrum("set", message.data);
		};
//	};

//	function {
		sseColor12 = new EventSource('/colorStream/4');
		sseColor12.onmessage = function(message) {
			$('#fix4').spectrum("set", message.data);
		};
//	};
//}

