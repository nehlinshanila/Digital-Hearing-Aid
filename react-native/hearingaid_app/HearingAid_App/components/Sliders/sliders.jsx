import React, {useState} from 'react';
import { View, Text } from 'react-native';
import Sliderstyles from './sliders_styles';
import Slider from 'react-native-slider';
// import Slider from '@react-native-community/slider';

const SliderComponent = () => {
  const [value, setValue] = useState(1);

  const styles = Sliderstyles;


  const handleSliderChange = sliderValue => {
    setValue(sliderValue);
  };

  return (
    <View style={styles.container}>
      <Text style={ styles.valueText }>
        Amplification Factor: {value}
      </Text>
      <Slider
        value={value}
        onValueChange={handleSliderChange}
        minimumValue={1}
        maximumValue={100}
        step={1}
        style={styles.slider}
        vertical={true}
        thumbStyle={styles.thumb}
        // orientation="vertical"
        // minimumTrackTintColor="#000"
        // maximumTrackTintColor="#ccc"
      />
    </View>
  );
};

export default SliderComponent;
