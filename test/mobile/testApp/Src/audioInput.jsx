import React, { useState } from "react";
import { StyleSheet, Text, View, Button } from "react-native";

const AudioInput = ({ onAudioInput }) => {
  const [isRecording, setIsRecording] = useState(false);

  const handleRecord = () => {
    if (isRecording) {
      onAudioInput(new AudioRecording());
    } else {
      // Start recording
    }
    setIsRecording(!isRecording);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Audio Input</Text>
      <Button
        title={isRecording ? "Stop Recording" : "Start Recording"}
        onPress={handleRecord}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  text: {
    fontSize: 20,
    fontWeight: "bold",
  },
});

export default AudioInput;
