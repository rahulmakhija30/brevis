import React from 'react'
import { Typography } from '@material-ui/core'
import style from './Footer.module.css'

const Footer = () => {
    return(
        <Typography variant='caption' align='center' className={style.footer} id='footer'>Team Brevis || Mayank || Aayush || Himanshu || Rahul</Typography>
    )
}

export default Footer