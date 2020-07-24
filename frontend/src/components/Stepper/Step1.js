import React from 'react'
import StepStyle from './Step.module.css'
import {FormControl, InputLabel, OutlinedInput, InputAdornment, Button, makeStyles, Typography, Divider, Backdrop} from '@material-ui/core'
import SearchIcon from '@material-ui/icons/Search';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import {DarkStep1} from '../Functions'
import Loader from '../Loader/Loader';


class Step1 extends React.Component{

    state={
        url:'',
        videoType:'Preview',
        open:false
    }

    changetoUpload = (e) =>{
        this.setState({videoType:'Upload'})
    }
    
    changetoPreview = (e) =>{
        this.setState({videoType:'Preview'})
    }

    handleOnClick = () =>{
        this.setState({open:true,videoType:''})
        this.props.onChange()
        console.log(this.state)
    }

    handleChange=(event)=> {
        this.props.onURLChange(event.target.value)
    }

    componentDidMount=()=>{
        DarkStep1()
    }

    render(){
        if (this.state.videoType==='Preview'){
            return(
                <div>

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
                    <p></p>
                    <div id={StepStyle.or}><Typography variant='caption'>OR</Typography></div>
                    <p></p>
                    <Button variant='contained' startIcon={<CloudUploadIcon/>} color="primary" onClick={this.changetoUpload}>Upload a Video Instead ?</Button>
                </div>
            )
        }
        else if(this.state.open){
            return(
                <Backdrop open={this.state.open} className={StepStyle.backdrop}>
                    <Loader></Loader>
                </Backdrop>
            )
        }
        else{
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