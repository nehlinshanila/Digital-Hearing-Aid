import Navbar from "./components/header/navbar/navbar";
// import Frontpage from "./components/body/frontpage";
import Footer from "./components/footer/footer/footer";

export const App = () => {
  return (
    <div>
      <Navbar />
      {/* <Frontpage /> */}
      {/* <Footer /> */}
    </div>
  );
};

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

export default App;
