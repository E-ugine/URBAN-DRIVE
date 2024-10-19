import React, { useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { UserContext } from '../context/UserContext';
import '../styles/card.css';

function CarsCard({ car }) {
  



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
          <button  className="btn book-now">Book Now</button>
        </div>
      </div>
    </div>
  );
}

export default CarsCard;
