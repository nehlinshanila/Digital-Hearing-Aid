import "./navbar.css";

const Navbar = () => {
  return (
    <div>
      <nav className="navbar">
        <div className="navbar_container">
          <div className="wrapper">
            <div className="sidebar">
              <ul>
                <h1>Dashboard</h1>
                <li>
                  <a className="active" href="#Home">
                    Home
                  </a>
                </li>
                <li>
                  <a href="#Signup">Signup</a>
                </li>
                <li>
                  <a href="#About">About</a>
                </li>
                <li>
                  <a href="#LogIn">LogIn</a>
                </li>
                <li>
                  <a href="#Contact">Contact</a>
                </li>
              </ul>
            </div>
            <div className="main">
              <div className="header"></div>
            </div>
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Navbar;
