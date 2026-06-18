import { BrowserRouter, Routes, Route } from "react-router-dom";
import DemandPrediction from "./pages/DemandPrediction";

import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import Analytics from "./pages/Analytics";
import PreviousOrders from "./pages/PreviousOrders";
import VoiceConsole from "./pages/VoiceConsole";

function App() {
  return (
    <BrowserRouter>

      <Navbar />

      <Routes>

        <Route path="/" element={<Home />} />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/analytics"
          element={<Analytics />}
        />

        <Route
          path="/orders"
          element={<PreviousOrders />}
        />

<Route
  path="/voice-console"
  element={<VoiceConsole />}
/>

<Route
  path="/prediction"
  element={<DemandPrediction />}
/>

</Routes>

    </BrowserRouter>
  );
}

export default App;