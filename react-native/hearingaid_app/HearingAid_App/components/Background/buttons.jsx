import React from 'react';
import { TouchableOpacity, Text } from 'react-native';
import CustomButtonStyle from './buttons_styles';

const CustomButton = ({ title, onPress }) => {
    const styles=CustomButtonStyle
  return (
    <TouchableOpacity style={styles.button} onPress={onPress}>
      <Text style={styles.buttonText}>{title}</Text>
    </TouchableOpacity>
  );
};

export default CustomButton;
