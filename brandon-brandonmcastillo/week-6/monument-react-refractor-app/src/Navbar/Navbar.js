import React, { Component } from "react";
// import Gallery from "../Index/Gallery/Gallery"
// import Form from "../Index/Contact/Contact"
// import About from "../Index/About/About"
import {
  Route,
  Link,
  Switch
} from 'react-router-dom';

class Navbar extends Component {
  render() {
    return (
      // all jsx
  <div className="Nav">
    <nav>
      <ul>
        <li><Link to ="#about">About</Link></li>
        <li><Link to="#gallery">Gallery</Link></li>
        <li><Link to="blog.html">Blog</Link></li>
        <li><Link to="#contact">Contact</Link></li>
      </ul>
    </nav> 
    <div>
      <Switch>
        <Route path="about" />
        <Route path="gallery"/>
        <Route path="blog.html" />
        <Route path ="contact" />
      </Switch>
    </div>
  </div>
     
    );
  }
}
export default Navbar;
