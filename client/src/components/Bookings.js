import React, { useState } from 'react';

function Bookings({ car }) {
  const [bookingDetails, setBookingDetails] = useState({
    date: '',
    duration: '',
    userId: '', 
  });

  function handleSubmit(e){
    e.preventDefault();
    console.log('Booking confirmed:', bookingDetails);
  };

  function handleChange(e){
    setBookingDetails({
      ...bookingDetails,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Book {car.name}</h2>
      <label>Date: 
        <input type="date" name="date" value={bookingDetails.date} onChange={handleChange} required />
      </label>
      <label>Duration (days): 
        <input type="number" name="duration" value={bookingDetails.duration} onChange={handleChange} required />
      </label>
      <button type="submit">Confirm Booking</button>
    </form>
  );
}

export default Bookings;
