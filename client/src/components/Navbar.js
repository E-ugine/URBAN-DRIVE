import React from "react";
import { Link } from "react-router-dom";
import '../styles/navbar.css';

function Navbar() {
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
            <li><Link to="/bookings">Bookings</Link></li>
            {/* <li><Link to="/pricing">Pricing</Link></li>  */}
            <li><Link to="/cars">Cars</Link></li> 
            <li><Link to="/contact">Contact</Link></li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default Navbar;
