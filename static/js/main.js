const roomName = JSON.parse(document.getElementById("room-name").textContent);
const conversation = document.getElementById("conversation");

const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
);

const currentUser = JSON.parse(document.getElementById("user").textContent);
//const currentuser = JSON.getElementById("user").textContent;

const sendButton = document.querySelector("#send");
const messageInput = document.querySelector("#sendMessage");

chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  console.log(roomName);
  console.log("Gönderen Kişi " + data.user + " Alan Kişi: " + currentUser);
  //document.querySelector("#chat-log").value += data.message + "\n";
  if (currentUser == data.user) {
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
  } else {
    var message = `
    <div class="mySelf">
      <div class="avatar">A</div>
      <div class="content">
        <div class="headline">Ahmet Yılmaz</div>
        <div class="message" id="chatLog">
          ${data.message}
        </div>
      </div>
    </div>`;
  }
  conversation.innerHTML += message;

  chatSocket.onclose = function (e) {
    console.error("Chat socket closed unexpectedly");
  };
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
