document.getElementById('dreamForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const date = document.getElementById('date').value;
  const dream = document.getElementById('dream').value;
  const messageDiv = document.getElementById('message');

  if (!date || !dream) {
    messageDiv.textContent = 'Please fill in both fields.';
    messageDiv.style.color = 'red';
    return;
  }

  fetch('/save_dream', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ date, dream })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      messageDiv.textContent = data.message;
      messageDiv.style.color = 'green';
      document.getElementById('dreamForm').reset();
    } else {
      messageDiv.textContent = data.message;
      messageDiv.style.color = 'red';
    }
  })
  .catch(error => {
    messageDiv.textContent = 'An error occurred while saving your dream.';
    messageDiv.style.color = 'red';
    console.error('Error:', error);
  });
});
