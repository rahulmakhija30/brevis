import React from 'react'
import { Container, Typography } from '@material-ui/core'
import AppStyle from '../../App.module.css'
import Details from '../Details/Detail'
import video from './Brevis.mp4'
import './About.css'
import {AboutPage} from '../Functions'


export default class About extends React.Component{

    componentDidMount = () =>{
        console.log('Component Mounted')
        AboutPage()
    }
    
    render(){
        return(
            <div style={{marginLeft:'80px'}}>
                <Container maxWidth='lg'>
                <Typography align='center' variant='h2' className={AppStyle.brevisHeading}>About Us</Typography>
                <p style={{padding:'5px'}}><br></br></p>
                <Typography align='Left' variant='h6'  id='about1'><b>Ever missed classes ?</b></Typography> 
                <Typography  id='about2'>
                    Of course you did ! Now worried about watching the whole lecture video again ? 
                    Struggling with internet issues? Or getting disturbed by the background noises in the lecture
                    video? It's tough, and we understand your problem. But, no need to worry now ! 
                    We bring to you Brevis, a web application that will do this job for you, and provide you with 
                    the best quality of notes, with the exact content you need. 
                    Brevis, goes through your entire lecture video and looks for content that matters, and the best 
                    part is, you don't need to watch the entire video. Just plug in the video url and we will do the 
                    rest of it. Click on the Download button and get your notes. As easy as that !
                    But wait, that’s not all, we still have something more for you !
                    While the notes are being generated, you can check out other videos that are related to your 
                    lecture for a better understanding. Go through some articles related to the topic. And be sure 
                    to go through some important definitions, that you won't like to miss out. Brevis provides you 
                    with all of this !
                </Typography>
                <br></br>
                <Typography align='Left' variant='h6'  id='about3'>
                    <b>Why Us ?</b>
                </Typography>
                <Typography align='center'>
                    <video width="50%" height="50%" controls className='video'>
                        <source src={video} type="video/mp4" className='video'/>
                    </video>
                </Typography>
                <br></br>
                <Typography  id='about4' align='Left' variant='h6'>
                    <b>So, who are we ?</b>
                </Typography>
                <Typography  id='about5'>
                    We are students, just like you who thought that this global issue needs some attention. 
                    After all, it's not easy to be a student.  So, we took this as a challenge, and made a 
                    project for every other student like us.
                </Typography>
                <p><br></br></p>
                <Details/>
                </Container>
            </div>
        )
    }
}