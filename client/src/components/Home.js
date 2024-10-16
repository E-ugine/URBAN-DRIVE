import React, { useState, useEffect } from 'react';
import Hero from './Hero';
import CarsCard from './CarsCard';
import SearchBar from './SearchBar';

function Home() {
  const [cars, setCars] = useState([]);
  const [filters, setFilters] = useState({ name: '' });
  const [type, setType] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const carsPerPage = 2;
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:3000/cars')
      .then((response) => response.json())
      .then((data) => {
        setCars(data);
        setLoading(false);
      })
      .catch((error) => console.error('Error fetching cars data:', error));
  }, []);

 
  const filteredCars = cars.filter((car) => {
      return type ? car.carType === type : true;
    })
 cars.filter((car) => {
      return filters.name ? car.name === filters.name : true;
    });

  const totalPages = Math.ceil(filteredCars.length / carsPerPage);
  const displayedCars = filteredCars.slice(
    (currentPage - 1) * carsPerPage,
    currentPage * carsPerPage
  );

  if (loading) {
    return <p>Loading cars data...</p>;
  }

  return (
    <div className="home">
      <Hero />
      <SearchBar/>
      <div className="properties-list">
        {displayedCars.map((car) => (
          <CarsCard key={car.id} car={car} />
        ))}
      </div>
      <div className="pagination">
        {[...Array(totalPages)].map((_, index) => (
          <button
            key={index}
            onClick={() => setCurrentPage(index + 1)}
            className={currentPage === index + 1 ? 'active' : ''}
          >
            {index + 1}
          </button>
        ))}
      </div>
    </div>
  );
}

export default Home;
