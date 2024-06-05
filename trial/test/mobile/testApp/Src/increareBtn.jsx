import React, { useState } from "react";
const ButtonTest = () => {
  const [count, setCount] = useState(0);
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Click me</button>
      <p>{val}</p>
    </div>
  );
};

export default ButtonTest;
