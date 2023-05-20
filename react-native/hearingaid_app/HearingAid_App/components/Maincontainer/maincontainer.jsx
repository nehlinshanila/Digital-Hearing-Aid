import React from 'react';
import {View, Text, Image} from 'react-native';
import MaincontainerStyles from './maincontainer_styles';
import LinearGradient from 'react-native-linear-gradient';

const Maincontainer = () => {
  const styles = MaincontainerStyles;
  return (
    <View style={styles.container}>
      <LinearGradient
        colors={['#bdc3c7', '#2c3e50']}
        start={{x: 1, y: 0}} // Start from the right side of the container
        end={{x: 0, y: 0}} // End at the left side of the container
        style={[styles.block, styles.elevation]}></LinearGradient>
{/* 
<LinearGradient
        colors={['#2c3e50', '#bdc3c7']}
        start={{x: 1, y: 0}} // Start from the right side of the container
        end={{x: 0, y: 0}} // End at the left side of the container
        style={[styles.designblock, styles.elevation]}></LinearGradient> */}
        
      <View style={ styles.elevation}></View>
      {/* <Image source={require('./logooo.png')} style={styles.logo} /> */}

      <Text style={styles.title}>Hearing Aid Guide</Text>
      <Text style={styles.subtitle}>Welcome To Our Application</Text>
    </View>
  );
};

export default Maincontainer;
