import React from "react";
import aa from "../image/aa.png";
// import { Switch, Route, Link, useHistory } from "react-router-dom";

class Banner extends React.Component {
  render() {
    const imagestyle = {
        height: "100px",  
        width: "100%",
          };
    return (
      <div>
        <section>
          <div>
            <a
              className="aa"
              href="http://ncov.mohw.go.kr/tcmBoardView.do?contSeq=365746"
              target="_blank"
              rel="noopener noreferrer"
            >
              <img className="bb" 
              src={aa}
              style={imagestyle} 
              alt="사회적 거리두기" />
            </a>
          </div>
        </section>
      </div>
    );
  }
}
export default Banner;