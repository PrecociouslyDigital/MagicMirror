var websocket = new WebSocket("ws://127.0.0.1:8000");
websocket.onmessage = function(message){
	var command = JSON.parse(message.data);
	handlers[command.command](command.data);
};

var handlers = {
	create: function(data){
		$("<div><div>")
		.addClass("widget")
		.html(data.html)
		.attr(data.attributes || {})
		.prop(data.properties || {})
		.css(data.style || {})
		.appendTo("body")
		.offset({
			top:data.position.y,
			left:data.position.x
		});
	}
}