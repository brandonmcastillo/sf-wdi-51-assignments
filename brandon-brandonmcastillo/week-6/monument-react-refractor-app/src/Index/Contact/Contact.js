import React, { Component } from "react";

class Form extends Component {
    render() {
        return (

	<section id="contact">
		<div class="wrap">
			<h2>Get in Touch</h2>
			<form class="contact">
				<input type="text" placeholder="Full Name" class="col-third"></input>
				<input type="email" placeholder="Email" class="col-third"></input>
				<input type="text" placeholder="Subject" class="col-third"></input>
				<textarea name="" id="" cols="30" rows="10" placeholder="Message"></textarea>
				<button type="submit">Submit</button>
			</form>
		</div>
	</section>
    );
  }
}
export default Form;