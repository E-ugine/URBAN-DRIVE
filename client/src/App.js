import React from "react";
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { UserProvider } from './context/UserContext'; 
import Home from "./components/Home";
import About from "./components/About";
import Cars from "./components/Cars";
import CarsDetail from "./components/CarsDetail";
import Services from "./components/Services";
// import Pricing from "./components/Pricing";
import Contact from "./components/Contact";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Bookings from "./components/Bookings";
// import Login from "./components/Login";  
// import Signup from "./components/SignUp"; 

function App() {
  return (
    <UserProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/services" element={<Services />} />
          {/* <Route path="/pricing" element={<Pricing />} /> */}
          <Route path="/cars" element={<Cars />} />
          <Route path="/cars/:id/book" element={<Bookings />} />
          <Route path="/cars/:id" element={<CarsDetail />} />
          <Route path="/contact" element={<Contact />} />
          {/* <Route path="/login" element={<Login />} />   
          <Route path="/signup" element={<Signup />} /> */}
        </Routes>
        <Footer />
      </Router>
    </UserProvider>
  );
}

export default App;
