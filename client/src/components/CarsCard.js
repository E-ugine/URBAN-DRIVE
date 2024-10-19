import React, { useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { UserContext } from '../context/UserContext';
import '../styles/card.css';

function CarsCard({ car }) {
  const { user } = useContext(UserContext);
  const navigate = useNavigate();

  const handleBookNow = () => {
    if (user) {
      // Proceed with booking for signed-in users
      navigate(`/cars/${car.id}/book`);
    } else {
      // Notify user that they can book, but will need to sign in later
      const proceedWithoutLogin = window.confirm(
        'You can start booking now, but you will need to sign in or sign up to complete the booking. Do you want to proceed?'
      );
      if (proceedWithoutLogin) {
        // Continue booking process even without login
        navigate(`/cars/${car.id}/book`);
      }
    }
  };
  

  return (
    <div className="car-card" id={car.id}>
      <div className="car-card-img-container">
        {car.image_url ? (
          <img
            className="car-card-img"
            src={car.image_url}
            alt={car.name}
          />
        ) : (
          <div className="no-image">No Image Available</div>
        )}
        <div className="car-card-tags">
          <small>{car.status}</small>
        </div>
      </div>
      <div className="car-card-content">
        <h2 className="car-card-title">{car.name}</h2>
        <div className="car-card-price">
          <h3>${car.price.toLocaleString()} /day</h3>
          {car.status === 'For Rent' && <span>/day</span>}
        </div>
        <div className="car-card-actions">
          <Link to={`/cars/${car.id}`} className="btn details">Details</Link>
          <button onClick={handleBookNow} className="btn book-now">Book Now</button>
        </div>
      </div>
    </div>
  );
}

export default CarsCard;
