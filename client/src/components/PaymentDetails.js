import React, { useContext, useState } from 'react';
import { CartContext } from '../context/CartContext';
import '../styles/payment-details.css';

function PaymentDetails() {
  const { cart } = useContext(CartContext);
  const [numberOfDays, setNumberOfDays] = useState(1); 
  const [paymentConfirmed, setPaymentConfirmed] = useState(false);
  const [amountPaid, setAmountPaid] = useState(0);

  const handleDaysChange = (event) => {
    setNumberOfDays(Number(event.target.value));
  };

  const handlePayment = () => {
    const totalAmount = cart.reduce((total, car) => total + car.price * numberOfDays, 0);
    setAmountPaid(totalAmount);
    setPaymentConfirmed(true);
  };

  return (
    <div className="payment-details-container">
      <h2>Payment Details</h2>
      {cart.length === 0 ? (
        <p>Your cart is empty. Please add cars to proceed with payment.</p>
      ) : (
        <div>
          <h3>Your Cars:</h3>
          <ul>
            {cart.map((car) => (
              <li key={car.name}>
                {car.name} - ${car.price} / day
              </li>
            ))}
          </ul>
          <div className="rental-days">
            <label>
              Number of Days:
              <input
                type="number"
                value={numberOfDays}
                onChange={handleDaysChange}
                min="1"
              />
            </label>
          </div>
          <button onClick={handlePayment}>Pay</button>
          {paymentConfirmed && (
            <div className="payment-notification">
              <p>Payment Confirmed! Amount Paid: ${amountPaid}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default PaymentDetails;
