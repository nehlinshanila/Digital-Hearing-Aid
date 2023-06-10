import React from "react";
import { View, Text, ImageBackground, Button } from "react-native";
import styles from "./styles";


const Nextpage = ({ navigation }) => {
  return (
    <View>
      <Text>Screen One</Text>
      <Button
        title="Go to Screen Two"
        onPress={() => navigation.navigate("ScreenTwo")}
      />
    </View>
  );
};

export default Nextpage;