import axios from "axios";
import "./index.css";
import MyMapComponent from "../others/maps/Map";
import { API_URL, countyName, citysName } from "../constants";
<<<<<<< HEAD
import { useHistory } from "react-router-dom";
import React from "react";
import { Cascader, Form, Button, Divider, message } from "antd";
=======
import { Route, useHistory, Link } from "react-router-dom";
import React from "react";
import { Cascader, Form, Button, Divider, message } from "antd";
import { unstable_renderSubtreeIntoContainer } from "react-dom";

>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
// import SearchBar from "../SearchBar/";
// import SearchBar from "../others/serchBar";
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
    // console.log("병원정보 : ", hos_infos[0]);
    // console.log("위도 : ", hos_infos[0]["loc_Latitude"]);
    // console.log("경도 : ", hos_infos[0]["loc_longitude"]);
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

<<<<<<< HEAD
  return (
    <div className="selectFrom">
      <Form name="selectHos" onFinish={onSubmit} className="searchBar">
        <Form.Item name="selectHospital">
          <Cascader
            size="large"
            id="searchCas"
            options={options}
            onChange={onChange}
            placeholder="Please select"
          />
        </Form.Item>
        <Form.Item>
          <Button id="submit-buttion" size="large" htmlType="submit">
            병원 선택
          </Button>
        </Form.Item>
      </Form>
      <div>
        <MyMapComponent hosInfos={hos_infos} />
      </div>
    </div>
  );
=======
  return <SearchBar />;
>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
}
export default MainPage;
