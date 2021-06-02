import axios from "axios";
import "./index.css";
import { API_URL, countyName, citysName } from "../../constants";
import { useHistory } from "react-router-dom";
import React from "react";
import { Cascader, Form, Button, Divider, message } from "antd";
// import SearchBar from "../SearchBar/";
// import SearchBar from "../others/serchBar";
function onChange(value) {
  console.log(value);
}

function SearchBar() {
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
        //  console.log("병원정보 : ", hos_infos);
      })
      .catch(function (error) {
        console.log("Fail to Conn API", error);
      });
  };
  if (hos_infos.length != 0) {
  }

  function onChange(value) {}

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
    </div>
  );
}
export default SearchBar;