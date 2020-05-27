import React from 'react';
import axios from 'axios';
import Home from './components/home'
import { BrowserRouter, Route } from 'react-router-dom';
import Navbar from './components/navbar'
import About from './components/about'



class App extends React.Component {  

  render() {
    return (
      <BrowserRouter>
      <div >
        <Navbar />
        <h1 className="center">BREVIS</h1>
        <Route  exact path='/' component={Home} />
        <Route path='/about' component={About} />
        
       
      </div>
      </BrowserRouter>
    );
  }
}

export default App;