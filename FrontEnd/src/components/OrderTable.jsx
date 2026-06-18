import { useEffect, useState } from "react";
import { API_URL } from "../config";

function OrderTable() {

  const [orders, setOrders] = useState([]);

  useEffect(() => {

fetch(`${API_URL}/orders`)      .then((response) => response.json())
      .then((data) => setOrders(data))
      .catch((error) => console.error(error));

  }, []);

  return (

    <table className="order-table">

      <thead>

        <tr>
          <th>Product</th>
          <th>Quantity</th>
          <th>Language</th>
          <th>Status</th>
          <th>Timestamp</th>
        </tr>

      </thead>

      <tbody>

        {orders.map((order, index) => (

          <tr key={index}>

            <td>{order.product}</td>
            <td>{order.quantity}</td>
            <td>{order.language}</td>
            <td>{order.status}</td>
            <td>{order.timestamp}</td>

          </tr>

        ))}

      </tbody>

    </table>

  );

}

export default OrderTable;