import React, { useState, useEffect } from "react";
import { googleLogout, useGoogleLogin } from '@react-oauth/google';
import axios from 'axios';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { UserProvider } from './context/UserContext'; 
import Home from "./components/Home";
import About from "./components/About";
import Cars from "./components/Cars";
import CarsDetail from "./components/CarsDetail";
import Services from "./components/Services";
import Pricing from "./components/Pricing";
import Contact from "./components/Contact";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Bookings from "./components/Bookings";
import SignupModal from './components/SignupModal';

function App() {
  const [ user, setUser ] = useState([]);
  const [ profile, setProfile ] = useState(null); 
  const [ showModal, setShowModal ] = useState(false);

  const login = useGoogleLogin({
      onSuccess: (codeResponse) => setUser(codeResponse),
      onError: (error) => console.log('Login Failed:', error)
  });

  useEffect(() => {
      if (user) {
          axios
              .get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
                  headers: {
                      Authorization: `Bearer ${user.access_token}`,
                      Accept: 'application/json'
                  }
              })
              .then((res) => {
                  setProfile(res.data);
                  setShowModal(false); 
              })
              .catch((err) => console.log(err));
      }
  }, [user]);

  useEffect(() => {
      if (!profile) {
          setShowModal(true);
      }
  }, [profile]);

  
  const logOut = () => {
      googleLogout();
      setProfile(null);
  };

  return (
    <UserProvider>
      {showModal && <SignupModal login={login} />}
      <Router>
        <Navbar profile={profile} logOut={logOut} />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/services" element={<Services />} />
          <Route path="/pricing" element={<Pricing />} />
          <Route path="/cars" element={<Cars />} />
          <Route path="/cars/:id/book" element={<Bookings />} />
          <Route path="/cars/:id" element={<CarsDetail />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
        <Footer />
      </Router>
    </UserProvider>
  );
}

export default App;
