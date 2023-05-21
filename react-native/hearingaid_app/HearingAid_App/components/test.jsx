import React, { useState } from 'react';
import { View, Button, Text } from 'react-native';

const MyComponent = () => {
  const [isComponentVisible, setComponentVisible] = useState(true);

  const toggleComponentVisibility = () => {
    setComponentVisible(!isComponentVisible);
  };

  return (
    <View>
      {isComponentVisible ? (
        <View>
          {/* Component 1 */}
          <Text>This is Componentouierftbnajfuiobsndehvjcvkjdn lbjndvkivbkjnd lsvjnx kd 1</Text>
        </View>
      ) : (
        <View>
          {/* Component 2 */}
          <Text>This is Component 2</Text>
        </View>
      )}

      <Button
        title={isComponentVisible ? 'Hide Component 1' : 'Hide Component 2'}
        onPress={toggleComponentVisibility}
      />
    </View>
  );
};

export default MyComponent;
