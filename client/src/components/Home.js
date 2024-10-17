import React from 'react';
import Hero from './Hero';
import Services from './Services';
import AvailableCars from './AvailableCars';
import '../styles/home.css';

function Home() {
  return (
    <div>
      <Hero />
      <div className="welcome-section">
        <h2>Welcome to UrbanDrive</h2>
        <p>Your journey starts here. Find the perfect car for your adventure.</p>
      </div>
      <Services />
      <AvailableCars />
      {/* Add Testimonials and some  Blog possibly  */}
    </div>
  );
}

export default Home;
