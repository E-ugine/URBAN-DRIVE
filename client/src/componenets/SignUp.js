import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/signup.css'

async function signup(username, password) {
  const response = await fetch('/api/signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password }),
  });

  if (!response.ok) {
    throw new Error('Signup failed');
  }
  return response.json();
}

function Signup() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  function handleSubmit(event) {
    event.preventDefault();
    signup(username, password)
      .then(() => {
        localStorage.setItem('isSignedUp', 'true'); 
        localStorage.setItem('username', username); 
        localStorage.setItem('password', password);
        setUsername("");
        setPassword(""); 
        navigate('/login'); 
      })
      .catch(() => {
        setError('Username already exists or signup failed');
      });
  }

  return (
    <div className="signup-container">
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
        <input type='submit' value="Sign Up" />
      </form>
    </div>
  );
}

export default Signup;
