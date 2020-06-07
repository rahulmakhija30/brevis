import React from 'react'
import ReactPlayer from "react-player"

const Preview = () => {
    return(
        <div>
            <ReactPlayer height="70%" 
                        width="90%" 
                        style={{
                            padding: "10px",
                            paddingLeft: "25%",
                            borderRadius:"20px",
                        }}
                        url={this.props.url}/>
        </div>
    )
}

export default Preview;