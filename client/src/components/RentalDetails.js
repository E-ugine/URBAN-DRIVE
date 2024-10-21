import React from 'react';
import { useLocation } from 'react-router-dom';
// import '../styles/rental-details.css';

function RentalDetails() {
  const { state } = useLocation(); 
  const { cart, days } = state || {};
  
  const totalAmount = cart.reduce((total, car) => total + car.price * days, 0);

  return (
    <div className="rental-details-page">
      <h1>Rental Details</h1>
      <div className="rental-details">
        {cart.map((car) => (
          <div key={car.name} className="rental-item">
            <img src={car.image_url} alt={car.name} />
            <h3>{car.name}</h3>
            <p>Price: ${car.price} / day</p>
            <p>Rental Days: {days}</p>
            <p>Total: ${car.price * days}</p>
          </div>
        ))}
        <h2>Total Amount to Pay: ${totalAmount}</h2>
      </div>
    </div>
  );
}

export default RentalDetails;
