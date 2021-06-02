import React from "react";
import Map from "./component/Map";
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
          <Route exact={true} path="/info/:city/:county">
            <div>
              <Main2 />
            </div>
          </Route>
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
