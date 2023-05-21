import {StyleSheet} from 'react-native';


const NavbarStyle = StyleSheet.create({
    navbar: {
      position: 'absolute',
      top: -70,
      left: 0,
      width: '100%',
      height: 200,
      backgroundColor: 'white',
      flexDirection: 'row',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: 16,
      backgroundColor: 'transparent',
    },
    navbarButton: {
      fontSize: 16,
      fontWeight: 'bold',
    },
    optionsContainer: {
      position: 'relative',
      top: 30,
      marginTop: 8,
      padding: 8,
      backgroundColor: 'transparent',
      borderWidth: 1,
      borderColor: '#ccc',
      flex: 1, // Take up remaining space
      justifyContent: 'center',
    },
  //   showOptions: {
  //     display: 'flex', // Show options container
  //   },
  //   hideOptions: {
  //     display: 'none', // Hide options container
  //   },
  optionText: {
      fontSize: 16,
      fontWeight: 'bold',
      position: 'relative',
      marginBottom: 10,
    },
  });

  export default NavbarStyle;
