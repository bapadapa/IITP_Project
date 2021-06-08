import React from "react";
// import covidBanner from "/images/covidBanner.png";
// import { Switch, Route, Link, useHistory } from "react-router-dom";

const Banner = () => {
  return (
    <div>
      <section>
        <div>
          <a
            className="covidBanner"
            href="http://ncov.mohw.go.kr/tcmBoardView.do?contSeq=365746"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              className="bb"
              src="/images/covidBanner.png"
              alt="사회적 거리두기"
            />
          </a>
        </div>
      </section>
    </div>
  );
};
export default Banner;
