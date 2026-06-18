import { Link } from "react-router-dom";
import { API_URL } from "../config";
function HeroSection() {
    return (
      <section className="hero">
  
        <h1>VoiceCart AI</h1>
  
        <h2>Speak. Order. Simplify.</h2>
  
        <p>For modern retail businesses.</p>
  
        <div className="hero-buttons">

  <Link to="/voice-console">
    <button className="primary-btn">
      Start Recording
    </button>
  </Link>

  <Link to="/dashboard">
    <button className="secondary-btn">
      Open Dashboard
    </button>
  </Link>

</div>
  
      </section>
    );
  }
  
  export default HeroSection;