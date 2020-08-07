import React from 'react'
import {Navbar,Footer,StepComponent} from './components'
import { Container } from '@material-ui/core'
import { Typography } from '@material-ui/core'
import Home from './components/Home/Home'
import {BrowserRouter as Router, Route} from 'react-router-dom'
import Style from './App.module.css'
import About from './components/About/About'

class App extends React.Component{
  render(){
    return(
      <div>
      <Router>
        <Navbar/>
        <div className={Style.contentWrap}>
            <Container maxWidth='lg'>
              <Route exact path='/' component={Home}/> 
              <Route exact path='/about' component={About}/>
            </Container>
        </div>
        <Footer></Footer> 
        </Router>
      </div>
    )
  }
}

export default App
