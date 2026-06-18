import { useEffect, useState } from "react";
import AnalyticsCard from "../components/AnalyticsCard";
import ProductChart from "../components/ProductChart";

function Analytics() {

  const [analytics, setAnalytics] = useState({
    highest_selling_item: "",
    top_products: "",
    average_orders_per_day: "",
    weekly_sales: ""
  });

  useEffect(() => {

    fetch("http://127.0.0.1:8000/analytics")
      .then((response) => response.json())
      .then((data) => setAnalytics(data))
      .catch((error) => console.error(error));

  }, []);

  return (

    <div className="analytics">

      <h1>Analytics</h1>

      <div className="analytics-grid">

        <AnalyticsCard
          title="Highest Selling Item"
          value={analytics.highest_selling_item}
        />

        <AnalyticsCard
          title="Top Products"
          value={analytics.top_products}
        />

        <AnalyticsCard
          title="Average Orders Per Day"
          value={analytics.average_orders_per_day}
        />

        <AnalyticsCard
          title="Weekly Sales"
          value={analytics.weekly_sales}
        />

      </div>

      <ProductChart />

    </div>

  );
}

export default Analytics;