import React from 'react';
import {View, Text} from 'react-native';

const Amplify = navigation => {
  return (
    <View>
      <Text
        // onPress={() => navigation.navigate()}
        style={{fontSize: 26, fontWeight: 'bold'}}>
        Amplify
      </Text>
    </View>
  );
};

export default Amplify;
