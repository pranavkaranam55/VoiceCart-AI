import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">

      <div className="logo">
        VoiceCart AI
      </div>

      <div className="nav-links">

        <Link to="/">Home</Link>

        <Link to="/dashboard">Dashboard</Link>

        <Link to="/analytics">Analytics</Link>

        <Link to="/orders">Previous Orders</Link>

        <Link to="/voice-console">Voice Console</Link>
        <Link to="/prediction">
  Prediction
</Link>

      </div>

    </nav>
  );
}

export default Navbar;