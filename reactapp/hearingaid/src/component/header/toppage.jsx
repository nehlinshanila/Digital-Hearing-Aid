import React, { useState } from "react";
import SliderOne from "./sliders/slidersone";
import SliderTwo from "./sliders/sliderstwo";

import "./toppage.css";

const Toppage = () => {
  const [isControl, setIsControl] = useState(true);
  const [isProfile, setIsProfile] = useState(false);
  const [isSlider, setIsSlider] = useState(false);

  return (
    <div>
      {!isControl == false && <h1>Hearing Aid Guide</h1>}
      {/* <h1>Hearing Aid Guide</h1> */}
      {!isControl == false && <h6>Welcome To Our Application</h6>}
      {/* <h6>Welcome To Our Application</h6> */}
      {/* <button className='pairbutton'><h2>Pair Device</h2></button> */}

      <button
        className="controlBtn"
        onClick={() => {
          setIsControl(!isControl);
          setIsProfile(false);
          setIsSlider(false);
        }}
      >
        {isControl === true ? "Control" : "Back"}
      </button>

      {/* below is the profile button */}
      <button
        className="profileBtn"
        onClick={() => {
          setIsProfile(!isProfile);
          setIsControl(false);
          setIsSlider(false);
        }}
      >
        {isProfile ? "Back" : "Profile"}
      </button>

      {/* below is the slider button */}
      <button
        className="sliderBtn"
        onClick={() => {
          setIsSlider(!isSlider);
          setIsControl(false);
          setIsProfile(false);
        }}
      >
        {isSlider ? "Back" : "Slider"}
      </button>

      {/* {isControl === true ? <SliderOne /> : <SliderTwo />} */}
      {isControl == false && (
        <>
          Welcome to the options page
        </>
      )}

      {isProfile && <h2>Profile Content</h2>}

      {isSlider == true && (
        <>
        <SliderOne/>
        <SliderTwo/>
        </>
      )}
    </div>
  );
};

export default Toppage;
