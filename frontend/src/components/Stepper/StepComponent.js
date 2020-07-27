import { Stepper, Step, StepLabel, StepConnector, withStyles, makeStyles, Typography, Zoom } from '@material-ui/core';
import React from 'react';
import StepStyle from './Step.module.css'
import clsx from 'clsx';
import Check from '@material-ui/icons/Check';
import PropTypes from 'prop-types';
import Step1 from './Step1'
import Step2 from './Step2'
import Step3 from './Step3'
import axios from 'axios';


const QontoConnector = withStyles({
    alternativeLabel: {
      top: 10,
      left: 'calc(-50% + 16px)',
      right: 'calc(50% + 16px)',
    },
    active: {
      '& $line': {
        borderColor: '#784af4',
      },
    },
    completed: {
      '& $line': {
        borderColor: '#784af4',
      },
    },
    line: {
      borderColor: '#cfcfff',
      borderTopWidth: 3,
      borderRadius: 1,
    },
})(StepConnector);


const useQontoStepIconStyles = makeStyles({
  root: {
    color: '#ababff',
    display: 'flex',
    height: 22,
    alignItems: 'center',
  },
  active: {
    color: '#784af4',
  },
  circle: {
    width: 12,
    height: 12,
    borderRadius: '50%',
    backgroundColor: 'currentColor',
  },
  completed: {
    color: '#784af4',
    zIndex: 1,
    fontSize: 18,
  },
});
  
function QontoStepIcon(props) {
  const classes = useQontoStepIconStyles();
  const { active, completed } = props;

  return (
    <div
      className={clsx(classes.root, {
        [classes.active]: active,
      })}
    >
      {completed ? <Check className={classes.completed} /> : <div className={classes.circle} />}
    </div>
  );
}
  
QontoStepIcon.propTypes = {
  /**
   * Whether this step is active.
   */
  active: PropTypes.bool,
  /**
   * Mark the step as completed. Is passed to child components.
   */
  completed: PropTypes.bool,
};
  
class StepComponent extends React.Component{

  state={
    activestep:0,
    url:null,
    validurl:false,
    scrape:"",
    type:""
  }

  gotostep1= () =>{
    this.setState({activestep:0})
  }

  gotostep2=() =>{
    this.setState({activestep:1})
    console.log(this.state)
  }
  

  gotostep3= (value) =>{
    this.setState({activestep:2,
      type:value
    })
    console.log(this.state)
  }

  getURL = (url) =>{
    this.setState({url:url})
  }

  getScrapeContent = (scrape) =>{
    this.setState({scrape:scrape})
  }

  getStepContent(stepIndex) {
    switch (stepIndex) {
      case 0:
        return <Step1 onChange={this.gotostep2} onURLChange={this.getURL}/>;
      case 1:
        return <Step2 onNext={this.gotostep3} url={this.state.url} onPrevious={this.gotostep1} onScrapeContent={this.getScrapeContent}/>;
      case 2:
        return <Step3 data={this.state} onScrapeContent={this.getScrapeContent}/>;
      default:
        return 'Unknown stepIndex';
    }
  }


    render(){
        return(
            <div>
                <Stepper activeStep={this.state.activestep} alternativeLabel connector={<QontoConnector/>} className={StepStyle.Stepper}>
                    <Step>
                        <StepLabel StepIconComponent={QontoStepIcon}><Typography  id='Step1'>Enter link</Typography></StepLabel>
                    </Step>
                    <Step>
                        <StepLabel StepIconComponent={QontoStepIcon}><Typography  id='Step2'>Preview video and select the type of notes</Typography></StepLabel>
                    </Step>
                    <Step>
                        <StepLabel StepIconComponent={QontoStepIcon}><Typography  id='Step3'>Enjoy your notes</Typography></StepLabel>
                    </Step>
                </Stepper>
                <div> 
                  <p></p>
                  <Zoom in><Typography align='center'>{this.getStepContent(this.state.activestep)}</Typography></Zoom>
                </div>
            </div>
        )
    }
}

export default StepComponent