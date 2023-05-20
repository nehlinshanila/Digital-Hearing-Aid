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
    color: '#17212a',
    fontSize: 60,
    fontWeight: 'bold',
    // fontFamily: 'Poppins, sans-serif',
  },
  subtitle: {
    color: '#001728af',
    fontSize: 25,
    fontWeight: 'bold',
  },
  logo: {
    top: -280,
    left: -10,
    position: 'absolute',
    width: 300,
    height: 300,
    resizeMode: 'contain',
    borderColor: 'white', // HOWWWWWWWWWWWWWWWWWWW  then give logo
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
    elevation: 30,
    shadowColor: 'black',
  },
});

export default MaincontainerStyles;
