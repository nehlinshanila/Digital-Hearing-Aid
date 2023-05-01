import React, { useState } from "react";
import Slider from "@react-native-community/slider/dist";
import { View, StyleSheet, Text } from "@react-native-community/slider";

export default function Sliders() {
  const [sliderValue, setSliderValue] = useState(0);

  return (
    <div >
      <p >Slider value: {sliderValue.toFixed(2)}</p>
      <Slider
        
        minimumValue={0}
        maximumValue={1}
        step={0.01}
        value={sliderValue}
        
      />
    </div>
  );
}