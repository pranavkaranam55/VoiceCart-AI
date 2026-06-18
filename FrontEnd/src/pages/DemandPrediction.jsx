import { useEffect, useState } from "react";

function DemandPrediction() {

  const [predictions, setPredictions] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/prediction")
      .then((response) => response.json())
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