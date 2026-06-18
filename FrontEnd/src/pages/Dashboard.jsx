import { useEffect, useState } from "react";
import StatsCard from "../components/StatsCard";

function Dashboard() {

  const [stats, setStats] = useState({
    today_orders: 0,
    live_orders: 0,
    delivered_orders: 0,
    revenue: 0
  });

  useEffect(() => {

    fetch("http://127.0.0.1:8000/dashboard")
      .then((response) => response.json())
      .then((data) => setStats(data))
      .catch((error) => console.error(error));

  }, []);

  return (
    <div className="dashboard">

      <h1>Dashboard</h1>

      <div className="stats-grid">

        <StatsCard
          title="Today's Orders"
          value={stats.today_orders}
        />

        <StatsCard
          title="Live Orders"
          value={stats.live_orders}
        />

        <StatsCard
          title="Delivered Orders"
          value={stats.delivered_orders}
        />

        <StatsCard
          title="Revenue Today"
          value={`₹${stats.revenue}`}
        />

      </div>

    </div>
  );
}

export default Dashboard;