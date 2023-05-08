import React, { useState, useEffect } from "react";
import "./sliders.css";

export default function Sliders() {
  const [value, onChange] = useState(1);
  useEffect(() => {
    const ele = document.querySelector(".buble");
    if (ele) {
      ele.style.left = `${Number(value / 4)}px`;
    }
  });
  return (
    <div className="shadedarea">
      <div className="slider-parentone">
        <input
          className="input-sliderone"
          type="range"
          min="1"
          max="100"
          value={value}
          onChange={({ target: { value: radius } }) => {
            onChange(radius);
          }}
        />
        <div className="bubleone">{value} <p>Normal Volume</p></div>
      </div>
      <div className="slider-parenttwo">
        <input
          className="input-slidertwo"
          type="range"
          min="1"
          max="100"
          value={value}
          onChange={({ target: { value: radius } }) => {
            onChange(radius);
          }}
        />
        <div className="bubletwo">{value} <p>Smart Amplify</p></div>
      </div>
    </div>
  );
}
