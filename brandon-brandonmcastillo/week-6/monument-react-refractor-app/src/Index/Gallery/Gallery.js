import React, { Component } from "react";
import imageOne from "./gallery_1.jpg";
import imageThree from "./gallery_3.jpg";
import imageFour from "./gallery_4.jpg";
import imageTwo from "./gallery_2.jpg";
import imageFive from "./gallery_5.jpg";
import imageSix from "./gallery_6.jpg";
class Gallery extends Component {
    render() {
        return (
  <section id="gallery">
		<div class="wrap">
			<h2>Issue Twenty</h2>
			<h3>A visual guide to the Southwest</h3>
				<div class="masonry">
					<img src={imageOne} alt=""></img>
					<img src={imageThree} alt=""></img>
					<img src={imageFour} alt=""></img>
					<img src={imageTwo} alt=""></img>
					<img src={imageFive} alt=""></img>
					<img src={imageSix} alt=""></img>
				</div>
		</div>
	</section>
    )
  }
}
export default Gallery;