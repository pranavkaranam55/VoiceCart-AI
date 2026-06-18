import { useEffect, useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

function ProductChart() {

  const [products, setProducts] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/orders")
      .then((response) => response.json())
      .then((data) => {

        const counts = {};

        data.forEach((order) => {

          if (counts[order.product]) {
            counts[order.product] += order.quantity;
          } else {
            counts[order.product] = order.quantity;
          }

        });

        const chartData = Object.entries(counts)
          .map(([product, quantity]) => ({
            product,
            quantity
          }))
          .sort((a, b) => b.quantity - a.quantity)
          .slice(0, 5);

        setProducts(chartData);

      })
      .catch((error) => console.error(error));

  }, []);

  return (

    <div className="chart-card">

      <h2>Top Products</h2>

      <ResponsiveContainer width="100%" height={350}>

        <BarChart data={products}>

          <XAxis dataKey="product" />

          <YAxis />

          <Tooltip />

          <Bar
            dataKey="quantity"
            fill="#6C63FF"
            radius={[10, 10, 0, 0]}
          />

        </BarChart>

      </ResponsiveContainer>

    </div>

  );

}

export default ProductChart;