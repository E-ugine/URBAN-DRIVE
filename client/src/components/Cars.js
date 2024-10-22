import React, { useState, useEffect } from 'react';
import CarsCard from './CarsCard';
import '../styles/cars.css';

function Cars() {
  const [cars, setCars] = useState([]);
  const [search, setSearch] = useState('');
  const [minPrice, setMinPrice] = useState(''); 
  const [maxPrice, setMaxPrice] = useState(''); 
  const [filteredCars, setFilteredCars] = useState([]); 
  const [loading, setLoading] = useState(true);
console.log(cars)
  useEffect(() => {
    fetch('/cars')
      .then((response) => response.json())
      .then((data) => {
        setCars(data);
        setFilteredCars(data); 
        setLoading(false);
      })
      .catch((error) => console.error('Error fetching cars data:', error));
  }, []);

  function handleSearchChange(event){
    setSearch(event.target.value);
  };

  function handleMinPriceChange(event){
    setMinPrice(event.target.value);
  };

  function handleMaxPriceChange (event) {
    setMaxPrice(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault(); 

    const toLowerCaseSearch = search.toLowerCase();
    const filtered = cars.filter((car) => {
      const matchesSearch =
        car.name.toLowerCase().includes(toLowerCaseSearch) ||
        car.type.toLowerCase().includes(toLowerCaseSearch) ||
        car.description.toLowerCase().includes(toLowerCaseSearch);

      const matchesMinPrice = minPrice === '' || car.price >= Number(minPrice);
      const matchesMaxPrice = maxPrice === '' || car.price <= Number(maxPrice);

      return matchesSearch && matchesMinPrice && matchesMaxPrice;
    });
    setFilteredCars(filtered); 
    setSearch('');
    setMinPrice('');
    setMaxPrice('');
  };

  if (loading) {
    return <p>Loading cars data...</p>;
  }

  return (
    <div className="cars-page">
      <h1>Available Cars</h1>
      
      <form onSubmit={handleSubmit} className="search-bar">
        <input
          type="text"
          placeholder="Search cars..."
          value={search}
          onChange={handleSearchChange}
        />
        <input
          type="number"
          placeholder="Min Price"
          value={minPrice}
          onChange={handleMinPriceChange}
        />
        <input
          type="number"
          placeholder="Max Price"
          value={maxPrice}
          onChange={handleMaxPriceChange}
        />
        <button type="submit">Search</button> 
      </form>
      <div className="car-list">
        {filteredCars.length > 0 ? (
          filteredCars.map((car) => <CarsCard key={car.id} car={car} />)
        ) : (
          <p>No cars found matching your criteria.</p>
        )}
      </div>
    </div>
  );
}

export default Cars;
