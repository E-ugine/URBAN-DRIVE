import React from 'react';
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
          <small>{car.type}</small> 
        </div>
      </div>
      <div className="car-card-content">
        <div className="car-card-details">
          <h2 className="car-card-title">{car.name}</h2> 
          <div className="car-card-price">
            <h3>KES {car.price.toLocaleString()}</h3>
            {car.status === 'For Rent' && <span>/day</span>} 
          </div>
          <div className="car-card-location">
            <p>{car.location}</p>
          </div>
          <hr />
        </div>
      </div>
      <div className="car-card-actions">
        <button className="btn book-now">Book now</button>
        <button className="btn details">Details</button>
      </div>
    </div>
  );
}

export default CarsCard;
