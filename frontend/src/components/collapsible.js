import React,{Component} from 'react'
import './collapsible.css'
//import data from '../scrape_results.json'
//var fs = require('fs');
//var data = JSON.parse(fs.readFileSync('../scrape_results.json', 'utf8'));
//var data=require('../../../backend/scrape_results.json')

class Collapsible extends Component{
    state = {
        summary:"Demo Text Summary. Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem expedita repudiandae voluptas in neque mollitia doloribus possimus velit cum, eaque tempore. Dolores vel possimus sint impedit, nobis alias ab optio.",
        ArticleLink:["Link 1","\n","Link 2"],
        VideoLink:""
    }
    
    Button = () => {
        var coll = document.getElementsByClassName("collapsible");
        var i;
        
        for (i = 0; i < coll.length; i++) {
          coll[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.maxHeight){
              content.style.maxHeight = null;
            } else {
              content.style.maxHeight = 150 + "px";
              content.style.visibility = "visible";
            } 
          });
        }
    }

    
    render(){

      const {google,youtube}=this.props.scrape;
      const googleList=google.map(element=>{
        return(
          <div key={element.linktopage}>
            <a href={element.linktopage} >{element.title}</a>
          </div>
        )
      })
      const youtubeList=youtube.map(element=>{
        return(
          <div key={element.linktopage}>
            <a href={element.linktopage}>{element.title}</a>
          </div>
        )
      })
        return(
            <div className="Top-align animate__fadeIn animate__animated">
                <button className="collapsible z-depth-0" onClick={this.Button}>Text Summary</button>
                <div className="content">
                <p>{this.state.summary}</p>
                </div>
                <button className="collapsible z-depth-0" onClick={this.Button}>Links to useful Articles...</button>
                <div className="content">
                {googleList}
                </div>
                <button className="collapsible z-depth-0" onClick={this.Button}>Links to useful Videos...</button>
                <div className="content">
                {youtubeList}
                </div>
            </div>
        )
    }
}

export default Collapsible