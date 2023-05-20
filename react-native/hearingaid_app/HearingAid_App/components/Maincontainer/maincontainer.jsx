import React from 'react';
import {View, Text} from 'react-native';
import {NavigationContainer} from '@react-navigation/native';
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';
import Ionicons from 'react-native-vector-icons/Ionicons';

// screens

import Homescreen from './Homescreen/homescreen';
import Amplify from './Amplify/amplify';
import Server from './Server/server';

// screen names

const homeName = 'Home';
const amplifyName = 'Amplification';
const serverName = 'Server';

const Tab = createBottomTabNavigator();

export default function Maincontainer() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        initialRouteName={homeName}
        screenOptions={({route}) => ({
          tabBarIcon: ({focused, color, size}) => {
            let iconName;
            let rn = route.name;
            if (rn === homeName) {
              iconName = focused ? 'home' : 'home-outline';
            } else if (rn === amplifyName) {
              iconName = focused ? 'amplify' : 'amplify-outline';
            } else if (rn === serverName) {
              iconName = focused ? 'server' : 'server-outline';
            }

            return <Ionicons name={iconName} size={size} color={color} />;
          },
        })}>
        <Tab.Screen name={homeName} component={Homescreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

// const Maincontainer = navigation => {
//     return (
//       <View>
//         <Text>Maincontainer</Text>
//       </View>
//     );
//   };

//   export default Maincontainer;
