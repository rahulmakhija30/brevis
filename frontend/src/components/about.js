import React from 'react';
import './About.css';
import image from './profileimages/image.jpg'

const About=()=> {
  return (
    <div >
    <h1 className="about-brevis">BREVIS</h1>
        <p className="about-heading">About Us</p>
        <p className="about-content">Lorem ipsum dolor sit amet consectetur adipisicing elit.
         Natus dolores hic eius adipisci quam, consequatur est, beatae fugiat 
         architecto suscipit sed officiis consectetur ut? 
         Dicta consequatur nobis earum ullam eos.
        </p>
        <p className="heading">Our Team</p>
        <div className="left-alignment-1">
        <div class="w3-card">
          <h4 className="CardHead">Name</h4>
          <p className="content">
          <img src={image}/>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Natus dolores hic eius adipisci quam, consequatur est, beatae fugiat 
          architecto suscipit sed officiis consectetur ut? 
          Dicta consequatur nobis earum ullam eos.</p>  
        </div>
        </div>
        <div className="left-alignment-2">
        <div class="w3-card">
          <h4 className="CardHead">Name</h4>
          <p className="content">
          <img src={image}/>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Natus dolores hic eius adipisci quam, consequatur est, beatae fugiat 
          architecto suscipit sed officiis consectetur ut? 
          Dicta consequatur nobis earum ullam eos.</p>  
        </div>
        </div>
        <div className="left-alignment-1">
        <div class="w3-card">
          <h4 className="CardHead">Name</h4>
          <p className="content">
          <img src={image}/>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Natus dolores hic eius adipisci quam, consequatur est, beatae fugiat 
          architecto suscipit sed officiis consectetur ut? 
          Dicta consequatur nobis earum ullam eos.</p>  
        </div>
        </div>
        <div className="left-alignment-2">
        <div class="w3-card">
          <h4 className="CardHead">Name</h4>
          <p className="content">
          <img src={image}/>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Natus dolores hic eius adipisci quam, consequatur est, beatae fugiat 
          architecto suscipit sed officiis consectetur ut? 
          Dicta consequatur nobis earum ullam eos.</p>  
        </div>
        </div>

        <p className="heading">Our Mentors</p>
        <div className="left-alignment-1">
        <div class="w3-card">
          <h4 className="CardHead">Name</h4>
          <p className="content">
          <img src={image}/>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Natus dolores hic eius adipisci quam, consequatur est, beatae fugiat 
          architecto suscipit sed officiis consectetur ut? 
          Dicta consequatur nobis earum ullam eos.</p>  
        </div>
        </div>
        <div className="left-alignment-2">
        <div class="w3-card">
          <h4 className="CardHead">Name</h4>
          <p className="content">
          <img src={image}/>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Natus dolores hic eius adipisci quam, consequatur est, beatae fugiat 
          architecto suscipit sed officiis consectetur ut? 
          Dicta consequatur nobis earum ullam eos.</p>  
        </div>
        </div>
        
    </div>
  );
}

export default About
