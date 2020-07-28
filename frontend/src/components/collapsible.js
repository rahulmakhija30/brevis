import React,{Component} from 'react'
import './collapse.css'
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
    
    onClick = () =>{
      var acc = document.getElementsByClassName("accordion");
              var i;
      
              for (i = 0; i < acc.length; i++) {
              acc[i].addEventListener("click", function() {
                  this.classList.toggle("active");
                  var panel = this.nextElementSibling;
                  if (panel.style.maxHeight) {
                  panel.style.maxHeight = null;
                  } else {
                  panel.style.maxHeight = panel.scrollHeight + "px";
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
              <button className="accordion" onClick={this.onClick}>Text Summary</button>
              <div className="panel">
                <p>{this.state.summary}</p>
                </div>
                <p></p>
                <button className="accordion" onClick={this.onClick}>Links to useful Articles</button>
                <div className="panel">
                {googleList}
                </div>
                <p></p>
                <button className="accordion" onClick={this.onClick}>Links to related Youtube Videos</button>
                <div className="panel">
                {youtubeList}
                </div>
                <p></p>
            </div>
        )
    }
}

export default Collapsible