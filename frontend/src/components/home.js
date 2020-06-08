import React from 'react';
import axios from 'axios';
import DownloadFile from './download';
import './home.css'
import Preview from './Preview'
import LoadingSpinner from './LoadingSpinner'

class Home extends React.Component {

 state={
   url:'',
   validurl:false,
   loading: false
 }
  handleChange=(event)=> {
    this.setState({url:event.target.value});
  }

  handleSubmit=(event)=> {
    console.log(this.state)
    this.setState({loading:true} , () => {
      axios.post('/result',this.state)
      .then(res=>{
        axios.get('/res')
        .then(response=>{
        
          let download=null;
          if(response.data.result==1)
            {
              this.setState({
                validurl:true,
                loading:false
              });
              document.getElementById('disp').innerHTML=""
          }
          else{
              this.setState({
                validurl:false,
                loading:false
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
                this.setState({
                  loading:false
                })
                console.log(error.name)
                document.getElementById("disp").innerHTML=error.message;
            }
          }
          
          )
      },(error) => {
        
        if (error) {
          this.setState({
            loading:false
          })
            console.log(error.name)
            document.getElementById("disp").innerHTML='Please check the link again!';
        }
      }

      );
    })
}

  render() {
    let preview=null;
    if(this.state.validurl)
    {
      preview=<Preview url={this.state.url}/>;
    }
    return (
      <div>
        <h1 className="brevis-home center-align middle-align animate__fadeIn animate__animated animate__slow">BREVIS</h1>
        <div className="center-align middle-align animate__fadeIn animate__animated animate__slow" id="Inputfield">
          <input type="text" className="input" placeholder="Enter Link" onChange={this.handleChange}></input>
        </div>  
          <div className="button center-align">
          <button className="btn waves-effect waves-light animate__fadeIn animate__animated animate__slow" type="submit" onClick={this.handleSubmit} id="Preview">Preview</button>
        </div> 
        <p></p>
        <div className="center-align bold">{this.state.loading ? <LoadingSpinner /> : ""}</div>
        <p id="disp" className="center-align"></p>
        {preview}
      </div>
    );
  }
}

export default Home;