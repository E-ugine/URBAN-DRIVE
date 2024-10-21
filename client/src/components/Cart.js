import React, { useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { CartContext } from '../context/CartContext';
import '../styles/cart.css';

function Cart() {
  const { cart, removeFromCart, clearCart } = useContext(CartContext);
  const [days, setDays] = useState(1); 
  const navigate = useNavigate();

  const handleProceedToPay = () => {
    if (cart.length === 0) {
      alert('Your cart is empty!');
      return;
    }
    navigate('/rental-details', { state: { cart, days } });
  };

  return (
    <div className="cart-page">
      <h1>Your Cart</h1>
      {cart.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <div className="cart-items">
          {cart.map((car) => (
            <div key={car.name} className="cart-item">
              <img src={car.image_url} alt={car.name} />
              <h3>{car.name}</h3>
              <p>${car.price} / day</p>
              <button onClick={() => removeFromCart(car.name)}>Remove</button>
            </div>
          ))}
        </div>
      )}
      {cart.length > 0 && (
        <>
          <label htmlFor="days">Number of days:</label>
          <input
            id="days"
            type="number"
            value={days}
            onChange={(e) => setDays(e.target.value)}
            min="1"
          />
          <button className="clear-cart" onClick={clearCart}>
            Clear Cart
          </button>
          <button className="proceed-btn" onClick={handleProceedToPay}>
            Proceed to Pay
          </button>
        </>
      )}
    </div>
  );
}

export default Cart;
