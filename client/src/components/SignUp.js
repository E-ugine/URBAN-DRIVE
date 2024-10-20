import React, { useState } from 'react';
import '../styles/SignUp.css';

const SignUpPage = ({ onSignUp }) => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (formData.password !== formData.confirmPassword) {
      alert("Passwords don't match!");
      return;
    }
    
    // Call onSignUp with the username
    onSignUp(formData.username);
    console.log("Form submitted", formData);
    
    // Optionally, reset the form after submission
    setFormData({
      username: '',
      email: '',
      password: '',
      confirmPassword: ''
    });
  };

  return (
    <div className="signup-container">
      <div className="form-box">
        <h2>Join Urban Drive</h2>
        <p className="tagline">Drive into the future with ease</p>
        <form onSubmit={handleSubmit}>
          <div className="input-wrapper">
            <input
              type="text"
              name="username"
              placeholder="Username"
              value={formData.username}
              onChange={handleChange}
              required
            />
          </div>
          <div className="input-wrapper">
            <input
              type="email"
              name="email"
              placeholder="Email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>
          <div className="input-wrapper">
            <input
              type="password"
              name="password"
              placeholder="Password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>
          <div className="input-wrapper">
            <input
              type="password"
              name="confirmPassword"
              placeholder="Confirm Password"
              value={formData.confirmPassword}
              onChange={handleChange}
              required
            />
          </div>
          <button type="submit" className="submit-btn">Sign Up</button>
        </form>
        <p className="login-redirect">
          Already have an account? <a href="#">Log in</a>
        </p>
      </div>
    </div>
  );
};

export default SignUpPage;