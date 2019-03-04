import React, { Component } from "react";
import "./index.css";
import "./app.css";
// import Navbar from "./Navbar/Navbar.js";
// import Header from "./Index/Header/Header.js";
// import Article from "./Index/Archive/Article.js";
// import About from "./Index/About/About.jsx";
// import Gallery from "./Index/Gallery/Gallery.js";
// import Form from "./Index/Contact/Contact.js";
// import Footer from "./Footer/Footer.js"
// import {BrowserRouter as Router} from 'react-router-dom';

// class App extends Component {
//   render() {
//     return (
//       <Router>
//         <div className="Main">
//           <Navbar />
//             <div className="Index">
//               <Header />
//               <Article />
//               <About />
//               <Gallery />
//               <Form /> 
//             </div>  
//               <Footer/>
//           </div>
//         </Router>
//     );
//   }
// }

// export default App;

// Blog code
import HeaderBlog from './IndexBlog/Header/HeaderBlog'
import Main from './IndexBlog/Main/Main'
import ContactBlog from './IndexBlog/Contact/ContactBlog';

const Blog = () => {
    return (
        <div>
            <HeaderBlog />
            <Main />
            <ContactBlog />
        </div>
    )
}

export default Blog;
