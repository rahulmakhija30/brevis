import React,{Component} from 'react';
import {Link,NavLink} from 'react-router-dom'
import style from './Nav.module.css'
import home from './home-run.png'
import lightbulb from './lightbulb.png'
import info from './info.png'
import night from './night.png'
import {Tooltip, Zoom} from '@material-ui/core'
import {Mode} from '../Functions'
import sun from './sun.png'

document.body.classList.add("Nav_BodyLightMode__2olZR")

class Navbar extends Component {
  
  render(){
  return (
    <div>
      <div id='mySidenav' className={`${style.mysidenav} ${style.LightMode}`}>
        <span className={style.dot}></span>  
        <Tooltip title="HOME" arrow placement='right' TransitionComponent={Zoom} classes={{ tooltip: style.popper}} margin-top={10}>
            <Link to='/'><img id='homeicon' src={home} className={style.about} alt=""/></Link>
        </Tooltip>
        <Tooltip title="SUGGESTIONS" arrow placement='right' TransitionComponent={Zoom} classes={{ tooltip: style.popper}}>  
            <Link to='/suggestions'><img id='suggestionsicon' src={lightbulb} className={style.about} alt=""/></Link>
        </Tooltip>

        <Tooltip title="ABOUT" arrow placement='right' TransitionComponent={Zoom} classes={{ tooltip: style.popper}}>          
            <a href='/about'><img src={info} className={style.about} alt="" id='abouticon'/></a>  
        </Tooltip>
            
        <Tooltip title="" arrow placement='right' TransitionComponent={Zoom}>
          <img id="Image" src={night} className={style.night} alt="" onClick={Mode}/>
        </Tooltip>
      </div>   
  </div>
  )}
}

export default Navbar;
