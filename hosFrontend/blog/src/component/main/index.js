import axios from "axios";
import "./index.css";
import Map from "../others/maps/Map";
import { API_URL, countyName, citysName } from "../constants";
import { Route, useHistory, Link } from "react-router-dom";
import React from "react";
import { Cascader, Form, Button, Divider, message } from "antd";
import { unstable_renderSubtreeIntoContainer } from "react-dom";

// import SearchBar from "../SearchBar/";
import SearchBar from "../others/serchBar";
function onChange(value) {
  console.log(value);
}

function MainPage() {
  const [hosCity, sethosCity] = React.useState([]);
  const [hosCountry, sethosCountry] = React.useState([]);
  const history = useHistory();
  const [hos_infos, setHos_infos] = React.useState([]);
  //   const [latitute,setLatitue]
  const onSubmit = (values) => {
    let cityCounry = values.selectHospital;
    axios
      // .get(`${API_URL}/hosloc/`)
      .get(`${API_URL}/${cityCounry[0]}/city/${cityCounry[1]}/county/`)
      .then(function (result) {
        const hos_infos = result.data;
        setHos_infos(hos_infos);
        sethosCity(hos_infos[0]["loc_hosCityName"]);
        sethosCountry(hos_infos[0]["loc_hosCountyName"]);
        //  console.log("병원정보 : ", hos_infos);
      })
      .catch(function (error) {
        console.log("Fail to Conn API", error);
      });
  };
  if (hos_infos.length != 0) {
    console.log("병원정보 : ", hos_infos[0]);
    console.log("위도 : ", hos_infos[0]["loc_Latitude"]);
    console.log("경도 : ", hos_infos[0]["loc_longitude"]);
  }

  function onChange(values) {
    sethosCity(values[0]);
    sethosCountry(values[1]);

    //     let cityCounry = value.selectHospital;
    //     axios
    //       // .get(`${API_URL}/hosloc/`)
    //       .get(`${API_URL}/${cityCounry[0]}/city/${cityCounry[1]}/county/`)
    //       .then(function (result) {
    //         hos_infos = result.data;
    //         console.log("병원정보 : ", hos_infos);
    //       })
    //       .catch(function (error) {
    //         console.log("Fail to Conn API", error);
    //       });
  }

  let cnt = 0;
  const options = citysName.map((citysName) => {
    return {
      value: citysName,
      label: citysName,
      children: countyName[cnt++].map((countyName) => {
        return { value: countyName, label: countyName };
      }),
    };
  });

  return <SearchBar />;
}
export default MainPage;
