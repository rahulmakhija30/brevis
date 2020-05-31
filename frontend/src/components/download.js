import React from 'react';
import '../index.css'
import ReactPlayer from "react-player"

class DownloadFile extends React.Component {
	
	constructor(props) {
		super(props);
  }
  state={
    value:"both"
  }

  handleChange=(e)=>{
    this.setState({
      value:e.target.value
    });
  }
	
	handleDownload = () => {
		fetch('/send')
			.then(response => {
        console.log(response)
				response.blob().then(blob => {
          console.log(blob)
          let url = window.URL.createObjectURL(blob);
					let a = document.createElement('a');
					a.href = url;
					a.download = 'downloadfile.zip';
					a.click();
				});
				//window.location.href = response.url;
		});
	}
	
	render() {
    return (
    <div className="left-alignment">
      <div className="custom-select">
    <select onChange={this.handleChange} value={this.state.value}>
      <option value="both">Short Summary and Detailed Notes</option>
      <option value="shortsummary">Short Summary only</option>
      <option value="detailednotes">Detailed Notes only</option>
    </select>
      </div>
     <br></br>
     <ReactPlayer height="70%" width="90%" style={{padding: "10px", paddingLeft: "25%"}}
        url={this.props.url}/>
     <div className="Download-button"><button className="btn waves-effect waves-light" onClick={this.handleDownload}>Download</button></div>
    </div>
  );
	}

}

export default DownloadFile;