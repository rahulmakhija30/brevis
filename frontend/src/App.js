import React from 'react';
import axios from 'axios';
import Home from './components/home'
import { BrowserRouter, Route } from 'react-router-dom';
import Navbar from './components/navbar'
import About from './components/about'
import Footer from './components/footer';
import DownloadFile from './components/download';





class App extends React.Component {  

  render() {
    return (
      <BrowserRouter>
      <Navbar />
      <div id="main">
       <Route  exact path='/' component={Home} />
       <Route path='/about' component={About} />
       
      </div>
      <div className="footer">
        <Footer/>
      </div>
      </BrowserRouter>
    );
  }
}

export default App;