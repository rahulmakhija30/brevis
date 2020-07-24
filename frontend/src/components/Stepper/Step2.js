import React from 'react'
import ReactPlayer from "react-player"
import { Typography, Backdrop, CircularProgress, FormControl, InputLabel, Select, MenuItem, FormHelperText, Button } from '@material-ui/core'
import Stepstyle from './Step.module.css'
import { DarkStep2 } from '../Functions'
import Loader from '../Loader/Loader'
import io from 'socket.io-client'

const socket=io('http://localhost:5000',{transports:['websocket'],pingTimeout:3600000,pingInterval:180000});

class Step2 extends React.Component{

    state={
        open: true,
        type:'Both',
        disabled:true,
        scrape:''
    }

    handleChange = (event) => {
        this.setState({type:event.target.value})
    };

    handleClose=()=>{
        this.setState({open:false,disabled:false})
    }

    setSocketListeners(){
        console.log("listening")
        socket.on('response1',(json_result)=>{
        console.log("in response")
        console.log(json_result);
        this.setState({
          scrape:json_result
        });
        socket.emit('event2','junkdata')
        }

        )
        socket.on('response2',(resp)=>{
          console.log(resp)
          this.setState({downloadresponse:true})
          //document.getElementById('LoadingMessage').style.visibility = "hidden";
        })
        this.props.onScrapeContent(this.state.scrape)
    }

    componentDidMount(){
        DarkStep2()
        this.setSocketListeners()
    }

    handleOnClick=() => {
        this.props.onNext()
        socket.emit('event1',this.state)
        this.setState({open:true})
        //let response= await axios.post('/download',this.state);
        //console.log(response);
        //const scrape=response.data;
        //console.log({scrape});
        //this.setState({
          //  showdownload:true,
            //scrape:scrape,
           // loading: false
        //})
        //let res= await axios.get('/down');
        //console.log({res})
        //this.setState({downloadresponse:true})
        //document.getElementById('LoadingMessage').style.visibility = "hidden";
    }

    render(){
        console.log(this.props)
        return(
            <div>
            <Backdrop open={this.state.open} className={Stepstyle.backdrop}>
                <Loader></Loader>
            </Backdrop>
            <ReactPlayer width='387px' height='217px' url={this.props.url} className={Stepstyle.Videocenter} onReady={this.handleClose}/>
            <p style={{paddingBottom:'2px'}}></p>
            <FormControl  variant="outlined" disabled={this.state.disabled} id='dropdown'>
                <InputLabel id="demo-simple-select-autowidth-outlined-label">
                Select Type of Notes
                </InputLabel>
                <Select
                labelId="demo-simple-select-autowidth-outlined-label"
                id="demo-simple-select-autowidth-outlined"
                value={this.state.type}
                onChange={this.handleChange}
                displayEmpty
                labelWidth={150}
                >
                <MenuItem value='Both'><em>Short Summary and Detailed Notes</em></MenuItem>
                <MenuItem value='Short'>Short Summary only</MenuItem>
                <MenuItem value='Detailed'>Detailed Notes only</MenuItem>
                </Select>
            </FormControl>
            <p></p>
            <Button variant="contained" className={Stepstyle.Button} component="span" onClick={this.handleOnClick} disabled={this.state.disabled}>
                Generate
            </Button>
            <br></br>
            <Typography variant='caption' color='textSecondary' onClick={this.props.onPrevious} id='other-video' disabled={this.state.disabled} className={Stepstyle.othervideo}><u>Other Video ?</u></Typography>
            </div>
        )
    }
}

export default Step2