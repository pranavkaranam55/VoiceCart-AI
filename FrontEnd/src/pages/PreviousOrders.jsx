import OrderTable from "../components/OrderTable";

function PreviousOrders() {
  return (
    <div className="previous-orders">

      <h1>Previous Orders</h1>

      <div className="filters">

        <button>Today</button>
        <button>This Week</button>
        <button>This Month</button>

      </div>

      <OrderTable />

    </div>
  );
}

export default PreviousOrders;