import React from "react";
import { View, Text, ImageBackground } from "react-native";
import styles from "./styles";
import Styledbuttons from "../Styledbuttons";

const Aiditem = () => {
  return (
    <View>
      <View style={styles.titles}>
        <Text style={styles.title}>Hearing Aid Guide</Text>
        <Text style={styles.lineBreak}></Text>
        <Text style={styles.subtitle}>Welcome to our application</Text>
      </View>
      <Styledbuttons />
    </View>
  );
};

export default Aiditem;




