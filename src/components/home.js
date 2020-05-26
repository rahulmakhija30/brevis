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
        if(response.data.result)
          {
            this.setState({
              validurl:true
            });
          }
        else{
          document.getElementById('fail').innerHTML='Not an educational video!'
        }
        
        },(error) => {
          //console.log("3")
          if (error) {
              //console.log("4")
              console.log(error.name)
              document.getElementById("fail").innerHTML=error.message;
          }
        }
        
        )
    },(error) => {
      //console.log("3")
      if (error) {
          //console.log("4")
          console.log(error.name)
          document.getElementById("fail").innerHTML='Please check the link again!';
      }
    }

    );
  
}

  render() {
    let download=null;
    if(this.state.validurl)
    {
      download=<DownloadFile/>;
    }
    return (
      <div className="container">
        <input type="text" onChange={this.handleChange} placeholder="Enter the link"></input>
        <button class="btn waves-effect waves-light" type="submit" onClick={this.handleSubmit}>Submit
      </button> 
      <p></p>
        <p id="fail"></p>
        {download}
        
      </div>
    );
  }
}

export default Home;