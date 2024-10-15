import React from "react";
import '../styles/navbar.css'
import UserDetails from "./UserDetails";

function Navbar(){
    return(
        <header>
        <h1>Urban<em>Drive</em></h1>
        <nav>
            <ul> 
              <li > <a href="/Home">Home</a> </li> 
              <li > <a href="/About">About</a> </li> 
              <li > <a href="/Cars">Cars</a> </li> 
              <li > <a href="/Contacts">Contacts</a> </li>
            </ul>
        </nav>
        <UserDetails/>
        </header>
    )
}
export default Navbar;