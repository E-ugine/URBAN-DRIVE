// Services.js
import React from "react";
import '../styles/services.css';
import { FaCar, FaWrench, FaMoneyBill, FaLifeRing } from 'react-icons/fa';

function Services() {
  const servicesList = [
    { id: 1, icon: <FaCar />, title: "Car Rental", description: "Affordable car rental options for your convenience." },
    { id: 2, icon: <FaWrench />, title: "Car Maintenance", description: "Regular check-ups to ensure your car runs smoothly." },
    { id: 3, icon: <FaLifeRing />, title: "Insurance Services", description: "Get the best insurance deals for your vehicle." },
    { id: 4, icon: <FaMoneyBill />, title: "Financing Options", description: "Flexible financing solutions tailored to your needs." },
  ];

  return (
    <div className="services-section">
      <h2>Our Services</h2>
      <div className="services-list">
        {servicesList.map(service => (
          <div key={service.id} className="service-card">
            <div className="service-icon">
              {service.icon}
            </div>
            <h3>{service.title}</h3>
            <p>{service.description}</p>
          </div>
        ))}
      </div>
      <div>
        <p>Good</p>
      </div>
    </div>
  );
}

export default Services;
