import React from 'react'
import ReactPlayer from "react-player"
import DownloadFile from './download'
import axios from 'axios';
import { BrowserRouter, Route } from 'react-router-dom';
import './Preview.css'
import {Link,NavLink} from 'react-router-dom'
import LoadingSpinner from './LoadingSpinner'
import Collapsible from './collapsible'
import io from 'socket.io-client'

const socket=io('http://localhost:5000',{transports:['websocket'],pingTimeout:3600000,pingInterval:180000});


class Preview extends React.Component{ 
    state={
        value:"both",
        showdownload:false,
        loading:false,
        scrape:{},
        downloadresponse:false
    }
    handleChange=(e)=>{
        this.setState({
          value:e.target.value
        });
      }

      setSocketListeners(){
        console.log("listening")
        socket.on('response1',(json_result)=>{
        console.log("in response")
        console.log(json_result);
        this.setState({
          showdownload:true,
          scrape:json_result
        });
        socket.emit('event2','junkdata')
        
        }

        )
        socket.on('response2',(resp)=>{
          console.log(resp)
          this.setState({downloadresponse:true})
          //document.getElementById('LoadingMessage').style.visibility = "hidden";
        })
      }
      componentDidMount(){
        this.setSocketListeners()
      }
    handleSubmit =() => {
        this.setState({
          loading:true
        })
        document.getElementById('Preview').style.visibility = "hidden";
        document.getElementById('Inputfield').style.visibility = "hidden";
        document.getElementById('Preview').disabled=true;
        document.getElementById('Inputfield').disabled=true;

        socket.emit('event1',this.state)
        //let response= await axios.post('/download',this.state);
        //console.log(response);
        //const scrape=response.data;
        //console.log({scrape});
        //this.setState({
          //  showdownload:true,
            //scrape:scrape,
           // loading: false
        //})
        //let res= await axios.get('/down');
        //console.log({res})
        //this.setState({downloadresponse:true})
        //document.getElementById('LoadingMessage').style.visibility = "hidden";
      }
    render(){
        let download=null
        if(this.state.downloadresponse)
        { 
          return (
            <div>
              <Collapsible scrape={this.state.scrape}/>
              <DownloadFile url={this.props.url} value={this.state.value}/> 
            </div>
          )
        }
        else if(this.state.showdownload){
          return(
          <div>
          <Collapsible scrape={this.state.scrape}/>
          <p className="center" id="LoadingMessage">Your File is being Prepared ...</p>
          </div>)
        }
        else if(this.state.loading){
          return(
            <div className="center-align bold">{this.state.loading ? <LoadingSpinner /> : ""}</div>
          )
        }
        else{
          return(
            <div>
              <ReactPlayer width="100%"
                          style={{
                              paddingLeft: "35%",
                              paddingRight: "35%",
                              paddingBottom: "60px",
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
            </div>
          )
      }
}
}

export default Preview;