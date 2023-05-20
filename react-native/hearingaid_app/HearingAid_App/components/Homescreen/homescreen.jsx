import React from 'react';
import {View, Text} from 'react-native';

const Homescreen = navigation => {
  return (
    <View>
      <Text
        onPress={() => alert('This is the Homescreen')}
        style={{fontSize: 26, fontWeight: 'bold'}}>
        HOMESCREEN
      </Text>
    </View>
  );
};

export default Homescreen;
