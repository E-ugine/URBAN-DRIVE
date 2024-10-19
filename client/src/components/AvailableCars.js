import React, { useState, useEffect } from 'react';
import CarsCard from './CarsCard';
import '../styles/available-cars.css';

function AvailableCars() {
  const [cars, setCars] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:3001/cars')
      .then(response => response.json())
      .then(data => {
        setCars(data.slice(0, 4)); 
        setLoading(false);
      })
      .catch(error => console.error('Error fetching cars:', error));
  }, []);
  if (loading) {
    return <p>Loading cars...</p>;
  }
  return (
    <div className="available-cars-section">
      <h2>Amazing Offers!!!</h2>
      <div className="car-list">
        {cars.map(car => (
          <CarsCard key={car.id} car={car} />
        ))}
      </div>
      <a href="/cars" className="view-all-btn">View All Cars</a>
    </div>
  );
}

export default AvailableCars;
