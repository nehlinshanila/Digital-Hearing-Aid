import React from 'react';
import {Button, Text, View, TouchableOpacity} from 'react-native';
import ControlButtonStyle from './buttons_styles';

const ControlButton = ({title, onPress, pressValue}) => {
  const styles = ControlButtonStyle;
  // const newButtonTitle = "New Button Title"; // Update the button title here

  return (
    <TouchableOpacity onPress={onPress}>
      <View style={styles.container}>
      <Button title={pressValue == true ? 'control' : 'back'} onPress={onPress} style={styles.controlButton}/>
      <Text style={styles.buttonText}>{title}</Text>
    </View>
    </TouchableOpacity>
    
    
  );
};

export default ControlButton;
{/* <Button title="Amplitude" onPress={onPress} style={styles.amplitudeButton}/>
      <Button title="Profile" onPress={onPress} style={styles.profileButton}/> */}