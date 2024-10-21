import React, { createContext, useState } from 'react';

export const CartContext = createContext();

export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState([]);

  const addToCart = (car) => {
    setCart((prevCart) => [...prevCart, car]);
  };

  const removeFromCart = (carName) => {
    setCart((prevCart) => prevCart.filter((car) => car.name !== carName));
  };
  

  const clearCart = () => {
    setCart([]);
  };

  return (
    <CartContext.Provider value={{ cart, addToCart, removeFromCart, clearCart }}>
      {children}
    </CartContext.Provider>
  );
};
