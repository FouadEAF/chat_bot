function sendMessage() {
  const userInput = document.getElementById("user-input").value;
  if (!userInput) return;

  // Add user message to chat box
  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;

  // Get the CSRF token from the hidden input field
  const csrfToken = document.getElementById("csrf-token").value;

  // Send user input to backend
  fetch("/get_response/", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": csrfToken, // Include the CSRF token in the headers
    },
    body: `user_input=${encodeURIComponent(userInput)}`,
  })
    .then((response) => response.json())
    .then((data) => {
      // Add bot response to chat box
      chatBox.innerHTML += `<div><strong>Cell 2AD:</strong> ${data.response}</div>`;
      chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
    });

  // Clear input field
  document.getElementById("user-input").value = "";
}
