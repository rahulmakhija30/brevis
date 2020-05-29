import React,{Component} from 'react';
import {Link,NavLink} from 'react-router-dom'
import './Navbar.css'

class Navbar extends Component {
  render(){
  return (
    <div>
      <div id="mySidenav" className="mysidenav">
          <a href="javascript:void(0)" className="closebtn" onClick={window.closeNav}>&times;</a>
          <Link to='/'>Home</Link>
          <Link to='/about'>About</Link>
      </div>
      <span className="openbtn" onClick={window.openNav}>&#9776;</span>      
  </div>
  )}
}

export default Navbar;
