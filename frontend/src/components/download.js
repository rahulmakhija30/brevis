

import React from 'react';


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
          console.log(url)
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
    <div>
      Choose according to your requirement
      <p>
      <label>
        <input name="group1" type="radio" value="both" checked={this.state.value === 'both'} 
      onChange={this.handleChange} />
        <span>Both</span>
      </label>
    </p>
    <p>
      <label>
        <input name="group1" type="radio" value="shortsummary"  checked={this.state.value === 'shortsummary'} 
     onChange={this.handleChange} />
        <span>Short Summary</span>
      </label>
    </p>
    <p>
      <label>
        <input  name="group1" type="radio" value="detailednotes" checked={this.state.value === 'detailednotes'} 
      onChange={this.handleChange}  />
        <span>Detailed Notes </span>
      </label>
    </p>
     <br></br>
    <button className="waves-effect waves-light btn" onClick={this.handleDownload}>Download</button>
    </div>
  );
	}

}

export default DownloadFile;