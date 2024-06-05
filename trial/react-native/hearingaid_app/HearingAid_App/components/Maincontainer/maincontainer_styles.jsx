import {StyleSheet} from 'react-native';

const MaincontainerStyles = StyleSheet.create({
  container: {
    display: 'flex',
    // backgroundColor: 'red',
    justifyContent: 'center',
    alignItems: 'center',
    height: 'auto',
    position: 'absolute',
    top: 300,
  },
  title: {
    position: 'relative',
    color: '#485781',
    fontSize: 80,
    fontWeight: 'bold',
    // fontFamily: 'Poppins, sans-serif',
  },
  subtitle: {
    color: '#73767d',
    fontSize: 25,
    fontWeight: 'bold',
    // fontFamily: 'Poppins, sans-serif',

  },
  logo: {
    top: -150,
    left: 30,
    position: 'absolute',
    width: 200,
    height: 200,
    resizeMode: 'contain',
    borderColor: 'white', // HOWWWWWWWWWWWWWWWWWWW  then give logo
    opacity: 0.5,
    // elevation: 10,
    // shadowColor: '#000000',
  },
  designblock: {
    position: 'absolute',
    top: -300,
    left: -30,
    width: 300,
    height: 230,
    backgroundColor: 'grey',
    borderRadius: 50,
    opacity: 1,
    
  },
  block: {
    position: 'absolute',
    left: -50,
    backgroundColor: 'white',
    borderRadius: 50,
    paddingVertical: 280,
    paddingHorizontal: 25,
    width: '100%',
    marginVertical: 10,
  },
  elevation: {
    // zIndex:-1,
    elevation: 20,
    shadowColor: 'black',
  },
});

export default MaincontainerStyles;
