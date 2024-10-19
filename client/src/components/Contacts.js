import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import '../styles/Contacts.css';

function Contacts() {
  // State to handle form input
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form Data Submitted:', formData);
    // You can add form submission logic here, such as sending data to an API
  };

  return (
    <div className="contact-page">
      <h2>Contact Us</h2>
      
      <div className="contact-details">
        <p><strong>Email:</strong> contact@urbandrive.com</p>
        <p><strong>Phone:</strong> +1 234 567 890</p>
        <p><strong>Address:</strong> 123 Urban Drive, City, Country</p>
      </div>

      <h3>Send us a message</h3>
      
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input 
            type="text" 
            id="name" 
            name="name" 
            value={formData.name} 
            onChange={handleChange} 
            required 
          />
        </div>

        <div>
          <label htmlFor="email">Email:</label>
          <input 
            type="email" 
            id="email" 
            name="email" 
            value={formData.email} 
            onChange={handleChange} 
            required 
          />
        </div>

        <div>
          <label htmlFor="message">Message:</label>
          <textarea 
            id="message" 
            name="message" 
            value={formData.message} 
            onChange={handleChange} 
            required 
          />
        </div>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Contacts;