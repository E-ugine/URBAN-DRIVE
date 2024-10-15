import React from 'react';
import { Facebook, Twitter, Instagram, Mail, PhoneCall, MapPin } from 'lucide-react';
import "./footer.css"

const Footer = () => {
  return (
    <footer className="bg-dark text-light py-5" id="footer">
      <div className="container">
        <div className="footer-content">
          {/* About Section */}
          <div className="mb-4">
            <h5 className="text-uppercase mb-4">About CarBook</h5>
            <p className="small">
              Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.
            </p>
            <div className="mt-3">
              <a href="https://www.facebook.com" className="text-light me-3" aria-label="Facebook">
                <Facebook size={20} />
              </a>
              <a href="https://www.twitter.com" className="text-light me-3" aria-label="Twitter">
                <Twitter size={20} />
              </a>
              <a href="https://www.instagram.com" className="text-light" aria-label="Instagram">
                <Instagram size={20} />
              </a>
            </div>
          </div>

          {/* Information Section */}
          <div className="mb-4">
            <h5 className="text-uppercase mb-4">Information</h5>
            <ul className="list-unstyled small">
              <li><a href="#" className="text-light text-decoration-none d-block mb-2">About</a></li>
              <li><a href="#" className="text-light text-decoration-none d-block mb-2">Services</a></li>
              <li><a href="#" className="text-light text-decoration-none d-block mb-2">Terms and Conditions</a></li>
              <li><a href="#" className="text-light text-decoration-none d-block mb-2">Best Price Guarantee</a></li>
              <li><a href="#" className="text-light text-decoration-none d-block">Privacy &amp; Cookies Policy</a></li>
            </ul>
          </div>

          {/* Customer Support Section */}
          <div className="mb-4">
            <h5 className="text-uppercase mb-4">Customer Support</h5>
            <ul className="list-unstyled small">
              <li><a href="#" className="text-light text-decoration-none d-block mb-2">FAQ</a></li>
              <li><a href="#" className="text-light text-decoration-none d-block mb-2">Payment Option</a></li>
              <li><a href="#" className="text-light text-decoration-none d-block mb-2">Booking Tips</a></li>
              <li><a href="#" className="text-light text-decoration-none d-block mb-2">How it works</a></li>
              <li><a href="#" className="text-light text-decoration-none d-block">Contact Us</a></li>
            </ul>
          </div>

          {/* Contact Section */}
          <div className="mb-4">
            <h5 className="text-uppercase mb-4">Have a Question?</h5>
            <ul className="list-unstyled small">
              <li className="mb-3 d-flex">
                <MapPin size={20} className="me-2" />
                <span>203 Fake St. Mountain View, San Francisco, California, USA</span>
              </li>
              <li className="mb-3 d-flex">
                <PhoneCall size={20} className="me-2" />
                <a href="tel:+23923929210" className="text-light text-decoration-none">+2 392 3929 210</a>
              </li>
              <li className="d-flex">
                <Mail size={20} className="me-2" />
                <a href="mailto:info@yourdomain.com" className="text-light text-decoration-none">info@yourdomain.com</a>
              </li>
            </ul>
          </div>

          {/* Newsletter Section */}
          <div className="mb-4">
            <h5 className="text-uppercase mb-4">Newsletter</h5>
            <form>
              <div className="form-group mb-2">
                <input 
                  type="email" 
                  className="form-control form-control-sm mb-2" 
                  placeholder="Enter email address" 
                />
                <button type="submit" className="btn btn-primary btn-sm w-100">Subscribe</button>
              </div>
            </form>
          </div>
        </div>

        {/* Footer Bottom */}
        <div className="text-center mt-5">
          <p className="small mb-0">
            &copy; {new Date().getFullYear()} All rights reserved
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
