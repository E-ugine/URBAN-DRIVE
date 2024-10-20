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
      <div>
          <img src='https://plus.unsplash.com/premium_photo-1683121327669-9739544c58e4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' alt='home'/>
        </div>
        <p>Welcome to UrbanDrive Your journey starts here. Find the perfect car for your adventure.
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptatum blanditiis esse accusantium dignissimos labore laborum. Veniam, corporis mollitia temporibus, in quaerat vero deleniti amet dolorem repudiandae, pariatur nam dolore! Impedit neque sit ad temporibus quam similique dolor ipsam praesentium sunt.
        </p>
      </div>
      <AvailableCars />
      <Services />
     
      {/* We could add testimonials and some  Blog possibly  */}
    </div>
  );
}

export default Home;
