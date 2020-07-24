var i=0

const Mode = ()=>{
  try {
    console.log("clicked")
    var element = document.getElementById("mySidenav");
    var image = document.getElementById("Image");
    var homeicon = document.getElementById("homeicon")
    var suggestionsicon = document.getElementById("suggestionsicon")
    var abouticon = document.getElementById("abouticon")
    var Step1 = document.getElementById("Step1")
    var Step2 = document.getElementById("Step2")
    var Step3 = document.getElementById("Step3")
    var footer = document.getElementById("footer")

    i++;
    if(i%2!==0){
      element.classList.remove("Nav_LightMode__2VM7G");
      element.classList.add("Nav_DarkMode__2sqP_");
      image.src='/static/media/sun.e1edd63e.png';
      homeicon.classList.add("Nav_invert__3wJdG");
      suggestionsicon.classList.add("Nav_invert__3wJdG");
      abouticon.classList.add("Nav_invert__3wJdG");
      image.classList.add("Nav_invert__3wJdG");
      document.body.classList.remove("Nav_BodyLightMode__2olZR")
      document.body.classList.add("Nav_BodyDarkMode__EFIdu")
      Step1.classList.add('Nav_colorwhite__1dFlw')
      Step2.classList.add('Nav_colorwhite__1dFlw')
      Step3.classList.add('Nav_colorwhite__1dFlw')
      footer.classList.add('Nav_colorwhite__1dFlw')
      try {
        DarkStep1()
      } catch (error){}
      try{
        DarkStep2()
      } catch (error) {}
      try{
        DarkLoader()
      } catch (error) {}
    }
    else{
      element.classList.remove("Nav_DarkMode__2sqP_");
      element.classList.add("Nav_LightMode__2VM7G");
      image.src='/static/media/night.6048b803.png';
      homeicon.classList.remove("Nav_invert__3wJdG");
      suggestionsicon.classList.remove("Nav_invert__3wJdG");
      abouticon.classList.remove("Nav_invert__3wJdG");
      image.classList.remove("Nav_invert__3wJdG");
      document.body.classList.remove("Nav_BodyDarkMode__EFIdu")
      document.body.classList.add("Nav_BodyLightMode__2olZR")
      Step1.classList.remove('Nav_colorwhite__1dFlw')
      Step2.classList.remove('Nav_colorwhite__1dFlw')
      Step3.classList.remove('Nav_colorwhite__1dFlw')
      footer.classList.remove('Nav_colorwhite__1dFlw')
      try {
        DarkStep1()
      } catch (error){}
      try{
        DarkStep2()
      } catch (error) {}
      try{
        DarkLoader()
      } catch (error) {}
    } 
  } catch (error) {
   console.log(error) 
  }
}

const DarkStep1 = () =>{
  var inputfield = document.getElementById("inputfield")
  if(document.body.classList.contains("Nav_BodyDarkMode__EFIdu")){
    inputfield.classList.add('Step_Darkinput__1sFOK')
  }
  else{
    inputfield.classList.remove('Step_Darkinput__1sFOK')
  }
}

const DarkLoader = () =>{
  var loader = document.getElementById("loader")
  if(document.body.classList.contains("Nav_BodyDarkMode__EFIdu")){
    loader.classList.add('Step_Darkinput__1sFOK')
  }
  else{
    loader.classList.remove('Step_Darkinput__1sFOK')
  }
}

const DarkStep2 = () =>{
  var dropdown = document.getElementById("dropdown")
  var other_video = document.getElementById('other-video')
  if(document.body.classList.contains("Nav_BodyDarkMode__EFIdu")){
    dropdown.classList.add('Step_Darkinput__1sFOK')
    other_video.classList.add('Step_Darkinput__1sFOK')
  }
  else{
    dropdown.classList.remove('Step_Darkinput__1sFOK')
    other_video.classList.remove('Step_Darkinput__1sFOK')
  }
}

export {Mode, DarkStep1, DarkStep2, DarkLoader}