import React from 'react'
import ReactPlayer from "react-player"
import { Typography, Backdrop, CircularProgress, FormControl, InputLabel, Select, MenuItem, FormHelperText, Button } from '@material-ui/core'
import Stepstyle from './Step.module.css'
import { DarkStep2 } from '../Functions'
import Loader from '../Loader/Loader'

class Step2 extends React.Component{

    state={
        open: true,
        type:'Notes+Ref',
        disabled:true,
    }

    handleChange = (event) => {
        this.setState({type:event.target.value})
    };

    handleClose=()=>{
        this.setState({open:false,disabled:false})
    }

    componentDidMount(){
        DarkStep2()
    }

    handleOnClick=() => {
        this.props.onNext(this.state.type)
        this.setState({open:true})
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
                <MenuItem value='Overview'><em>Overview</em></MenuItem>
                <MenuItem value='Notes'>Notes without External Refrences</MenuItem>
                <MenuItem value='Notes+Ref'>Full Notes with References</MenuItem>
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