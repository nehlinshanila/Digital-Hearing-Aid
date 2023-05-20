import React, {useState} from 'react';
import {View, StyleSheet} from 'react-native';
import HelloWorld from './components/helloworld';
import ControlButton from './components/Background/buttons';
import SliderComponent from './components/Background/sliders';
import Homescreen from './components/Homescreen/homescreen';
// import Amplify from './components/Amplify/amplify';
// import Server from './components/Server/server';
// import Maincontainer from './components/Maincontainer/maincontainer';
import LinearGradient from 'react-native-linear-gradient';

const App = () => {
  const [value, setValue] = useState(0);
  const [isPressed, setisPressed] = useState(false);

  const handleSliderChange = sliderValue => {
    setValue(sliderValue);
  };

  const handlePressed = () => {
    setisPressed(!isPressed);
  };

  return (
    <LinearGradient
      colors={['#5f83a7', '#bdc3c7']}
      start={{x: 1, y: 0}} // Start from the right side of the container
      end={{x: 0, y: 0}} // End at the left side of the container
      style={styles.container}>
      <View style={styles.container}>
        {/* <Maincontainer/>
      <Homescreen/>
      <Amplify/>
      <Server/> */}
        <HelloWorld />
        <ControlButton onPress={handlePressed} pressValue={isPressed} />
        <SliderComponent value={value} onValueChange={handleSliderChange} />
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
