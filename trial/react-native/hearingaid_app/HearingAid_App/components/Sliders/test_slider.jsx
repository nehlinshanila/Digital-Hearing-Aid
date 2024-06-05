import { useState } from "react";
import { View, Text } from "react-native";
import Slider from "react-native-slider";
// import Slider from "@react-native-community/slider";
import Sliderstyles from "./sliders_styles";

export default Test_Slider = () => {
    const [value, setValue] = useState(0);
    const styles = Sliderstyles
    return (
            <View style={styles.container}>
                <Slider
                    value={value}
                    minimumValue={0}
                    maximumValue={100}
                    step={1}
                    onValueChange={(newvalue) => setValue(newvalue)}
                    style={styles.slider}
                />
                <Text style={styles.valueText}>{value}</Text>
            </View>
        );
}