import React from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import MobileStepper from '@material-ui/core/MobileStepper';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import KeyboardArrowLeft from '@material-ui/icons/KeyboardArrowLeft';
import KeyboardArrowRight from '@material-ui/icons/KeyboardArrowRight';
import SwipeableViews from 'react-swipeable-views';
import { autoPlay } from 'react-swipeable-views-utils';

const AutoPlaySwipeableViews = autoPlay(SwipeableViews);

const tutorialSteps = [
  {
    label: 'Tanishq Vyas',
    Position:'Mentor' ,
    imgPath:
      'https://images.unsplash.com/photo-1537944434965-cf4679d1a598?auto=format&fit=crop&w=400&h=250&q=60',
  },
  {
    label: 'Akshay',
    Position:'Mentor' ,
    imgPath:
      'https://images.unsplash.com/photo-1538032746644-0212e812a9e7?auto=format&fit=crop&w=400&h=250&q=60',
  },
  {
    label: 'Mayank Agrawal',
    Position:'Intern' ,
    imgPath:
      'https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=400&h=250&q=80',
  },
  {
    label: 'Rahul Makhija',
    Position:'Intern',
    imgPath:
      'https://images.unsplash.com/photo-1518732714860-b62714ce0c59?auto=format&fit=crop&w=400&h=250&q=60',
  },
  {
    label: 'Himanshu Jain',
    Position:'Intern',
    imgPath:
      'https://images.unsplash.com/photo-1512341689857-198e7e2f3ca8?auto=format&fit=crop&w=400&h=250&q=60',
  },
  {
    label: 'Aniket Aayush',
    Position:'Intern',
    imgPath:
      'https://images.unsplash.com/photo-1512341689857-198e7e2f3ca8?auto=format&fit=crop&w=400&h=250&q=60',
  },
];

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  header: {
    height: 50,
    paddingLeft: theme.spacing(4),
    backgroundColor: theme.palette.background.default,
  },
  img: {
    borderRadius: '50% !important',
    height: '120px',
    display: 'block',
    maxWidth: 400,
    overflow: 'hidden',
    width: '200px',
  },
  content:{
    display:'flex', 
    flexDirection:'column',
  },
  MobileStepper:{
    marginLeft:'80px', 
    borderRadius:'5px', 
    backgroundColor: '#d6d6d6',
    borderTopRightRadius: '0 !important',
    borderTopLeftRadius: '0 !important',
  },
  paper:{
    backgroundColor: '#dbdbdb',
    borderBottomLeftRadius:'0 !important',
    borderBottomRightRadius:'0 !important',
    marginLeft:'80px',
  }
}));

function Details() {
  const classes = useStyles();
  const theme = useTheme();
  const [activeStep, setActiveStep] = React.useState(0);
  const maxSteps = tutorialSteps.length;

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleStepChange = (step) => {
    setActiveStep(step);
  };

  return (
    <div className={classes.root}>
      <Paper elevation={3} className={classes.paper}>
      <AutoPlaySwipeableViews
        axis={theme.direction === 'rtl' ? 'x-reverse' : 'x'}
        index={activeStep}
        onChangeIndex={handleStepChange}
        enableMouseEvents
      >
        {tutorialSteps.map((step, index) => (
            <div key={step.label}>
                <div style={{display:'flex'}}>
                    {Math.abs(activeStep - index) <= 2 ? (
                        <img style={{margin:'10px'}} className={classes.img} src={step.imgPath} alt={step.label} />
                    ) : null}
                    <div className={classes.content}>
                      <Typography align='Center' variant= 'h6' ><b>{tutorialSteps[activeStep].label}</b></Typography>          
                      <Typography align='center'  variant='body2'>{tutorialSteps[activeStep].Position}</Typography>
                      <Typography style={{margin:'20px'}}>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed neque vitae non eum ullam autem! Inventore dolorem animi, cumque ad sapiente eos distinctio accusantium, nulla odio incidunt possimus asperiores consequatur.</Typography>
                    </div>
                    </div>
            </div>
        ))}
      </AutoPlaySwipeableViews>
      </Paper>
      <MobileStepper
        className={classes.MobileStepper}
        elevation={3}
        steps={maxSteps}
        position="static"
        variant="dots"
        activeStep={activeStep}
        nextButton={
          <Button size="small" onClick={handleNext} disabled={activeStep === maxSteps - 1}>
            {theme.direction === 'rtl' ? <KeyboardArrowLeft /> : <KeyboardArrowRight />}
          </Button>
        }
        backButton={
          <Button size="small" onClick={handleBack} disabled={activeStep === 0}>
            {theme.direction === 'rtl' ? <KeyboardArrowRight /> : <KeyboardArrowLeft />}
          </Button>
        }
      />
    </div>
  );
}

export default Details;
