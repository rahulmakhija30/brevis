import React from 'react'
import ReactPlayer from "react-player"
import DownloadFile from './download'
import axios from 'axios';
import { BrowserRouter, Route } from 'react-router-dom';




class Preview extends React.Component{ 
    state={
        value:"both",
        showdownload:false
    }
    handleChange=(e)=>{
        this.setState({
          value:e.target.value
        });
      }

      handleSubmit = async() => {
        let response= await axios.post('/download',this.state);
        console.log(response)
        this.setState({
            showdownload:true
        })
      }
    render(){
        let download=null
        if(this.state.showdownload)
        {
            download=<DownloadFile url={this.props.url} value={this.state.value} />
        }
    return(

        <div>
            <ReactPlayer height="70%" 
                        width="90%" 
                        style={{
                            padding: "10px",
                            paddingLeft: "25%",
                            borderRadius:"20px",
                        }}
                        url={this.props.url}/>
         <div className="custom-select">
        <select onChange={this.handleChange} value={this.state.value} class='browser-default'>
          <option value="both">Short Summary and Detailed Notes</option>
          <option value="shortsummary">Short Summary only</option>
          <option value="detailednotes">Detailed Notes only</option>
        </select>
        </div>
         <div className="button center-align">
          <button className="btn waves-effect waves-light animate__fadeIn animate__animated animate__slow" type="submit" onClick={this.handleSubmit}>Generate</button>
        </div> 
        {download}
        </div>
    )
}
}

export default Preview;