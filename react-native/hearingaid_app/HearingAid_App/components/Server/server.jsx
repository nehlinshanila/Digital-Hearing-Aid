import React from 'react';
import {View, Text} from 'react-native';

const Server = navigation => {
  return (
    <View>
      <Text
        onPress={() => navigation.navigate('Home')}
        style={{fontSize: 26, fontWeight: 'bold'}}>
        Server
      </Text>
    </View>
  );
};

export default Server;
