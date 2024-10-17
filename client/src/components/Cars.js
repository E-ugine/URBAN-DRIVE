import React, { useState, useEffect } from 'react';
import CarsCard from './CarsCard';
import '../styles/cars.css';

function Cars() {
  const [cars, setCars] = useState([]);
  const [search, setSearch] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:3001/cars')
      .then((response) => response.json())
      .then((data) => {
        setCars(data);
        setLoading(false);
      })
      .catch((error) => console.error('Error fetching cars data:', error));
  }, []);

  const handleSearchChange = (event) => {
    setSearch(event.target.value);
  };

  const filteredCars = cars.filter((car) => {
    const toLowerCaseSearch = search.toLowerCase();
    return (
      car.name.toLowerCase().includes(toLowerCaseSearch) ||
      car.type.toLowerCase().includes(toLowerCaseSearch) ||
      car.description.toLowerCase().includes(toLowerCaseSearch)
    );
  });

  if (loading) {
    return <p>Loading cars data...</p>;
  }

  return (
    <div className="cars-page">
      <h1>Our Cars</h1>
      <div className="search-bar">
        <input
          type="text"
          placeholder="Find cars..."
          value={search}
          onChange={handleSearchChange}
        />
      </div>
      <div className="car-list">
        {filteredCars.map((car) => (
          <CarsCard key={car.id} car={car} />
        ))}
      </div>
    </div>
  );
}

export default Cars;
