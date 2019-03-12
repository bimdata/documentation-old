let socket = new WebSocket('ws://localhost:8080');

socket.onmessage = function incoming(data) {
  location.reload();
};
socket.onclose = e => {
  console.error("Chat socket closed unexpectedly", e);
};
