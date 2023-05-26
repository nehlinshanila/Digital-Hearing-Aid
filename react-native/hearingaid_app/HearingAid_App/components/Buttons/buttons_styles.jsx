import {StyleSheet} from 'react-native';

const ControlButtonStyle = StyleSheet.create({
  controlButon: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: 20,
    position: 'relative',
    top: 210,
    right: 100,
    width: 100,
    backgroundColor: '#b09e6d',
    borderRadius: 15,
  },
  controlButtonText: {
    backgroundColor: '#b09e6d',
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
    padding: 10,
  },
  homeButtonText: {
    position: 'relative',
    height: '7%',
    top: -320,
    left: -130, 
    backgroundColor: '#b09e6d',
    fontSize: 16,
    fontWeight: 'bold',
    padding: 3,
    borderRadius: 10,
  },
});

export default ControlButtonStyle;
