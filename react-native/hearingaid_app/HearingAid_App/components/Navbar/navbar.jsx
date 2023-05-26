import React, {useState} from 'react';
import {View, Text, TouchableWithoutFeedback, StyleSheet} from 'react-native';
import NavbarStyle from './navbar_styles';

const Navbar = () => {
    const styles = NavbarStyle;

  const [showOptions, setShowOptions] = useState(false);

  const handlePress = () => {
    setShowOptions(!showOptions);
  };

  return (
    <View style={NavbarStyle.navbar}>
      <TouchableWithoutFeedback onPress={handlePress}>
        <Text style={styles.navbarButton}>Menu</Text>
      </TouchableWithoutFeedback>
      {showOptions && (
        <View style={NavbarStyle.optionsContainer}>
          <Text style={NavbarStyle.optionText}>Server</Text>
          <Text style={NavbarStyle.optionText}>Profile</Text>
          <Text style={NavbarStyle.optionText}>About Us</Text>
        </View>
      )}
    </View>
  );
};


export default Navbar;
