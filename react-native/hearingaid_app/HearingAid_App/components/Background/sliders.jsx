import React, { useState } from 'react';
import { View, Text } from 'react-native';
import sliderstyles from './sliders_styles';
import Slider from "react-native-slider";

const CustomSlider = ({ min, max, step, onValueChange }) => {
  const [value, setValue] = useState(min);
  const styles=sliderstyles

  const handleValueChange = (newValue) => {
    setValue(newValue);
    onValueChange(newValue);
  };

  return (
    <View style={styles.container}>
      <Slider
        style={styles.slider}
        minimumValue={min}
        maximumValue={max}
        step={step}
        value={value}
        onValueChange={handleValueChange}
      />
      <Text style={styles.valueText}>{value}</Text>
    </View>
  );
};


export default CustomSlider;
