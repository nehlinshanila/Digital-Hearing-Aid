import React, { useState } from "react";
import SliderOne from "./sliders/slidersone";
import SliderTwo from "./sliders/sliderstwo";

import "./toppage.css";
import "./sliders/sliderbackground.css";

const Toppage = () => {
  const [isControl, setIsControl] = useState(false);
  const [isProfile, setIsProfile] = useState(false);
  const [isSlider, setIsSlider] = useState(false);

  return (
    <div>
      {!isControl && (
        <div>
          <div className="shadeone"></div>
          <div className="shadetwo"></div>
          <img src="../images/Logo.png" alt="Logo" className="logo" />
          <h1>Hearing Aid Guide</h1>
          <h6>Welcome To Our Application</h6>
        </div>
      )}

      <button
        className="controlBtn"
        onClick={() => {
          setIsControl(!isControl);
          setIsProfile(false);
          setIsSlider(false);
        }}
      >
        {isControl ? "Home" : "Control"}
      </button>

      {isControl && (
        <>
          <button
            className="profileBtn"
            onClick={() => {
              setIsProfile(!isProfile);
              setIsSlider(false);
            }}
          >
            {isProfile ? "Back" : "Profile"}
          </button>

          <button
            className="sliderBtn"
            onClick={() => {
              setIsSlider(!isSlider);
              setIsProfile(false);
            }}
          >
            {isSlider ? "Back" : "Slider"}
          </button>
        </>
      )}

      {isControl === true && isProfile === false && isSlider === false && (
        <h2>Welcome to the options page</h2>
      )}

      {isProfile && <h2>Profile Content</h2>}

      {isSlider && (
        <>
          <SliderOne />
          <SliderTwo />
        </>
      )}
    </div>
  );
};

export default Toppage;
