import React from "react";
import Banner from "./Pages/others/banner";

import { Route, Switch } from "react-router";
import "./App.scss";
// Route할 페이지 import
import MainPage from "./Pages/main";
import IntrocutTeam from "./Pages/introducts";
const App = () => {
  return (
    <div>
      {/* Header */}
      <section>
        <header>
          <Banner />
        </header>
      </section>
      {/* body */}
      <section>
        <Switch>
          <Route exact={true} path="/">
            <MainPage />
          </Route>
          <Route exact={true} path="/introducts">
            <IntrocutTeam />
          </Route>
        </Switch>
      </section>
      {/* Footer */}
      <section>
        <footer>
          <div id="serviceNameArea">
            <a href="/">
              <h2>우리는 불사조다</h2>
            </a>
          </div>
          <ul>
            <a href="/introducts">
              <h2>하이하이</h2>
            </a>
          </ul>
        </footer>
      </section>
    </div>
  );
};
export default App;
