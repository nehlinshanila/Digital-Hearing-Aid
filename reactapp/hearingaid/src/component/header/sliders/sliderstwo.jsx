import React, { useState, useEffect } from "react";
import "./sliderstwo.css";
import { Link } from "react-router-dom"

export default function SliderTwo() {
  const [value, setValue] = useState(1);
  useEffect(() => {
    const bubleElement = document.querySelector(".buble");
    if (bubleElement) {
      bubleElement.style.left = `${Number(value / 4)}px`;
    }
  },[]);
  return (
    <div className="shadedarea">
      
      <div className="slider-parenttwo">
        <input
          className="input-slidertwo"
          type="range"
          min="1"
          max="100"
          value={value}
          onChange={({ target: { value: radius } }) => {
            setValue(radius);
          }}
        />
        <div className="bubletwo">{value} <p>Smart Amplify</p></div>
      </div>
    </div>
  );
}
