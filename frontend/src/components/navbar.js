import React,{Component} from 'react';
import {Link,NavLink} from 'react-router-dom'
import './Navbar.css'

class Navbar extends Component {
  render(){
  return (
    <div>
      <div id="mySidenav" className="mysidenav">
          <div className="tooltip">
            <Link to='/'><i class="medium material-icons">home</i></Link>
            <span className="tooltiptext">Home</span>
          </div>
          <div className="tooltip">
            <Link to='/about'><i class="medium material-icons">face</i></Link>
            <span className="tooltiptext" container="body">About</span>  
          </div>    
      </div>   
  </div>
  )}
}

export default Navbar;
