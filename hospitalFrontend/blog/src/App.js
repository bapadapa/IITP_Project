import React from "react";
import SearchBar from "./component/SearchBar";
import Map from "./component/Map";
import "./App.css";
import ss from "./image/ss.png";
import cng from "./image/충남대.png";

const App = () => {
  return (
    <div className="full">
      <div>
        <section>
          <div className="App">
            <div className="App-header">
              <div className="searhbox">
                <div>
                  <img className="image1" src={ss} alt="통합의료" />
                </div>
                <div className="A">
                  <div>
                    <SearchBar />
                  </div>
                  <div>
                    <Map />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <div>
          <div className="under">
            <section>
              <footer className="hos">
                <a
                  className="hos"
                  href="http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <img src={cng} className="hos" alt="코로나 링크" />
                </a>
              </footer>
            </section>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
