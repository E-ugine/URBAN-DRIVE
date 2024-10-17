function Services() {
    const servicesList = [
      { id: 1, title: "Car Maintenance", description: "Regular check-ups to ensure your car runs smoothly." },
      { id: 2, title: "Car Rental", description: "Affordable car rental options for your convenience." },
      { id: 3, title: "Insurance Services", description: "Get the best insurance deals for your vehicle." },
      { id: 4, title: "Financing Options", description: "Flexible financing solutions tailored to your needs." },
    ];
  
    return (
      <div className="services-section">
        <h2>Our Services</h2>
        <div className="services-list">
          {servicesList.map(service => (
            <div key={service.id} className="service-card">
              <h3>{service.title}</h3>
              <p>{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    );
  }
  
  export default Services;