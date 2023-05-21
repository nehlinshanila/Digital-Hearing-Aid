import React, {useState} from 'react';
import {View, StyleSheet, Button, Text} from 'react-native';
import Maincontainer from './components/Maincontainer/maincontainer';
import ControlButton from './components/Buttons/buttons';
import SliderComponent from './components/Sliders/sliders';
import LinearGradient from 'react-native-linear-gradient';
import Test_Slider from './components/Sliders/test_slider';
import Navbar from './components/Navbar/navbar';

import MyComponent from './components/test';

const App = () => {
  const [isPressed, setisPressed] = useState(false);

  // for component appear disappear
  const [isComponentVisible, setComponentVisible] = useState(true);
  const toggleComponentVisibility = () => {
    setComponentVisible(!isComponentVisible);
  };

  // const handlePressed = () => {
  //   setisPressed(!isPressed);
  // };

  return (
    <LinearGradient
      colors={['#D7DDE8', 'white']}
      // start={{x: 0, y: 0}} // Start from the right side of the container
      // end={{x: 0, y: 0}} // End at the left side of the container
      style={styles.container}>
      <View style={styles.container}>
        {isComponentVisible ? (
          <>
            <Navbar />
            <Maincontainer />
            {/* <ControlButton onPress={handlePressed} pressValue={isPressed} /> */}
          </>
        ) : (
          <>
            <SliderComponent />
          </>
        )}

        <ControlButton
          title={isComponentVisible ? 'Amplitude' : 'Home'}
          onPress={toggleComponentVisibility}
        />

        {/* <MyComponent/> */}

        {/* <Navbar/>
        <Maincontainer />
        <ControlButton onPress={handlePressed} pressValue={isPressed} /> */}
        {/* <SliderComponent /> */}
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
