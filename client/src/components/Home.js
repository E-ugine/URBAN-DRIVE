import React from 'react';
import Hero from './Hero';
import Services from './Services';
import AvailableCars from './AvailableCars';
import '../styles/home.css';
import BookingForm from './BookingForm';

function Home() {
  return (
    <div>
      <Hero />
      <BookingForm/>
      <div className="welcome-section">
        <h2>Welcome to UrbanDrive</h2>
        <p>Your journey starts here. Find the perfect car for your adventure.</p>
      </div>
      <AvailableCars />
      <Services />
     
      {/* We could add testimonials and some  Blog possibly  */}
    </div>
  );
}

export default Home;
