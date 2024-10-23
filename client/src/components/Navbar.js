import React, { useState } from "react";
import { Link } from "react-router-dom";
import { FaShoppingCart, FaUser } from 'react-icons/fa'; 
import '../styles/navbar.css';

function Navbar() {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  return (
    <header className="navbar">
      <div className="navbar-container">
        <h1 className="logo">
          Urban<em>Drive</em>
        </h1>
        <nav>
          <ul className="nav-links">
            <li><Link to="/">Home</Link></li> 
            <li><Link to="/about">About</Link></li> 
            <li><Link to="/services">Services</Link></li>
            <li><Link to="/cars">Cars</Link></li>
            
            <li className="cart-icon">
              <Link to="/cart">
                <FaShoppingCart size={20} />
              </Link>
            </li>

            <li className="dropdown">
              <button onClick={toggleDropdown} className="dropdown-btn">
                <FaUser size={20} style={{ marginRight: '5px' }} />
              </button>
              {isDropdownOpen && (
                <ul className="dropdown-content">
                  <li><Link to="/signup" onClick={toggleDropdown}>Sign Up</Link></li>
                  <li><Link to="/login" onClick={toggleDropdown}>Login</Link></li>
                  <li><Link to="/profile" onClick={toggleDropdown}>Profile</Link></li>
                  <li><Link to="/bookings" onClick={toggleDropdown}>Bookings</Link></li>
                </ul>
              )}
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default Navbar;
