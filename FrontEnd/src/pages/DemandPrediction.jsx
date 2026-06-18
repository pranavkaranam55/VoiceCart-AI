import { useEffect, useState } from "react";
import { API_URL } from "../config";

function DemandPrediction() {

  const [predictions, setPredictions] = useState([]);

  useEffect(() => {

fetch(`${API_URL}/prediction`)      .then((response) => response.json())
      .then((data) => setPredictions(data))
      .catch((error) => console.error(error));

  }, []);

  return (

    <div className="analytics">

      <h1>Demand Prediction</h1>

      <div className="analytics-grid">

        {predictions.map((item, index) => (

          <div className="analytics-card" key={index}>

            <h3>{item.product}</h3>

            <h2>
              {item.predicted_quantity}
            </h2>

          </div>

        ))}

      </div>

    </div>

  );

}

export default DemandPrediction;