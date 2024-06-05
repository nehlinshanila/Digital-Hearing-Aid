import React from 'react';
import {Button, Text, View, TouchableOpacity} from 'react-native';
import ControlButtonStyle from './buttons_styles';

const ControlButton = ({onPress, title, isInControl}) => {
  const styles = ControlButtonStyle;
  // const newButtonTitle = "New Button Title"; // Update the button title here

  return (
    <TouchableOpacity
      onPress={onPress}
      style={isInControl ? styles.controlButon : styles.homeButtonText}>
      <Text style={styles.controlButtonText}>{title}</Text>
    </TouchableOpacity>
  );
};
export default ControlButton;
