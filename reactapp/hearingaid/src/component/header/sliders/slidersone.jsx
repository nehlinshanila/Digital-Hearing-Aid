import React, { useState, useEffect } from "react";
import "./slidersone.css";
import { Link } from "react-router-dom";

export default function SliderOne() {
  const [value, setValue] = useState(1);
  useEffect(() => {
    const bubleElement = document.querySelector(".buble");
    if (bubleElement) {
      bubleElement.style.left = `${Number(value / 4)}px`;
    }
  }, []);
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
            setValue(radius);
          }}
        />
        <div className="bubleone">
          {value} <p>Normal Volume</p>
        </div>
      </div>
    </div>
  );
}
