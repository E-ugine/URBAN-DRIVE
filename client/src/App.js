import React from "react";
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import About from "./components/About";
import Cars from "./components/Cars";
import CarsDetail from "./components/CarsDetail";
import Services from "./components/Services";
import Pricing from "./components/Pricing";
import Contact from "./components/Contact";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import SignUpPage from "./components/SignUp"; 

function App() {
  return (
    <Router>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/about" element={<About/>}/>
        <Route path="/services" element={<Services/>}/>
        <Route path="/pricing" element={<Pricing/>}/>
        <Route path="/cars" element={<Cars/>}/>
        <Route path="/cars/:id" element={<CarsDetail/>}/>
        <Route path="/contact" element={<Contact/>}/>
        <Route path="/signup" element={<SignUpPage/>}/> {/* Added Sign-up route */}
      </Routes>
      <Footer/>
    </Router>
  );
}

export default App;
