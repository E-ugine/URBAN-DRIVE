import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import '../styles/car-details.css';

function CarsDetail() {
  const { id } = useParams();
  const [car, setCar] = useState(null);
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`http://localhost:3000/cars/${id}`)
      .then((response) => response.json())
      .then((data) => {
        setCar(data);
        setLoading(false);
      })
      .catch((error) => console.error('Error fetching car data:', error));
  }, [id]);
  if (loading) {
    return <p>Loading car details...</p>;
  }
  if (!car) {
    return <p>No car details available.</p>;
  }
  return (
    <div>
      <div className="car-details">
        <button onClick={() => navigate(-1)} className="back-btn">&larr; Back</button>
        <div className="car-main">
          <div>
            <h2>Car Description</h2>
            <p>{car.description}</p>
            <h2>Car Overview</h2>
            <h3>{car.carType}</h3>     
          </div>
        </div>
      </div>
    </div>
  );
}
export default CarsDetail;
