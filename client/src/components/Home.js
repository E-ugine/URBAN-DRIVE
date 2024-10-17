import React,{useState} from 'react'
import Hero from './Hero';
import CarsCard from './CarsCard';
import CarTypeCard from './CarTypeCard';
import CarsFilter from './CarsFilter';
import { useOutletContext } from 'react-router-dom'

function Home() {
//   const {cars, handleChange, filters, handleDelete} = useOutletContext();
// const[type, setType] = useState("");
// const [currentPage, setCurrentPage] = useState(1);
// const carsPerPage = 4;

// function handleTypeClick(e){
//   const selectedType = e.target.getAttribute('type');
//   if (selectedType === type) {
//     setType("");
//   }
//   else{
//     setType(selectedType);
//   }
// }

// const carType = cars.reduce((acc, car) => {
//   acc[car.carType] = (acc[car.carType] || 0) + 1;
//   return acc;
// }, {});
// const carTypeCount = Object.entries(carType)

// const filteredCars = cars.filter(car => {
//   return (
//     (type? car.carType === type : true) &&
//     (filters.name ? car.name === filters.name : true)
//   )
// })


  return (
    <>
    <Hero/>
    {/* <CarsFilter filters={filters} handleChange={handleChange} /> */}
    <div className='car-type-section'>
    <small><em className='dash'>———</em> Car Types</small>
    <h2>Available <em>Cars</em></h2>
    </div>
    </>
      
  )
}
export default Home;
