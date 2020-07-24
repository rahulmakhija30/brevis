import React from 'react'
import Accordion from '@material-ui/core/Accordion';
import AccordionSummary from '@material-ui/core/AccordionSummary';
import AccordionDetails from '@material-ui/core/AccordionDetails';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { Button, Backdrop } from '@material-ui/core';
import StepStyle from './Step.module.css'
import Loader from '../Loader/Loader';


class Step3 extends React.Component{

    state={
        disabled:'true',
        buttondisabled:'true',
        open:'true',
    }
    

    handleOnClick=(e)=>{
        this.setState({open:false,disabled:false})

    }

    render(){
        return(
            <div>
                <Backdrop open={this.state.open} className={StepStyle.backdrop} onClick={this.handleOnClick}>
                    <Loader></Loader>
                </Backdrop>
                <Button variant="contained" className={StepStyle.Button} component="span" onClick={this.handleOnClick} disabled={this.state.buttondisabled}>
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
                    <AccordionDetails>
                    <Typography>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
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
                    <Typography>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
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
                    <Typography>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                        sit amet blandit leo lobortis eget.
                    </Typography>
                    </AccordionDetails>
                </Accordion>
                <p></p>
            </div>
        )
    }
}

export default Step3