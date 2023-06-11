import React from "react";
import { View, Text, ImageBackground, Pressable } from "react-native";
import styles from "./styles";

const Styledbuttons = () => {
  return (
    <View style={styles.container}>
      <Pressable style={styles.button} 
        onPress={() => {
            console.warn("HELLO");
        }}>
        <Text style={styles.text}>Pair Device</Text>
      </Pressable>
    </View>
  );
};

export default Styledbuttons;

// on press function called