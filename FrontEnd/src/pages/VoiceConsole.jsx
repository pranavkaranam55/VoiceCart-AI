import { useState, useRef } from "react";
function VoiceConsole() {

  const [status, setStatus] = useState("Ready to Listen");
  const [detectedOrder, setDetectedOrder] = useState([]);  const mediaRecorderRef = useRef(null);
const audioChunksRef = useRef([]);
const startRecording = async () => {

  try {

    const stream = await navigator.mediaDevices.getUserMedia({
      audio: true
    });

    const mediaRecorder = new MediaRecorder(stream);

    mediaRecorderRef.current = mediaRecorder;
    audioChunksRef.current = [];

    mediaRecorder.ondataavailable = (event) => {
      audioChunksRef.current.push(event.data);
    };

    mediaRecorder.onstop = async () => {
      console.log("Recording stopped");

      const audioBlob = new Blob(
        audioChunksRef.current,
        { type: "audio/webm" }
      );

      const formData = new FormData();

      formData.append(
        "file",
        audioBlob,
        "recording.webm"
      );

      try {

        const response = await fetch(
          "http://127.0.0.1:8000/process-order",
          {
            method: "POST",
            body: formData
          }
        );

        const data = await response.json();
        console.log(data.transcribed_text);
console.log(data.orders);

        setDetectedOrder(data.orders);

        setStatus("Order Detected");
        

      } catch (error) {

        console.error(error);
        setStatus("Error Processing Order");

      }

    };

    mediaRecorder.start();

    setStatus("Listening...");

    setTimeout(() => {

      mediaRecorder.stop();

      setStatus("Processing Order...");

    }, 6000);

  } catch (error) {

    console.error(error);
    setStatus("Microphone access denied");

  }

};
  return (
    <div className="voice-console">

      <h1>Voice Console</h1>

      <div className="voice-card">

        <div className="record-circle">
          🎤
        </div>

        <h2>Status</h2>

        <p className="status-text">
          {status}
        </p>

        <div className="languages">

          <h3>Supported Languages</h3>

          <div className="language-grid">

            <div>English</div>
            <div>Hindi</div>
            <div>Telugu</div>
            <div>Tamil</div>
            <div>Kannada</div>
            <div>Malayalam</div>

          </div>

        </div>

        <p>
          Click the button below and start speaking naturally.
        </p>

        <button
          className="record-btn"
          onClick={startRecording}        >
          Start Recording
        </button>

        <div className="detected-order">

  <h3>Detected Order</h3>

  {
    detectedOrder.length === 0 ? (
      <p>Waiting for order...</p>
    ) : (
      detectedOrder.map((item, index) => (
        <p key={index}>
          • {item.product} × {item.quantity}
        </p>
      ))
    )
  }

</div>

      </div>

    </div>
  );
}

export default VoiceConsole;