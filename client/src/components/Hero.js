import React from "react";
import '../styles/hero.css'

function Hero(){
    return(
        <div className="hero">
           <div className="hero-div">
            <p className='sub-header'>Quirky cars for whimsical travels. </p>
            <h1>Right Here</h1>
            <p>My grandma's the most careful, safe driver in the world.
            You put her in a rental car, and she's doing doughnuts in the K-Mart parking.</p>
            <small><em className='dash'>———</em>Driven by Quality, Fueled by Service!</small>
           </div>
           <img src="https://i.pinimg.com/enabled_lo/564x/07/8f/b6/078fb61e97491766a8e5eac61a1f5b9b.jpg" alt="hero"/>
        </div>
    )
}
export default Hero;