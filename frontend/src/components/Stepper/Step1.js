import React from 'react'
import StepStyle from './Step.module.css'
import {FormControl, InputLabel, OutlinedInput, InputAdornment, Button, makeStyles, Typography, Divider, Backdrop} from '@material-ui/core'
import SearchIcon from '@material-ui/icons/Search';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import {DarkStep1} from '../Functions'
import Loader from '../Loader/Loader';
import axios from 'axios';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

class Step1 extends React.Component{

    state={
        url:'',
        videoType:'Preview',
        open:false,
        validurl:false,
        Alertopen:false
    }

    IsValidURL=(event)=> {
        console.log(this.state)
          axios.post('/result',this.state)
          .then(res=>{
            axios.get('/res')
            .then(response=>{
            console.log(response)
              let download=null;
              if(response.data.result==1)
                {
                  this.setState({
                    validurl:true,
                    open:false
                  });
                  this.props.onChange()
              }
              else{
                  this.setState({
                    validurl:false,
                    open:false,
                    Alertopen:true,
                  });
                  // document.getElementById("alert").style.visibility='visible'
                //   alert("Please enter a valid link! ");
                  console.log(this.state)
                  //if(response.data.result==0)
                  //{
                    // document.getElementById('disp').innerHTML='Transcripts for the video do not exist!'
                  //}
                  //else{
                    // document.getElementById('disp').innerHTML='Not an educational video!'
                  //}
              } 
              
            },(error) => {
                if (error) {
                    console.log(error.name)
                    // document.getElementById("disp").innerHTML=error.message;
                }
              }
              
              )
          },(error) => {
            
            if (error) {
                console.log(error.name)
                // document.getElementById("disp").innerHTML='Please check the link again!';
            }
          }
        );
        console.log(this.state)
    }

    changetoUpload = (e) =>{
        this.setState({videoType:'Upload'})
    }
    
    changetoPreview = (e) =>{
        this.setState({videoType:'Preview'})
    }

    handleOnClick = () =>{
        if(this.state.videoType==='Preview')
        {
            this.setState({open:true})
            this.IsValidURL()
            console.log(this.state)
        }
    }

    handleAlertClose = () => {
        this.setState({Alertopen:false})
      };

    handleChange=(event)=> {
        this.setState({url:event.target.value})
        this.props.onURLChange(event.target.value)
    }

    componentDidMount=()=>{
        DarkStep1()
        console.log(this.state)
    }

    render(){
        if(this.state.open){
            console.log(this.state)
            return(
                <Backdrop open={this.state.open} className={StepStyle.backdrop}>
                    <Loader></Loader>
                </Backdrop>
            )
        }
        else if (this.state.videoType==='Preview'){
            return(
                <div>
                    {/*
                        Alert Dialog Start
                    */}
                    <div>
                        <Dialog
                            open={this.state.Alertopen}
                            onClose={this.handleAlertClose}
                            aria-labelledby="alert-dialog-title"
                            aria-describedby="alert-dialog-description"
                        >
                            <DialogTitle id="alert-dialog-title">{"Invalid Link!"}</DialogTitle>
                            <DialogContent>
                            <DialogContentText id="alert-dialog-description">
                                Please try again with a valid link.
                            </DialogContentText>
                            </DialogContent>
                            <DialogActions>
                            <Button onClick={this.handleAlertClose} color="primary">
                                OK
                            </Button>
                            </DialogActions>
                        </Dialog>
                        </div>
                    {/*
                        Alert Dialog End
                    */}
                    <FormControl variant="outlined" className={StepStyle.inputLink} id='inputfield' onChange={this.handleChange} value={this.state.url}>
                        <InputLabel htmlFor="outlined-adornment-amount">Paste Link</InputLabel>
                        <OutlinedInput
                            id="outlined-adornment-amount"
                            startAdornment={<InputAdornment position="start"><SearchIcon/></InputAdornment>}
                            labelWidth={80}
                        />
                    </FormControl>
                    <p></p>
                    <Button variant="contained" className={StepStyle.Button} component="span" onClick={this.handleOnClick}>
                        Preview
                    </Button>
                    {/*<p></p>
                    <div id={StepStyle.or}><Typography variant='caption' align='center'>OR</Typography></div>
                    <p></p>
                    <Button variant='contained' startIcon={<CloudUploadIcon/>} color="primary" onClick={this.changetoUpload}>Upload a Video Instead ?</Button>
                    */}</div>
            )
        }
        else 
       { 
            return(
                <div>
                    <input
                        accept="image/*"
                        className={StepStyle.input}
                        id="contained-button-file"
                        multiple
                        type="file"
                    />
                    <label htmlFor="contained-button-file">
                        <Button variant="contained" className={StepStyle.Button} component="span">
                        Upload
                        </Button>
                    </label>
                    <p></p>
                    <div id={StepStyle.or} ><Typography variant='caption'>OR</Typography></div>
                    <p></p>
                    <Button variant='contained' startIcon={<CloudUploadIcon/>} color="primary" onClick={this.changetoPreview}>Use an Online Video Instead ?</Button>
                </div>
            )
        }
    }
}

export default Step1
