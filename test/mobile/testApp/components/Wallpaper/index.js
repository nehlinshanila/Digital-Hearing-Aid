import React from "react";
import { View, Text, ImageBackground } from "react-native";
import Styledbuttons from "../Styledbuttons";

const Wallpaper = () => {
  return (
    <ImageBackground
      source={require("../../assets/images/wall.jpg")}
      style={{
        position: "absolute",
        width: "100%",
        height: "100%",
      }}
    />
  );
};

export default Wallpaper;
