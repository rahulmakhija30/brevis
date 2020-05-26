import React from 'react';
import {Link,NavLink} from 'react-router-dom'


const Navbar=()=> {
  return (
      <nav className="nav-wrapper blue">
        <div>
          <ul >
              <li><Link to='/'>Home</Link></li>
              <li><Link to='/about'>About</Link></li>


          </ul>

      </div>
      </nav>
  );
}

export default Navbar
