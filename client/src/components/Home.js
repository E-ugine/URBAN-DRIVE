import React, { useState } from 'react';
import Hero from './Hero';
import CarsCard from './CarsCard';
import CarTypeCard from './CarTypeCard';
import CarsFilter from './CarsFilter';
import Services from './Services';  
import { useOutletContext } from 'react-router-dom';

function Home() {
  const { cars, handleChange, filters, handleDelete } = useOutletContext();
  const [type, setType] = useState("");
  const carsPerPage = 4;

  function handleTypeClick(e) {
    const selectedType = e.target.getAttribute('type');
    setType(selectedType === type ? "" : selectedType);
  }

  // Counting car types
  const carType = cars.reduce((acc, car) => {
    acc[car.carType] = (acc[car.carType] || 0) + 1;
    return acc;
  }, {});
  
  const carTypeCount = Object.entries(carType);

  // Filtering cars based on selected type and filters
  const filteredCars = cars.filter(car => (
    (type ? car.carType === type : true) &&
    (filters.name ? car.name === filters.name : true)
  ));

  return (
    <>
      <Hero />
      <CarsFilter filters={filters} handleChange={handleChange} />
      <div className='car-type-section'>
        <small><em className='dash'>———</em> Car Types</small>
        <h2>Available <em>Cars</em></h2>
        <div className="car-type-cards">
          {carTypeCount.map(([carType, count]) => (
            <CarTypeCard 
              key={carType}
              type={carType}
              count={count}
              handleTypeClick={handleTypeClick}
              isSelected={type === carType}
            />
          ))}
        </div>
      </div>
      <div className='cars-list'>
        {filteredCars.slice(0, carsPerPage).map(car => (
          <CarsCard key={car.id} car={car} />
        ))}
      </div>
      <Services />  {/* Add the Services component here */}
    </>
  );
}

export default Home;