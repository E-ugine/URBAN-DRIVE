import React from "react";
import '../styles/booking-form.css';
import { Form, FormGroup } from "reactstrap";

function BookingForm() {
  const submitHandler = (event) => {
    event.preventDefault();
  };
  
  return (
    <div className="booking-container">
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

          <FormGroup className="booking__form d-inline-block me-4 mb-4">
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
            <input
              type="time"
              placeholder="Journey Time"
              className="time__picker"
            />
          </FormGroup>

          <FormGroup>
            <textarea
              rows={5}
              type="textarea"
              className="textarea"
              placeholder="Write"
            ></textarea>
          </FormGroup>
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
          <button className="reserve-btn">Reserve Now</button>
        </div>
      </div>
    </div>
  );
}

export default BookingForm;
