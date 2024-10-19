import React from 'react';
import '../styles/signupmodal.css';

const SignupModal = ({ login }) => {
  return (
    <div className="signup-modal">
      <div className="modal-content">
        <h2>Welcome to UrbanDrive!</h2>
        <p>Please sign up to explore the best car rentals in town.</p>
        <button onClick={login} className="google-signup-btn">
          Sign up with Google
        </button>
      </div>
    </div>
  );
};

export default SignupModal;
