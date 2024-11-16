const roomName = JSON.parse(document.getElementById("room-name").textContent);
const conversation = document.getElementById("conversation");
console.log(roomName);
const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
);
const sendButton = document.querySelector("#send");
const messageInput = document.querySelector("#sendMessage");

chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  //document.querySelector("#chat-log").value += data.message + "\n";
  var message = `
    <div class="oldMessages">
      <div class="avatar">A</div>
      <div class="content">
        <div class="headline">Ahmet Yılmaz</div>
        <div class="message" id="chatLog">
          ${data.message}
        </div>
      </div>
    </div>`;
  conversation.innerHTML += message;
};

chatSocket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};

messageInput.focus();
messageInput.onkeyup = function (e) {
  if (e.keyCode === 13) {
    sendButton.click();
  }
};

sendButton.onclick = function (e) {
  const message = messageInput.value;
  console.log("Deneme" + message);
  chatSocket.send(JSON.stringify({ message: message }));
  messageInput.value = "";
};
