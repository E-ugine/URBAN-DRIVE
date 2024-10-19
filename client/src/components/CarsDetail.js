import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import '../styles/car-details.css';

function CarsDetail() {
  const { id } = useParams();
  const [car, setCar] = React.useState(null);
  const navigate = useNavigate();
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    fetch(`http://localhost:3001/cars/${id}`)
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
    <div className="car-details">
      <button onClick={() => navigate(-1)} className="back-btn">&larr; Back</button>
      <div className="car-details-container">
        <img src={car.image_url} alt={car.name} className="car-details-img" />
        <div className="car-details-info">
          <h2>{car.name}</h2>
          <h3>${car.price.toLocaleString()} / day</h3>
          <p>{car.description}</p>
          <button 
  className="btn book-now" 
  onClick={() => navigate('/booking', { state: { carImage: car.image_url, carName: car.name, carPrice: car.price } })}>Book Now</button>

        </div>
      </div>
    </div>
  );
}

export default CarsDetail;
