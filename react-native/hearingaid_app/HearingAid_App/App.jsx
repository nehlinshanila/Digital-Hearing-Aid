import React, {useState} from 'react';
import {View, StyleSheet} from 'react-native';
import Maincontainer from './components/Maincontainer/maincontainer';
import ControlButton from './components/Buttons/buttons';
import SliderComponent from './components/Sliders/sliders';
import LinearGradient from 'react-native-linear-gradient';
import Test_Slider from './components/Sliders/test_slider';

const App = () => {
  const [isPressed, setisPressed] = useState(false);

  const handlePressed = () => {
    setisPressed(!isPressed);
  };

  return (
    <LinearGradient
      colors={['#bdc3c7', '#2c3e50']}
      start={{x: 1, y: 0}} // Start from the right side of the container
      end={{x: 0, y: 0}} // End at the left side of the container
      style={styles.container}>
      <View style={styles.container}>
{/* 
        <Maincontainer />
        <ControlButton onPress={handlePressed} pressValue={isPressed} /> */}
        <SliderComponent />
        {/* <Test_Slider /> */}
      </View>
    </LinearGradient>
  );
};

const styles = StyleSheet.create({
  container: {
    // backgroundColor: 'red',
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
