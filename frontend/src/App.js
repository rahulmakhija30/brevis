import React from 'react'
import {Navbar,Footer,StepComponent} from './components'
import { Container } from '@material-ui/core'
import { Typography } from '@material-ui/core'
import Home from './components/Home/Home'
import {BrowserRouter as Router, Route} from 'react-router-dom'

class App extends React.Component{
  render(){
    return(
      <div>
      <Router>
        <Navbar/>
        <div>
            <Container maxWidth='lg'>
              <Route to='/' component={Home}/>
              <Footer></Footer>  
            </Container>
        </div>
        </Router>
      </div>
    )
  }
}

export default App