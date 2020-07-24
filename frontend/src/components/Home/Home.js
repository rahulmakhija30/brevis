import React from 'react'
import { Container, Typography } from '@material-ui/core'
import StepComponent from '../Stepper/StepComponent'
import AppStyle from '../../App.module.css'

export default function Home(){
    return(
        <div>
            <Container maxWidth='lg'>
            <Typography align='center' variant='h2' className={AppStyle.brevisHeading} >BREVIS</Typography>
            <StepComponent></StepComponent>
            </Container>
        </div>
    )
}