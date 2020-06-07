import React from 'react';
import '../index.css'
import axios from 'axios';
import ReactPlayer from "react-player"

class DownloadFile extends React.Component {
	
	constructor(props) {
		super(props);
  }
	
	handleDownload = async() => {
    
    let res= await axios.get('/send/'+this.props.url.slice(32)+this.props.value,{responseType: 'blob'});

    let url = window.URL.createObjectURL(res.data);
		let a = document.createElement('a');
		a.href = url;
		a.download = 'brevis_notes2.zip';
		a.click();
	}
	
	render() {
    return (
      
    <div>
      <div className="Download-button"><button className="btn waves-effect waves-light" onClick={this.handleDownload}>Download</button></div>
    </div>
  );
	}

}

export default DownloadFile;