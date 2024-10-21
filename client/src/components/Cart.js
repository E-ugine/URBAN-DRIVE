import React, { useContext } from 'react';
import { CartContext } from '../context/CartContext';
import '../styles/cart.css';

function Cart() {
  const { cart, removeFromCart, clearCart } = useContext(CartContext);

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
              {/* Pass the car name to removeFromCart */}
              <button onClick={() => removeFromCart(car.name)}>Remove</button>
            </div>
          ))}
        </div>
      )}
      {cart.length > 0 && (
        <button className="clear-cart" onClick={clearCart}>
          Clear Cart
        </button>
      )}
    </div>
  );
}

export default Cart;
