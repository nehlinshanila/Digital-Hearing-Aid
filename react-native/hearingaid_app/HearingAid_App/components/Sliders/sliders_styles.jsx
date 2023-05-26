import {StyleSheet} from 'react-native';

const Sliderstyles = StyleSheet.create({
  container: {
    display: 'flex',
    // backgroundColor: 'red',
    justifyContent: 'center',
    alignItems: 'center',
    height: 'auto',
    position: 'absolute',
    top: 110,
    
  },

  slider: {
    height: 60,
    width: 300,
    top:180,
    borderRadius: 10,
    borderWidth: 2,
    borderColor: '#FFFFFF',
    // transform: [{ rotate: '-90deg' }],
    position: 'relative',
    // backgroundColor: 'red'
  },

  valueText: {
    textAlign: 'center',
    marginTop: 8,
    fontSize: 45,
    fontWeight: 'bold',
    marginBottom: 10,
    color: '#263D54',
    
  },
  thumb: {
    height: 35,
    width: 35,
    borderRadius: 50,
    color: '#263D54',
    
    
  }
});

export default Sliderstyles;
