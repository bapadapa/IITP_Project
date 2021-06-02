import { Cascader } from "antd";
import { countyName, citysName } from "../../constants";
import React, { useState } from "react";

function onChange(value) {
  console.log(value);
}

const SearchBar = () => {
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
    <Cascader
      options={options}
      onChange={onChange}
      placeholder="Please select"
    />
  );
};
export default SearchBar;
