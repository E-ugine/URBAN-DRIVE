import React from "react";
import { Navigate, useLocation } from "react-router-dom";

function ProtectedRoute({ component: Component }) {
  const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true';
  const location = useLocation();

  return isAuthenticated ? (
    <Component />
  ) : (
    <Navigate to="/login" state={{ from: location }} />
  );
}

export default ProtectedRoute;
