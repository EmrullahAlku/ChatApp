const roomName = JSON.parse(document.getElementById("room-name").textContent);
const conversation = document.getElementById("conversation");

const chatSocket = new WebSocket(
  "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
);

const currentUser = JSON.parse(document.getElementById("user").textContent);

const sendButton = document.querySelector("#send");
const messageInput = document.querySelector("#sendMessage");

function scrollToBottom() {
  const chatHistory = document.querySelector(".chatHistory");
  chatHistory.scrollTop = chatHistory.scrollHeight;
}

document.addEventListener("DOMContentLoaded", function () {
  scrollToBottom();
});

chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);

  if (currentUser == data.user) {
    var message = `
    <div class="mySelf">
      <div class="content">
        <div class="headline">${data.user}</div>
        <div class="message tooltip" id="chatLog">
          <span class="tooltiptext">${data.created_at}</span>
          ${data.message}
        </div>
      </div>
      <div class="avatar">${data.user.charAt(0).toUpperCase()} </div>
    </div>`;
  } else {
    var message = `
    <div class="oldMessages">
      <div class="avatar">${data.user.charAt(0).toUpperCase()} </div>
      <div class="content">
        <div class="headline">${data.user}</div>
        <div class="message tooltip" id="chatLog">
          ${data.message}
          <span class="tooltiptext">${data.created_at}</span>
        </div>
      </div>
    </div>`;
  }
  conversation.innerHTML += message;
  scrollToBottom();
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
  chatSocket.send(JSON.stringify({ message: message }));
  messageInput.value = "";
};
