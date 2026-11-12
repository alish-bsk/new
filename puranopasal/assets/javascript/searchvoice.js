document.addEventListener("DOMContentLoaded", () => {
  const voiceBtn = document.getElementById('voiceBtn');
  const searchBox = document.getElementById('searchBox');

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
      alert("Speech Recognition not supported in this browser.");
      return;
  }

  const recognition = new SpeechRecognition();
  let isListening = false;

  // Enable continuous mode for longer speech
  recognition.continuous = true;
  recognition.lang = 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  voiceBtn.addEventListener('click', () => {
      if (!isListening) {
          searchBox.value = 'Listening...';
          recognition.start();
          isListening = true;
      }
  });

  recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      searchBox.value = transcript;
      console.log("Recognized:", transcript);
      isListening = false; // Ensure this resets for the next input
      searchForm.submit(); 
              };

  recognition.onerror = (event) => {
      console.error("Error:", event.error);
      searchBox.value = `Error: ${event.error}`;
      isListening = false;
  };

  recognition.onspeechend = () => {
      // Stop the recognition process to avoid the InvalidStateError
      recognition.stop();
      isListening = false;
  };

  recognition.onend = () => {
      isListening = false;
  };
});                       
