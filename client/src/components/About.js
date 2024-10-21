import React from "react";
import { useNavigate } from "react-router-dom";
import '../styles/About.css'

const About = () => {
  return (
    <div className="about-container">
      {/* Image section */}
      <div className="about-image">
        {/* Image will be set via CSS */}
      </div>

      <section className="about-content">
        <h2>Drive the Extraordinary</h2>
        <p>
          Urban Drive is a premium car rental service designed for those who seek comfort, luxury, and efficiency on the go. Whether you're traveling for business, pleasure, or simply want to make a statement on the road, we provide a curated selection of high-end vehicles tailored to your needs.
        </p>
        
        <h3>Our Fleet</h3>
        <p>
          Our fleet includes the latest models of luxury sedans, sports cars, SUVs, and electric vehicles, ensuring a seamless driving experience. Each vehicle is maintained to the highest standards, ensuring performance, safety, and comfort at every turn.
        </p>
        
        <div className="highlight-section">
          <h3>What Sets Us Apart?</h3>
          <ul>
            <li>24/7 Customer Support & Assistance</li>
            <li>Flexible booking options with transparent pricing</li>
            <li>Pickup and drop-off services at multiple locations</li>
            <li>Eco-friendly options with electric cars</li>
            <li>Exclusive membership perks and discounts</li>
          </ul>
        </div>

        <div className="experience-section">
          <h3>We Don’t Just Rent Cars – We Offer Experiences</h3>
          <p>
            Whether you want to explore the city, impress your clients, or enjoy a weekend getaway, we have the perfect vehicle for every occasion. At Urban Drive, we transform your journey into an unforgettable experience.
          </p>
        </div>
      </section>
    </div>
  );
};

export default About
