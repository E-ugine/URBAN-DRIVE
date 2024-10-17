import React, { useState, useEffect } from 'react';
import CarsCard from './CarsCard';
import CarsFilter from './CarsFilter';
import SearchBar from '../components/SearchBar';
import '../styles/cars.css';

function Cars() {
  const [cars, setCars] = useState([]);
  const [filters, setFilters] = useState({ price: '', name: '' });
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

  const handleChange = (event) => {
    setFilters({
      ...filters,
      [event.target.name]: event.target.value,
    });
  };

  const filteredCars = cars
    .filter((car) => {
      const toLowerCaseSearch = search.toLowerCase();
      return (
        car.name.toLowerCase().includes(toLowerCaseSearch) ||
        car.carType.toLowerCase().includes(toLowerCaseSearch) ||
        car.description.toLowerCase().includes(toLowerCaseSearch)
      );
    })
    .filter((car) => {
      return (
        (filters.price ? car.price <= Number(filters.price) : true) &&
        (filters.name ? car.name === filters.name : true)
      );
    });

  if (loading) {
    return <p>Loading cars data...</p>;
  }

  return (
    <div className="cars-container">
      <div className="cars-header">
        <h1>All Cars</h1>
        <SearchBar search={search} handleSearchChange={handleSearchChange} />
      </div>
      <CarsFilter filters={filters} handleChange={handleChange} />
      <div className="car-list">
        {filteredCars.map((car) => (
          <CarsCard key={car.id} car={car} />
        ))}
      </div>
    </div>
  );
}

export default Cars;
