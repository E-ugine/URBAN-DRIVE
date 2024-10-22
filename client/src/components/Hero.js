import React from "react";
import { Link } from "react-router-dom";
import '../styles/hero.css'

function Hero(){
    return(
        <div className="hero">
           <div className="hero-div">
            <p className='sub-header'>Quirky cars for whimsical travels. </p>
            <h1>Rent the best quality cars with us!</h1>
            <p>My grandma's the most careful, safe driver in the world.
            You put her in a rental car, and she's doing doughnuts in the K-Mart parking.</p>
            <small><em className='dash'>———</em>Driven by Quality, Fueled by Service!</small>
            <div className="nav-actions">
            <button><Link to="/signup" className="signup-button">Sign Up</Link></button>
            </div>
           </div>
           <img src="https://i.pinimg.com/enabled_lo/564x/07/8f/b6/078fb61e97491766a8e5eac61a1f5b9b.jpg" alt="hero"/>
        </div>
    )
}
export default Hero;