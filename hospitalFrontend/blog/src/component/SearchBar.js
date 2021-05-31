import React from "react";
// import Category from "../Category";
import "./SearchBar.css"
import { Input, Space } from 'antd';
import { AudioOutlined } from '@ant-design/icons';

const { Search } = Input;
const onSearch = value => console.log(value);
const suffix = (
    <AudioOutlined
      style={{
        fontSize: 16,
        color: '#1890ff',
      }}
    />
  );


class SearchBar extends React.Component{

    render(){
        return (
            <div className="searchBar">
                <Space direction="vertical">
    <Search placeholder="input search text" onSearch={onSearch} style={{ width: 200 }} />
    <Search placeholder="input search text" allowClear onSearch={onSearch} style={{ width: 200 }} />
    <Search placeholder="input search text" onSearch={onSearch} enterButton />
    <Search
      placeholder="input search text"
      allowClear
      enterButton="Search"
      size="large"
      onSearch={onSearch}
    />
    <Search
      placeholder="input search text"
      enterButton="Search"
      size="large"
      suffix={suffix}
      onSearch={onSearch}
    />
  </Space>
 

                {/* <main> */}
                {/* <div id="mainLogo">
                  
                </div>
                <input
                    id="pac-input"
                    className="controls"
                    type="text"
                    placeholder="Search Box"
                />
                <Category/>
                </main> */}
            </div>
        )
    }    
}

export default SearchBar;