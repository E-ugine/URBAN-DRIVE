import React from 'react';
import Hero from './Hero';
import Services from './Services';
import AvailableCars from './AvailableCars';
import '../styles/home.css';

function Home() {
  return (
    <div className="home-container">
      <Hero />
      <div className="welcome-section">
        <div className="welcome-image">
          <img
            src='https://plus.unsplash.com/premium_photo-1683121327669-9739544c58e4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
            alt='home'
          />
        </div>
        <div className="welcome-text">
          <h1>Welcome to UrbanDrive</h1>
          <p>
            Your journey starts here. Find the perfect car for your adventure.
          </p>
          <p>
            At UrbanDrive, we offer a wide range of vehicles to suit your needs, whether you're looking for comfort, luxury, or efficiency. Our fleet is designed to provide you with the best driving experience possible. We are committed to making your travel seamless and enjoyable.
          </p>
          <p>
            Explore our selection of cars and discover your ideal match today. Join us as we embark on a journey of unforgettable experiences and make your travel dreams come true!
          </p>
        </div>
      </div>
      <AvailableCars />
      <Services />
      {/* We could add testimonials and some Blog possibly */}
    </div>
  );
}

export default Home;
