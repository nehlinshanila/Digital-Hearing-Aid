import {StyleSheet} from 'react-native';

const ControlButtonStyle = StyleSheet.create({
  container: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: 20,
    position: 'relative',
    top: 200,
    right: 100,
    width: 100,
  },
  button: {
    display: 'flex',
    backgroundColor: '#2196F3',
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderRadius: 8,
    alignItems: 'center',
  },
  controlButton: {
    backgroundColor: 'red',
    marginLeft: '20%',
    
  },
  amplitudeButton: {
    backgroundColor: 'green', // Set the color for Amplitude button
  },
  profileButton: {
    backgroundColor: 'blue', // Set the color for Profile button
  },
  // buttonText: {
  //   color: 'white',
  //   fontSize: 16,
  //   fontWeight: 'bold',
  // },
});

export default ControlButtonStyle;
