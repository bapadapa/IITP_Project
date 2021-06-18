import React from "react";
import { useParams } from "react-router-dom";

import MapContainer from "../others/maps/Map";
import SearchBar from "../others/serchBar";
import dream from "../../image/dream.png";
import axios from "axios";
import { API_URL } from "../constants";
import { scroll } from "../others/scroll";
const Main2 = () => {
  const { city, county } = useParams([]);
  const [hosInfo, setHosInfo] = React.useState([]);
  // console.log(city, county);

  React.useEffect(function () {
    axios
      // .get(`${API_URL}/hosloc/`)
      .get(`${API_URL}/${city}/city/${county}/county/`)
      .then(function (result) {
        const hosInfo = result.data;
        setHosInfo(hosInfo);
        // console.log(hosInfo);
      })
      .catch(function (error) {
        console.log("Fail to Conn API", error);
      });
  }, []);
  if (hosInfo.length != 0 && hosInfo[0]["loc_hosCityName"] != city)
    axios
      // .get(`${API_URL}/hosloc/`)
      .get(`${API_URL}/${city}/city/${county}/county/`)
      .then(function (result) {
        const hosInfo = result.data;
        setHosInfo(hosInfo);
        console.log(hosInfo);
      })
      .catch(function (error) {
        console.log("Fail to Conn API", error);
      });
  return (
    <div className="full">
      <div className="All">
        <div className="AK">
          <div className="App0">
            <div className="Ap">
              <div className="App01">
                <SearchBar />
                <div className="App02"></div>
              </div>
            </div>
          </div>
          <div className="App11">
            <div className="App1">
              <MapContainer hosInfos={hosInfo} />
            </div>
          </div>
          <div className="infos">
            {hosInfo.map(function (hosInfo, index) {
              return (
                <div className="infoSpan">
                  <span className="hosInfo.loc_hosName">
                    병원 이름 : {hosInfo.loc_hosName + "      "}
                  </span>
                  <span className="hosInfo.loc_hosAddress">
                    주소 : {hosInfo.loc_hosAddress}
                  </span>
                </div>
              );
            })}
          </div>
          <div>
            <img
              src={dream}
              border=" 3px solid black"
              width="100%"
              alt="통합검색"
            />
          </div>
        </div>
      </div>
    </div>
  );
};
export default Main2;
