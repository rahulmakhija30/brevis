import React from 'react'
import ReactPlayer from "react-player"
import DownloadFile from './download'
import axios from 'axios';
import { BrowserRouter, Route } from 'react-router-dom';
import './Preview.css'
import {Link,NavLink} from 'react-router-dom'
import LoadingSpinner from './LoadingSpinner'


class Preview extends React.Component{ 
    state={
        value:"both",
        showdownload:false,
        loading:false
    }
    handleChange=(e)=>{
        this.setState({
          value:e.target.value
        });
      }

    handleSubmit = async() => {
      this.setState({loading:true},async() =>{
        let response= await axios.post('/download',this.state);
        console.log(response);})
        document.getElementById('Preview').style.visibility = "hidden";
        document.getElementById('Preview').disabled=true;
        document.getElementById('Inputfield').style.visibility = "hidden";
        document.getElementById('Inputfield').disabled=true;
        this.setState({
            showdownload:true
        })
      }
    render(){
        let download=null
        if(this.state.showdownload)
        { 
          return (
            <DownloadFile url={this.props.url} value={this.state.value}/> 
          )
        }
        else{
          return(
            <div>
              <ReactPlayer width="100%"
                          style={{
                              paddingLeft: "30%",
                              paddingRight: "30%",
                              paddingBottom: "20px",
                            }}
                          url={this.props.url}
                          className="animate__fadeIn animate__animated animate__slow"/>
             <div className="custom-select center-align dropdown">
                <select onChange={this.handleChange} value={this.state.value} className='browser-default animate__fadeIn animate__animated animate__slow'>
                  <option value="both">Short Summary and Detailed Notes</option>
                  <option value="shortsummary">Short Summary only</option>
                  <option value="detailednotes">Detailed Notes only</option>
                </select>
              </div>
              <div className="button center-align">
                <button className="btn waves-effect waves-light animate__fadeIn animate__animated animate__slow" type="submit" onClick={this.handleSubmit}>Generate</button>
              </div> 
              <div className="center-align bold">{this.state.loading ? <LoadingSpinner /> : ""}</div>
            </div>
          )
      }
}
}

export default Preview;