import React, {useState} from 'react';
import SliderOne from './sliders/slidersone';
import SliderTwo from './sliders/sliderstwo';

import "./toppage.css";

const Toppage = () => {
  const [isControl, setIsControl] = useState(true)

  
  return (
    <div>
      <h1>Hearing Aid Guide</h1>
      <h6>Welcome To Our Application</h6>
      {/* <button className='pairbutton'><h2>Pair Device</h2></button> */}
      
      <button className='controlBtn'onClick={()=>{
        setIsControl(!isControl);
      }}>{isControl === true ? "Control" : "Back"}</button>
      {isControl === true ? <SliderOne /> : <SliderTwo />}

    </div>
  );
};

export default Toppage;
