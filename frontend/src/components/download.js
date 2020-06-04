import React from 'react';
import '../index.css'
import axios from 'axios';

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
	
	handleDownload = async() => {
    let response= await axios.post('/download',this.state);
        console.log("helloworld",response)
       let res= await axios.get('/send/'+this.props.url.slice(32)+this.state.value,{responseType: 'blob'});
          console.log("heyyy",res)
        //res.data.blob()
        //.then(blob => {
          //console.log(blob)
          let url = window.URL.createObjectURL(res.data);
          console.log(url)
					let a = document.createElement('a');
					a.href = url;
					a.download = 'brevis_notes2.zip';
					a.click();
				//});
        //window.location.href = response.url;
        

   /* const method = 'GET';

    const url = '/download';

    axios

      .request({

        url,

        method,

        responseType: 'blob', //important

      })

      .then(({ data }) => {

        const downloadUrl = window.URL.createObjectURL(new Blob([data]));

        const link = document.createElement('a');

        link.href = downloadUrl;

        link.setAttribute('download', 'brevis_notes2.zip'); //any other extension

        document.body.appendChild(link);

        link.click();

        link.remove();

      })
      .catch((error)=>{

        console.log(error.response)

      });*/
    
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