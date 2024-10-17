import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
// import Login from "./components/Login";
// import Signup from "./components/SignUp";
import ProtectedRoute from "./components/ProtectedRoute";
import Home from "./components/Home";
// import About from "./components/About";
import Navbar from "./components/Navbar";
// import Footer from "./components/Footer";

function App() {
  const isSignedUp = localStorage.getItem('isSignedUp');

  return (
    <>
    <div>
   <Navbar/>
   <Home/>
    </div>
    <Router>
      <div>
      <Routes>
        <Route path="/" element={isSignedUp ? <Navigate to="/login" /> : <Navigate to="/signup" />} />
        {/* <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} /> */}
        {/* <Route path="/about" element={<About/>}/> */}
        {/* <Route path="/home" element={<ProtectedRoute component={Home} />} /> */}
      </Routes>
      </div>
     
    </Router>
    <div>
      {/* <Footer/> */}
    </div>
  
    </>
  );
 
}

export default App;
