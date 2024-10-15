import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./componenets/Login";
import Signup from "./componenets/SignUp";
import ProtectedRoute from "./componenets/ProdectedRoute";
import Home from "./componenets/Home";
import About from "./componenets/About";

function App() {
  const isSignedUp = localStorage.getItem('isSignedUp');

  return (
    <>
    <Router>
      <Routes>
        <Route path="/" element={isSignedUp ? <Navigate to="/login" /> : <Navigate to="/signup" />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/about" element={<About/>}/>
        <Route path="/home" element={<ProtectedRoute component={Home} />} />
      </Routes>
    </Router>
    <div>
      
    </div>
    </>
  );
 
}

export default App;
