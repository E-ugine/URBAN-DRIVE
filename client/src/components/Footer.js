import React from 'react';
import { Facebook, Twitter, Instagram, Mail, PhoneCall, MapPin } from 'lucide-react';
import "../styles/Footer.css";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        {/* About Section */}
        <div className="footer-section">
          <h5>About UrbanDrive</h5>
          <p className="small">
            Comfort, Luxury, and Efficiency on the go!
          </p>
          <div className="social-icons">
            <a href="https://www.facebook.com" aria-label="Facebook">
              <Facebook size={20} />
            </a>
            <a href="https://www.twitter.com" aria-label="Twitter">
              <Twitter size={20} />
            </a>
            <a href="https://www.instagram.com" aria-label="Instagram">
              <Instagram size={20} />
            </a>
          </div>
        </div>

        {/* Information Centre */}
        <div className="footer-section">
          <h5>Information</h5>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Cars</a></li>
            <li><a href="#">Services</a></li>
          </ul>
        </div>

        {/* Customer Support */}
        <div className="footer-section">
          <h5>Customer Support</h5>
          <ul>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Payment Option</a></li>
            
          </ul>
        </div>

        {/* Contact */}
        <div className="footer-section">
          <h5>Have a Question?</h5>
          <ul>
            <li>
              <MapPin size={20} />
              <span>43 Ngong Lane, Ngong, Nairobi, Kenya</span>
            </li>
            <li>
              <PhoneCall size={20} />
              <a href="tel:+254712345678">+254 712345678</a>
            </li>
            <li>
              <Mail size={20} />
              <a href="mailto:info@example.com">info@example.com</a>
            </li>
          </ul>
        </div>

        {/* Newsletter */}
        <div className="footer-section">
          <h5>Newsletter</h5>
          <form>
            <input type="email" placeholder="Enter email address" />
            <button type="submit">Subscribe</button>
          </form>
        </div>
      </div>

      {/* Rights */}
      <div className="footer-bottom">
        <p>&copy; {new Date().getFullYear()} All rights reserved</p>
      </div>
    </footer>
  );
};

export default Footer;