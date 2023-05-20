import React from 'react';
import { View, Text, Slider } from 'react-native';
import Sliderstyles from './sliders_styles';
// import Slider from 'react-native-slider';
// import Slider from '@react-native-community/slider';

const SliderComponent = ({ value, onValueChange }) => {
  const styles = Sliderstyles;

  return (
    <View style={styles.container}>
      <Text style={ styles.valueText }>
        Amplification Factor:                        {value}
      </Text>
      <Slider
        value={value}
        onValueChange={onValueChange}
        minimumValue={0}
        maximumValue={100}
        step={1}
        style={styles.slider}
        thumbTintColor="#000"
        minimumTrackTintColor="#000"
        maximumTrackTintColor="#ccc"
      />
    </View>
  );
};

export default SliderComponent;
