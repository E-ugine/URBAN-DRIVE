import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { UserProvider } from './context/UserContext'; 
import { CartProvider } from './context/CartContext'; 
import SignUp from "./components/SignUp"; 
import Login from "./components/Login"; 
import Home from "./components/Home";
import About from "./components/About";
import Cars from "./components/Cars";
import CarsDetail from "./components/CarsDetail";
import Services from "./components/Services";
import BookingForm from "./components/BookingForm";
import Contact from "./components/Contact";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Cart from "./components/Cart";
import RentalDetails from "./components/RentalDetails";
import PaymentDetails from "./components/PaymentDetails";


function App() {
  
  return (
    <UserProvider>
      <CartProvider> 
        <Router>
          <Navbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/services" element={<Services />} />
            <Route path="/cars" element={<Cars />} />
            <Route path="/booking" element={<BookingForm />} />
            <Route path="/cars/:id" element={<CarsDetail />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/cart" element={<Cart />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/login" element={<Login />} />
            <Route path="/rental-details" element={<RentalDetails />} />
            <Route path="/payment-details" element={<PaymentDetails />} />
          </Routes>
          <Footer />
        </Router>
      </CartProvider>
    </UserProvider>
  );
}

export default App;
