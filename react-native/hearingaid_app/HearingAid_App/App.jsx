import React from 'react';
import {View, StyleSheet} from 'react-native';
import HelloWorld from './components/helloworld';
import CustomButton from './components/Background/buttons';
import CustomSlider from './components/Background/sliders';

const App = () => {
  return (
    <View style={styles.container}>
      <HelloWorld />
      <CustomButton />
      <CustomSlider
        max={100}
        min={0}
        step={1}
        onValueChange={value => {
          console.log('Slider value:', value);
        }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
