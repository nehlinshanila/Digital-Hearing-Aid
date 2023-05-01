import React from "react";
// import { createBottomTabNavigator } from "react-navigation-tabs";
// import { createAppContainer } from "react-navigation";
import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View, ImageBackground } from "react-native";
import Aiditem from "./components/Aiditem/index";
import Nextpage from "./components/Nextpage/index";
import Wallpaper from "./components/Wallpaper/index";
import Nextpagetwo from "./components/Nextpagetwo/index";
import Sliders from "./components/Sliders/index";
import MyButton from './Src/testButton'
// import Navigation from "./components/Navigation";
// import Maincontainer from "./components/Navigation/Maincontainer";
// import { NavigationContainer } from "@react-navigation/native";

export default function App() {
  return (
    <div>
      {/* <NavigationContainer> */}
      {/* <Wallpaper />
      <Aiditem />
      <Nextpage />
      <Nextpagetwo /> */}
      <Sliders />
      {/* <Maincontainer /> */}
      {/* </NavigationContainer> */}

      {/* <StatusBar style="auto" /> */}
      <MyButton />
    </div>
  );
}

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "#fff",
//     alignItems: "center",
//     justifyContent: "center",
//   },
// });

// import React from "react";
// import { View, Text, ImageBackground } from "react-native";
// import styles from "./styles";

// const  = () => {
//   return (
//     <View>
//       <View>
//         <Text>Hearing Aid Guide</Text>
//         <Text>To make your life easier</Text>
//       </View>
//     </View>
//   );
// };

// export default ;

// import { StyleSheet } from "react-native";

// const styles = StyleSheet.create({

// });

// export default styles;
