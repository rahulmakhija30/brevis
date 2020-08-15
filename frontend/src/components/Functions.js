import Nav from './Navbar/Nav.module.css'
import Step from './Stepper/Step.module.css'

var i=0

const Mode = ()=>{
  try {
    console.log("clicked")
    var element = document.getElementById("mySidenav");
    var image = document.getElementById("Image");
    var homeicon = document.getElementById("homeicon")
    var suggestionsicon = document.getElementById("suggestionsicon")
    var abouticon = document.getElementById("abouticon")
    var footer = document.getElementById("footer")
    i++;
    if(i%2!==0){
      element.classList.remove(Nav.LightMode);
      element.classList.add(Nav.DarkMode);
      image.src='/static/media/sun.e1edd63e.png';
      homeicon.classList.add(Nav.invert);
      suggestionsicon.classList.add(Nav.invert);
      abouticon.classList.add(Nav.invert);
      image.classList.add(Nav.invert);
      document.body.classList.remove(Nav.BodyLightMode)
      document.body.classList.add(Nav.BodyDarkMode)
      footer.classList.add(Nav.colorwhite)
      try {
        DarkStep1()
      } catch (error){}
      try{
        DarkStep2()
      } catch (error) {}
      try{
        DarkLoader()
      } catch (error) {}
      try{
        DarkStep3()
      } catch (error) {}
      try{
        AboutPage()
      } catch (error) {}
    }
    else{
      element.classList.remove(Nav.DarkMode);
      element.classList.add(Nav.LightMode);
      image.src='/static/media/night.6048b803.png';
      homeicon.classList.remove(Nav.invert);
      suggestionsicon.classList.remove(Nav.invert);
      abouticon.classList.remove(Nav.invert);
      image.classList.remove(Nav.invert);
      document.body.classList.remove(Nav.BodyDarkMode)
      document.body.classList.add(Nav.BodyLightMode)
      footer.classList.remove(Nav.colorwhite)
      try {
        DarkStep1()
      } catch (error){}
      try{
        DarkStep2()
      } catch (error) {}
      try{
        DarkLoader()
      } catch (error) {}
      try{
        DarkStep3()
      } catch (error) {}
      try{
        AboutPage()
      } catch (error) {}
    } 
  } catch (error) {
   console.log(error) 
  }
}

const DarkStep1 = () =>{
  var inputfield = document.getElementById("inputfield")
  var Step1 = document.getElementById("Step1")
  if(document.body.classList.contains(Nav.BodyDarkMode)){
    inputfield.classList.add(Step.Darkinput)
    Step1.classList.add(Nav.colorwhite)
  }
  else{
    inputfield.classList.remove(Step.Darkinput)
    Step1.classList.remove(Nav.colorwhite)
  }
}

const DarkLoader = () =>{
  var loader = document.getElementById("loader")
  if(document.body.classList.contains(Nav.BodyDarkMode)){
    loader.classList.add(Step.Darkinput)
  }
  else{
    loader.classList.remove(Step.Darkinput)
  }
}

const DarkStep3 = () =>{
  var Step3 = document.getElementById("Step3") 
  if(document.body.classList.contains(Nav.BodyDarkMode)){
    Step3.classList.add(Nav.colorwhite)
  }
  else{
    Step3.classList.remove(Nav.colorwhite)
  }
}


const DarkStep2 = () =>{
  var Step2 = document.getElementById("Step2")
  try {
    var dropdown = document.getElementById("dropdown")
    var other_video = document.getElementById('other-video')
  } catch (error) {}
  if(document.body.classList.contains(Nav.BodyDarkMode)){
    Step2.classList.add(Nav.colorwhite)
    try {
      dropdown.classList.add(Step.Darkinput)
      other_video.classList.add(Step.Darkinput)
    } catch (error) {}
  }
  else{
    Step2.classList.remove(Nav.colorwhite)
    try {
      dropdown.classList.remove(Step.Darkinput)
      other_video.classList.remove(Step.Darkinput)
    } catch (error) {}
  }
}

const AboutPage = () =>{
  var about1 = document.getElementById("about1")
  var about2 = document.getElementById("about2")
  var about3 = document.getElementById("about3")
  var about4 = document.getElementById("about4")
  var about5 = document.getElementById("about5")
  if(document.body.classList.contains(Nav.BodyDarkMode)){
    about1.classList.add(Nav.invert);
    about2.classList.add(Nav.invert);
    about3.classList.add(Nav.invert);
    about4.classList.add(Nav.invert);
    about5.classList.add(Nav.invert);
  }
  else{
    about1.classList.remove(Nav.invert);
    about2.classList.remove(Nav.invert);
    about3.classList.remove(Nav.invert);
    about4.classList.remove(Nav.invert);
    about5.classList.remove(Nav.invert);
  }
}

export {Mode, DarkStep1, DarkStep2, DarkLoader,DarkStep3, AboutPage}