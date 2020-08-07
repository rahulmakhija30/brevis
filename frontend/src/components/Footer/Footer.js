import React from 'react'
import { Typography } from '@material-ui/core'
import style from './Footer.module.css'

const Footer = () => {
    
    return(
        <Typography variant='caption' align='center' className={style.footer} id='footer'>Team Brevis || Mayank Agrawal || Aniket Aayush || Himanshu Jain || Rahul Makhija</Typography>
    )
}

export default Footer