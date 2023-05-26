function _extends() { _extends = Object.assign ? Object.assign.bind() : function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; }; return _extends.apply(this, arguments); }
import * as React from 'react';
import { View, PanResponder, StyleSheet } from 'react-native';
import Animated, { useAnimatedStyle, useSharedValue } from 'react-native-reanimated';
const VerticalSlider = _ref => {
  let {
    min = 0,
    max = 100,
    step = 1,
    width = 350,
    height = 30,
    borderRadius = 5,
    maximumTrackTintColor = '#3F2DA5',
    minimumTrackTintColor = '#77ADE6',
    showBallIndicator = false,
    ballIndicatorColor = '#ECECEC',
    ballIndicatorWidth = 48,
    ballIndicatorHeight = 48,
    ballIndicatorPosition = -60,
    ballIndicatorTextColor = '#000000',
    showBackgroundShadow = true,
    shadowProps = {},
    renderIndicator = null,
    disabled = false,
    onChange = () => {},
    onComplete = () => {},
    value: currentValue = 0
  } = _ref;
  const {
    shadowOffsetWidth = 0,
    shadowOffsetHeight = 1,
    shadowOpacity = 0.22,
    shadowRadius = 2.22,
    elevation = 3,
    shadowColor = '#000'
  } = shadowProps || {};

  // Calculating Shadow Styles
  const calculateShadowStyles = () => {
    if (showBackgroundShadow) {
      return {
        shadowOffset: {
          width: shadowOffsetWidth,
          height: shadowOffsetHeight
        },
        shadowOpacity,
        shadowRadius,
        elevation,
        shadowColor
      };
    }
    return {};
  };
  const shadowStyles = React.useMemo(calculateShadowStyles, [elevation, shadowColor, shadowOffsetHeight, shadowOffsetWidth, shadowOpacity, shadowRadius, showBackgroundShadow]);
  // End Calculating Shadow Styles

  // Slider base styles
  const calculateBaseStyles = () => ({
    width,
    height,
    borderRadius
  });
  const sliderBaseStyles = React.useMemo(calculateBaseStyles, [width, height, borderRadius]);
  // End Slider base styles

  // Helper Variables
  const _moveStartValue = useSharedValue(0);
  const _value = useSharedValue(currentValue);
  const value = new Animated.Value(currentValue);

  // Calculating Values from props.value
  const calculateValues = () => {
    updateNewValue(currentValue);
  };
  // eslint-disable-next-line react-hooks/exhaustive-deps
  React.useEffect(calculateValues, [currentValue]);

  // Initializing when component mounts
  // eslint-disable-next-line react-hooks/exhaustive-deps
  React.useEffect(calculateValues, []);
  const _calculateValue = gestureState => {
    const ratio = -gestureState.dy / height;
    const diff = max - min;
    return step ? Math.max(min, Math.min(max,
    // @ts-ignore
    _moveStartValue.value + Math.round(ratio * diff / step) * step)) : Math.floor(
    // @ts-ignore
    Math.max(min, _moveStartValue.value + ratio * diff) * 100) / 100;
  };

  // Make values stable stand in between min and max
  const _clamp = (newValue, minValue, maxValue) => {
    return Math.min(Math.max(newValue, minValue), maxValue);
  };
  const updateNewValue = newValue => {
    let valueToUpdate = _clamp(newValue, min, max);
    _value.value = valueToUpdate;
    value.setValue(valueToUpdate);
  };

  // PanResponder handlers
  const onStartShouldSetPanResponder = () => true;
  const onMoveShouldSetPanResponder = () => false;
  const onPanResponderTerminationRequest = () => false;
  const onPanResponderGrant = () => {
    _moveStartValue.value = _value.value;
  };
  const onPanResponderMove = (_event, gestureState) => {
    if (disabled) {
      return;
    }
    onChange(_calculateValue(gestureState));
  };
  const onPanResponderRelease = (_event, gestureState) => {
    if (disabled) {
      return;
    }
    onChange(_calculateValue(gestureState));
  };
  const onPanResponderTerminate = (_event, gestureState) => {
    if (disabled) {
      return;
    }
    onComplete(_calculateValue(gestureState));
  };
  // End PanResponder handlers
  // Value connected to state, slider height Animated Value, ballHeight Animated Value, panResponder
  const panResponder = React.useRef(PanResponder.create({
    onStartShouldSetPanResponder,
    onMoveShouldSetPanResponder,
    onPanResponderTerminationRequest,
    onPanResponderGrant,
    onPanResponderMove,
    onPanResponderRelease,
    onPanResponderTerminate
  })).current;
  // End Value connected to state, slider height Animated Value, ballHeight Animated Value, panResponder

  const sliderStyle = useAnimatedStyle(() => ({
    height: (_value.value - min) * height / (max - min),
    backgroundColor: minimumTrackTintColor,
    borderRadius
  }), [_value]);
  const ballStyle = useAnimatedStyle(() => {
    let styles = {
      height: renderIndicator ? ballIndicatorHeight : ballIndicatorWidth,
      left: ballIndicatorPosition,
      width: ballIndicatorWidth,
      bottom: 0,
      backgroundColor: 'transparent',
      borderRadius: 0
    };
    // If renderIndicator is provided, then we don't need to calculate the position of ballIndicator
    if (!renderIndicator) {
      styles.backgroundColor = ballIndicatorColor;
      styles.borderRadius = ballIndicatorWidth;
    }
    let _sliderHeight = (_value.value - min) * height / (max - min);
    let _ballPosition = _sliderHeight;
    const _ballHeight = renderIndicator !== null ? ballIndicatorHeight : ballIndicatorWidth;
    if (_ballPosition + _ballHeight >= height) {
      _ballPosition = height - _ballHeight;
    } else if (_ballPosition - _ballHeight <= 0) {
      _ballPosition = 0;
    } else {
      _ballPosition = _ballPosition - _ballHeight / 2;
    }
    styles.bottom = _ballPosition;
    return styles;
  }, [_value]);
  return /*#__PURE__*/React.createElement(View, {
    style: [shadowStyles, sliderBaseStyles]
  }, /*#__PURE__*/React.createElement(View, _extends({
    style: [styles.container, sliderBaseStyles, {
      backgroundColor: maximumTrackTintColor
    }]
  }, panResponder.panHandlers), /*#__PURE__*/React.createElement(Animated.View, {
    style: [sliderBaseStyles, styles.slider, sliderStyle]
  })), showBallIndicator && /*#__PURE__*/React.createElement(Animated.View, {
    style: [styles.ball, shadowStyles, ballStyle],
    pointerEvents: "none"
  }, renderIndicator ?
  // @ts-ignore
  renderIndicator(_value.value) : /*#__PURE__*/React.createElement(Animated.Text, {
    style: [styles.ballText, {
      color: ballIndicatorTextColor
    }]
  }, value)));
};
const styles = StyleSheet.create({
  ball: {
    position: 'absolute',
    alignItems: 'center',
    justifyContent: 'center'
  },
  ballText: {
    fontWeight: '900'
  },
  container: {
    overflow: 'hidden'
  },
  slider: {
    position: 'absolute',
    bottom: 0,
    borderRadius: 0
  }
});
export default VerticalSlider;
//# sourceMappingURL=index.js.map