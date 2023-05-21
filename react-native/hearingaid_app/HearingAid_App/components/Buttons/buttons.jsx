import React from 'react';
import {Button, Text, View, TouchableOpacity} from 'react-native';
import ControlButtonStyle from './buttons_styles';

const ControlButton = ({onPress, title}) => {
  const styles = ControlButtonStyle;
  // const newButtonTitle = "New Button Title"; // Update the button title here

  return (
    // <TouchableOpacity onPress={onPress} >
    //   <View style={styles.container}>
    //     <Button
    //       // title={pressValue == true ? 'back' : 'Amplitude'}
    //       // onPress={onPress}
    //       color='#c4ac8f'

    //       style={styles.controlButton}
    //     />
    //   </View>
    // </TouchableOpacity>



    <TouchableOpacity onPress={onPress} style={styles.container}>
      <Text style={styles.controlButton}>{title}</Text>
    </TouchableOpacity>
  );
};

export default ControlButton;
{
  /* <Button title="Amplitude" onPress={onPress} style={styles.amplitudeButton}/>
      <Button title="Profile" onPress={onPress} style={styles.profileButton}/> */
}
