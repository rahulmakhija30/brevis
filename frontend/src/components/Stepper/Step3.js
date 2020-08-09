import React from 'react'
import Accordion from '@material-ui/core/Accordion';
import AccordionSummary from '@material-ui/core/AccordionSummary';
import AccordionDetails from '@material-ui/core/AccordionDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { Button, Backdrop } from '@material-ui/core';
import StepStyle from './Step.module.css'
import Loader from '../Loader/Loader';
import io from 'socket.io-client'
import axios from 'axios';

const socket=io('http://localhost:5000',{transports:['websocket'],pingTimeout:14400000,pingInterval:7200000});

window.onbeforeunload = function () {
  console.log('refresh')
}; 



class Step3 extends React.Component{

    state={
        disabled:'true',
        buttondisabled:'true',
        open:'true',
        scrape:''
    }
    
    handleDownload = async() => {
      let res= await axios.get('/send/'+this.props.data.url.slice(32)+this.props.data.type,{responseType: 'blob'});
  
      let url = window.URL.createObjectURL(res.data);
      let a = document.createElement('a');
      a.href = url;
      a.download = 'Brevis_Notes.zip';
      a.click();
    }
    setSocketListeners(){
        console.log("listening")
        socket.on('response1',(json_result)=>{
        console.log("in response")
        console.log(json_result);
        this.setState({
          scrape:json_result,
          disabled:false,
          open:false
        });
        socket.emit('event2','junkdata')
        }

        )
        socket.on('response2',(resp)=>{
          console.log(resp)
          this.setState({downloadresponse:true,
        buttondisabled:false})
          //document.getElementById('LoadingMessage').style.visibility = "hidden";
        })
        this.props.onScrapeContent(this.state.scrape)
    }

    componentDidMount(){
        socket.emit('event1',this.props.data)
        this.setSocketListeners()
    }

    render(){
        if(this.state.disabled){
            var googleList=null;
            var youtubeList=null;
            var wikilist=null;
        }
        else{
        const {google,youtube,wikipedia}=this.state.scrape;
        var googleList=google.map(element=>{
          return(
            <div key={element.linktopage}>
              •<a href={element.linktopage} target="_blank">{element.title}</a>
            </div>
          )
        })
        var youtubeList=youtube.map(element=>{
          return(
            <div key={element.linktopage}>
              •<a href={element.linktopage} target="_blank">{element.title}</a>
            </div>
          )
        })
        var wikilist=wikipedia.map(element=>{
          return(
            <div key={element.title}>
              <p><b>{element.title}</b></p>
          <p>{element.definition}</p>
            </div>
          )
        })
    }
        return(
            <div>
                <Backdrop open={this.state.open} className={StepStyle.backdrop}>
                    <Loader></Loader>
                </Backdrop>
                <Button variant="contained" className={StepStyle.Button} component="span" onClick={this.handleDownload} disabled={this.state.buttondisabled}>
                    Download
                </Button>
                <p></p>
                <Accordion style={{width:'40%',marginLeft:'32%',borderRadius:'10px'}} disabled={this.state.disabled}>
                    <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel1a-content"
                    id="panel1a-header"
                    >
                    <Typography>Summary</Typography>
                    </AccordionSummary>
                    <AccordionDetails style={{overflowY:'scroll',maxHeight:'200px'}}>
                    <Typography>
                       {wikilist}
                    </Typography>
                    </AccordionDetails>
                </Accordion>
                <p></p>
                <Accordion style={{width:'40%',marginLeft:'32%',borderRadius:'10px'}} disabled={this.state.disabled}>
                    <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel1a-content"
                    id="panel1a-header"
                    >
                    <Typography>Video Links</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                    <Typography align="left">
                        {youtubeList}
                    </Typography>
                    </AccordionDetails>
                </Accordion>
                <p></p>
                <Accordion style={{width:'40%',marginLeft:'32%',borderRadius:'10px'}} disabled={this.state.disabled}>
                    <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel1a-content"
                    id="panel1a-header"
                    >
                    <Typography>Article Links</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                    <Typography  align="left">
                        {googleList}
                    </Typography>
                    </AccordionDetails>
                </Accordion>
                <p></p>
            </div>
        )
    }
}

export default Step3
