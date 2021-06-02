import React from "react";
// import Category from "../Category";
import "./SearchBar.css";
import { Space, TreeSelect, Form, Divider, Button } from "antd";
import { API_URL } from "./constants";
import axios from "axios";
import {
  Subject,
  Subject01,
  Subject02,
  Subject03,
  Subject04,
  Subject06,
  Subject05,
  Subject07,
  Subject08,
  Subject09,
  Subject10,
  Subject11,
  Subject12,
  Subject13,
  Subject14,
  Subject15,
  Subject16,
  citysName,
} from "./constants";

import { AudioOutlined } from "@ant-design/icons";
import Search from "antd/lib/transfer/search";

const { TreeNode } = TreeSelect;
const onSearch = (value) => console.log(value);
const suffix = (
  <AudioOutlined
    style={{
      fontSize: 20,
      color: "#1890ff",
    }}
  />
);

class SearchBar extends React.Component {
  state = {
    value: undefined,
  };

  onChange = (value) => {
    console.log(value);
    this.setState({ value });
  };

  render() {
    const onSubmit = (values) => {
      console.log("aa : ", values.selectHospital);
      console.log("aa : ", values);
      let cityCounry = values.selectHospital;
      let hos_infos = Object;
      axios
        // .get(`${API_URL}/hosloc/`)
        .get(`${API_URL}/${cityCounry[0]}/city/${cityCounry[1]}/county/`)
        .then(function (result) {
          hos_infos = result.data;
          console.log("병원정보 : ", hos_infos);
        })
        .catch(function (error) {
          console.log("Fail to Conn API", error);
        });
    };

    return (
      <div className="searchBar">
        <Form name="selectHos" onFinish={onSubmit}>
          <Form.Item name="selectHospital">
            <Space direction="vertical">
              {/* <Search> */}
              <TreeSelect
                showSearch
                style={{ width: "250px" }}
                placeholder="검색할 병원을 선택하세요"
                onSearch={this.onSearch}
                enterButton
                allowClear
                multiple
                treeDefaultExpandAll
                object
                suffix={suffix}
              >
                {/* {citysName.map((citysName) => {
                  return (
                    <TreeNode value={citysName} title={citysName}>
                      {countyName[cnt].map((countyName) => {
                        return (
                          <TreeNode
                            value={countyName}
                            title={countyName}
                          ></TreeNode>
                        );
                      })}
                    </TreeNode>
                  );
                  cnt += 1;
                })} */}

                <TreeNode value="서울" title="서울">
                  {Subject01.map((Subjects01) => {
                    return (
                      <TreeNode value={Subjects01} title={Subjects01}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="충남" title="충남">
                  {Subject02.map((Subjects02) => {
                    return (
                      <TreeNode value={Subjects02} title={Subjects02}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="강원" title="강원">
                  {Subject03.map((Subjects03) => {
                    return (
                      <TreeNode value={Subjects03} title={Subjects03}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="충북" title="충북">
                  {Subject04.map((Subjects04) => {
                    return (
                      <TreeNode value={Subjects04} title={Subjects04}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="전북" title="전북">
                  {Subject05.map((Subjects05) => {
                    return (
                      <TreeNode value={Subjects05} title={Subjects05}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="전남" title="전남">
                  {Subject06.map((Subjects06) => {
                    return (
                      <TreeNode value={Subjects06} title={Subjects06}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="경북" title="경북">
                  {Subject07.map((Subjects07) => {
                    return (
                      <TreeNode value={Subjects07} title={Subjects07}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="경남" title="경남">
                  {Subject08.map((Subjects08) => {
                    return (
                      <TreeNode value={Subjects08} title={Subjects08}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="제주" title="제주">
                  {Subject09.map((Subjects09) => {
                    return (
                      <TreeNode value={Subjects09} title={Subjects09}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="부산" title="부산">
                  {Subject10.map((Subjects10) => {
                    return (
                      <TreeNode value={Subjects10} title={Subjects10}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="대구" title="대구">
                  {Subject11.map((Subjects11) => {
                    return (
                      <TreeNode value={Subjects11} title={Subjects11}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="인천" title="인천">
                  {Subject12.map((Subjects12) => {
                    return (
                      <TreeNode value={Subjects12} title={Subjects12}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="광주" title="광주">
                  {Subject13.map((Subjects13) => {
                    return (
                      <TreeNode value={Subjects13} title={Subjects13}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="대전" title="대전">
                  {Subject14.map((Subjects14) => {
                    return (
                      <TreeNode value={Subjects14} title={Subjects14}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="울산" title="울산">
                  {Subject15.map((Subjects15) => {
                    return (
                      <TreeNode value={Subjects15} title={Subjects15}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>

                <TreeNode value="경기" title="경기">
                  {Subject16.map((Subjects16) => {
                    return (
                      <TreeNode value={Subjects16} title={Subjects16}>
                        {Subject.map((Subjects) => {
                          return (
                            <TreeNode
                              value={Subjects}
                              title={Subjects}
                            ></TreeNode>
                          );
                        })}
                      </TreeNode>
                    );
                  })}
                </TreeNode>
              </TreeSelect>
            </Space>
          </Form.Item>
          <Divider />
          <Form.Item>
            <Button id="submit-buttion" size="large" htmlType="submit">
              병원 선택
            </Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

export default SearchBar;
