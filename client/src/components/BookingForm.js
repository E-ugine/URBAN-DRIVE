import React, { useContext } from "react";
import { useLocation } from "react-router-dom";
import { CartContext } from "../context/CartContext"; 
import '../styles/booking-form.css';
import { Form, FormGroup } from "reactstrap";

function BookingForm() {
  const { state } = useLocation(); 
  const { carImage, carName, carPrice } = state || {};
  const { cart, addToCart } = useContext(CartContext); 

  const submitHandler = (event) => {
    event.preventDefault();

    
    if (cart.length >= 3) {
      alert("You cannot add more than 3 cars to your cart.");
      return;
    }

    const carExists = cart.some((car) => car.name === carName);
    if (carExists) {
      alert(`${carName} is already in your cart!`);
    } else {
      const car = { image_url: carImage, name: carName, price: carPrice };
      addToCart(car);
      alert(`${carName} has been added to your cart!`);
    }
  };

  return (
    <div className="booking-container">
      <div className="car-image-section">
        <img src={carImage} alt={carName} className="car-img" />
        <h2>{carName}</h2>
        <p>{carPrice} / Day</p>
      </div>
      <div className="booking-info">
        <h3>Booking Information</h3>
        <Form onSubmit={submitHandler}>
          <FormGroup className="booking__form d-inline-block me-4 mb-4">
            <input type="text" placeholder="First Name" />
          </FormGroup>
          <FormGroup className="booking__form d-inline-block ms-1 mb-4">
            <input type="text" placeholder="Last Name" />
          </FormGroup>
          <FormGroup className="booking__form d-inline-block me-4 mb-4">
            <input type="email" placeholder="Email" />
          </FormGroup>
          <FormGroup className="booking__form d-inline-block ms-1 mb-4">
            <input type="number" placeholder="Phone Number" />
          </FormGroup>
          {/* <FormGroup className="booking__form d-inline-block me-4 mb-4">
            <input type="text" placeholder="From Address" />
          </FormGroup>
          <FormGroup className="booking__form d-inline-block ms-1 mb-4">
            <input type="text" placeholder="To Address" />
          </FormGroup>
          <FormGroup className="booking__form d-inline-block me-4 mb-4">
            <select name="" id="">
              <option value="1 person">1 Person</option>
              <option value="2 person">2 Person</option>
              <option value="3 person">3 Person</option>
              <option value="4 person">4 Person</option>
              <option value="5+ person">5+ Person</option>
            </select>
          </FormGroup>
          <FormGroup className="booking__form d-inline-block ms-1 mb-4">
            <select name="" id="">
              <option value="1 luggage">1 luggage</option>
              <option value="2 luggage">2 luggage</option>
              <option value="3 luggage">3 luggage</option>
              <option value="4 luggage">4 luggage</option>
              <option value="5+ luggage">5+ luggage</option>
            </select>
          </FormGroup>
          <FormGroup className="booking__form d-inline-block me-4 mb-4">
            <input type="date" placeholder="Journey Date" />
          </FormGroup>
          <FormGroup className="booking__form d-inline-block ms-1 mb-4">
            <input type="time" placeholder="Journey Time" className="time__picker" />
          </FormGroup>
          <FormGroup>
            <textarea rows={5} type="textarea" className="textarea" placeholder="Write"></textarea>
          </FormGroup> */}
          <button className="reserve-btn" type="submit">Reserve Now</button>
        </Form>
      </div>
      <div className="payment-info">
        <h3>Payment Information</h3>
        <div className="payment-options">
          <FormGroup>
            <label>
              <input type="radio" name="payment" /> Direct Bank Transfer
            </label>
          </FormGroup>
          <FormGroup>
            <label>
              <input type="radio" name="payment" /> Cheque Payment
            </label>
          </FormGroup>
          <FormGroup>
            <label>
              <input type="radio" name="payment" /> Master Card
            </label>
          </FormGroup>
          <FormGroup>
            <label>
              <input type="radio" name="payment" /> Paypal
            </label>
          </FormGroup>
        </div>
      </div>
    </div>
  );
}

export default BookingForm;
