import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import '../styles/rental-details.css';

function RentalDetails() {
  const { state } = useLocation();
  const { cart } = state || {};
  
  const [days, setDays] = useState(1); 
  const totalAmount = cart.reduce((total, car) => total + car.price * days, 0);

  const handlePayment = () => {
    alert(`Payment confirmed! Amount paid: $${totalAmount}`);
  };

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
        <label htmlFor="days">Update Number of Days:</label>
        <input
          id="days"
          type="number"
          value={days}
          onChange={(e) => setDays(Number(e.target.value))}
          min="1"
        />
        <button onClick={handlePayment} className="pay-button">
          Pay
        </button>
      </div>
    </div>
  );
}

export default RentalDetails;
