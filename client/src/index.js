import React, { useEffect, useRef, useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import debounce from 'lodash/debounce';

// const YourComponent = ({ callback, debounceTime = 300 }) => {
//   const ref = useRef(null); 
//   const [elementSize, setElementSize] = useState({ width: 0, height: 0 });

//   useEffect(() => {
//     const observeTarget = ref.current;
//     if (!observeTarget) return;

//     const debouncedCallback = debounce((entry) => {
//       setElementSize({
//         width: entry.contentRect.width,
//         height: entry.contentRect.height,
//       });
//       if (callback && typeof callback === 'function') {
//         callback(entry.contentRect);
//       }
//     }, debounceTime);

//     const resizeObserver = new ResizeObserver((entries) => {
//       if (!Array.isArray(entries) || !entries.length) return;

//       const entry = entries[0];
//       debouncedCallback(entry);
//     });

//     resizeObserver.observe(observeTarget);

//     return () => {
//       if (resizeObserver && observeTarget) {
//         resizeObserver.unobserve(observeTarget);
//       }
//     };
//   }, [ref, callback, debounceTime]);

//   return (
//     <div ref={ref}>
//       <p>Current width: {elementSize.width}</p>
//       <p>Current height: {elementSize.height}</p>
//     </div>
//   );
// };

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    {/* Example usage of YourComponent */}
    {/* <YourComponent /> */}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
