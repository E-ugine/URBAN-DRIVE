import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import '../styles/login.css'

async function authenticate(username, password) {
  const response = await fetch('/api/authenticate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password }),
  });
  if (!response.ok) {
    throw new Error('Authentication failed');
  }
  return response.json();
}

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const location = useLocation();

  function handleSubmit(event) {
    event.preventDefault();
    authenticate(username, password)
      .then(() => {
        localStorage.setItem('isAuthenticated', 'true');
        localStorage.setItem('username', username); // Store username
        setUsername("");
        setPassword(""); // Clear input fields
        navigate(location.state?.from || '/');
      })
      .catch(() => {
        setError('Invalid username or password');
      });
  }

  function handleForgotPassword() {
    const storedPassword = localStorage.getItem('password');
    if (storedPassword) {
      alert(`Your password is: ${storedPassword}`);
    } else {
      alert('No password found in local storage');
    }
  }

  return (
    <div className="login-container">
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input
            type='text'
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <label>
          Password:
          <input
            type='password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        {error && <p className="error">{error}</p>}
        <input type='submit' value="Submit" />
      </form>
      <button onClick={handleForgotPassword} className="forgot-password">
        Forgot Password?
      </button>
    </div>
  );
}

export default Login;
