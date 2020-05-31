import React from 'react';
import axios from 'axios';
import DownloadFile from './download'


class Home extends React.Component {

 state={
   url:'',
   validurl:false
 }
  handleChange=(event)=> {
    this.setState({url:event.target.value});
  }

  handleSubmit=(event)=> {
    console.log(this.state)
    axios.post('/result',this.state)
    .then(res=>{
      console.log("HHH", res)
     

      axios.get('/res')
      .then(response=>{
        console.log("III",response)
        //document.getElementById('print').innerHTML=response.data.result;
        let download=null;
        if(response.data.result==1)
          {
            this.setState({
              validurl:true
            });
            document.getElementById('disp').innerHTML=""
          }
        else{
            this.setState({
              validurl:false
            });
            if(response.data.result==0)
            {
              document.getElementById('disp').innerHTML='Transcripts for the video do not exist!'
            }
            else{
          document.getElementById('disp').innerHTML='Not an educational video!'
            }
        }
        
        },(error) => {
          //console.log("3")
          if (error) {
              //console.log("4")
              console.log(error.name)
              document.getElementById("disp").innerHTML=error.message;
          }
        }
        
        )
    },(error) => {
      //console.log("3")
      if (error) {
          //console.log("4")
          console.log(error.name)
          document.getElementById("disp").innerHTML='Please check the link again!';
      }
    }

    );
  
}

  render() {
    let download=null;
    if(this.state.validurl)
    {
      download=<DownloadFile url={this.state.url}/>;
    }
    return (
      <div>
      <h1 className="brevis">BREVIS</h1>
        <p className="left-alignment">
          <input type="text" onChange={this.handleChange} placeholder="Enter the link"></input>
        </p>
        <div className="button">
          <button className="btn waves-effect waves-light" type="submit" onClick={this.handleSubmit}>Submit</button>
        </div> 
        <p></p>
        <p id="disp" className="left-alignment"></p>
          {download}
      </div>
    );
  }
}

export default Home;