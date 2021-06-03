import React from "react";
<<<<<<< HEAD
import SearchBar from "./component/SearchBar";
=======
import Map from "./component/Map";
>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
import "./App.css";
import ss from "./image/ss.png";
import Footer from "./component/Footer";
import Banner from "./component/Banner";
import { Route, Switch } from "react-router";
import MainPage from "./component/main";
import Main2 from "./component/main2";

// import SearchBar2 from "./component/others/serchBar/SearchBar2";
const App = () => {
  return (
    <div className="back">
      <section>
        <header>
          <Banner />
        </header>
        <Switch>
          <Route exact={true} path="/">
            <div>
              <div className="App">
                <div className="App-header">
                  <img src={ss} alt="통합의료" />
                  <div>
                    <MainPage />
                  </div>
                  <div>{/* <Map /> */}</div>
                </div>
              </div>
            </div>
          </Route>
<<<<<<< HEAD
          <Route exact={true} path="/tmp"></Route>
=======
          <Route exact={true} path="/info/:city/:county">
            <div>
              <Main2 />
            </div>
          </Route>
>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
        </Switch>
      </section>
      <section>
        <footer>
          <Footer />
        </footer>
      </section>
    </div>
  );
};
export default App;
