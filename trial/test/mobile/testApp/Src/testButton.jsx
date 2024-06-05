import React, { useState } from "react";
import { View, Text, StyleSheet, Button } from "react-native";

const MyButton = () => {
  const [count, setCount] = useState(0);

  const onPressButton = () => {
    console.log("Button pressed");
    setCount(count + 1);
  };

  return (
    <div>
      <View style={styles.container}>
        <Text style={styles.title}>My App</Text>
        <Button title="Press me" onPress={onPressButton} />
        <p>{count}</p>
      </View>
    </div>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
  },
});

export default MyButton;
