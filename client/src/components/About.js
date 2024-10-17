// About.js
import React from "react";
import { useNavigate } from "react-router-dom";
import '../styles/About.css'

function About() {
  // const navigate = useNavigate();

  // const handleBack = () => {
  //   navigate('/');
  // };

  return (
    <div className="about-container">
      <h1 className="about-title">About Urban Drive</h1>
      <img 
        src="https://source.unsplash.com/800x400/?luxury-car,rental" 
        alt="Luxury Rental Cars" 
        className="about-image" 
      />
      <p className="about-text">
        <strong>Urban Drive</strong> is a premium car rental service designed for those who seek
        comfort, luxury, and efficiency on the go. Whether you're traveling for business, pleasure,
        or simply want to make a statement on the road, we provide a curated selection of high-end
        vehicles tailored to your needs.
      </p>
      <p className="about-text">
        Our fleet includes the latest models of luxury sedans, sports cars, SUVs, and electric vehicles,
        ensuring a seamless driving experience. Each vehicle is maintained to the highest standards,
        ensuring performance, safety, and comfort at every turn.
      </p>
      <p className="about-text">
        <strong>What sets us apart?</strong> We offer:
        <ul>
          <li>24/7 Customer Support & Assistance</li>
          <li>Flexible booking options with transparent pricing</li>
          <li>Pickup and drop-off services at multiple locations</li>
          <li>Eco-friendly options with electric cars</li>
          <li>Exclusive membership perks and discounts</li>
        </ul>
      </p>
      <p className="about-text">
        At Urban Drive, we don’t just rent cars – we offer experiences. Whether you want to explore the
        city, impress your clients, or enjoy a weekend getaway, we have the perfect vehicle for every occasion.
      </p>
      {/* <button onClick={handleBack} className="back-button">Back to Home</button> */}
    </div>
  );
}

export default About;
