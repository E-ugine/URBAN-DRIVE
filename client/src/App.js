import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./componenets/Login";
import Signup from "./componenets/SignUp";
import ProtectedRoute from "./componenets/ProdectedRoute";
import Home from "./componenets/Home";

function App() {
  const isSignedUp = localStorage.getItem('isSignedUp');

  return (
    <Router>
      <Routes>
        <Route path="/" element={isSignedUp ? <Navigate to="/login" /> : <Navigate to="/signup" />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/home" element={<ProtectedRoute component={Home} />} />
      </Routes>
    </Router>
  );
}

export default App;
