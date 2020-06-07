import React from 'react';
import axios from 'axios';
import DownloadFile from './download';
import './home.css'


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
     

      axios.get('/res')
      .then(response=>{
       
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
          
          if (error) {
              
              console.log(error.name)
              document.getElementById("disp").innerHTML=error.message;
          }
        }
        
        )
    },(error) => {
      
      if (error) {
          
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
        <h1 className="brevis-home center-align middle-align animate__fadeIn animate__animated animate__slow">BREVIS</h1>
        <div className="center-align middle-align animate__fadeIn animate__animated animate__slow">
          <input type="text" className="input" placeholder="Enter Link"></input>
        </div>  
          <div className="button center-align">
          <button className="btn waves-effect waves-light animate__fadeIn animate__animated animate__slow" type="submit" onClick={this.handleSubmit}>Preview</button>
        </div> 
        <p></p>
        <p id="disp"></p>
        {download}
      </div>
    );
  }
}

export default Home;