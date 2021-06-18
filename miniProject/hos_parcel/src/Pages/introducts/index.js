import React from "react";
import "./index.scss";
import { Link } from "antd";
const IntrocutTeam = () => {
  return (
    <div className="member-introduct-box">
      <div className="member-name">불사조 팀입니다.</div>
      <div id="member-list">
        {/* 이부분은 반복문으로 변경할 것임. */}
        
        <div className="member-block">
          <div className="teamMember-imgBox">
            <img className="teamMember-img" src="./images/icons/man.png" />
          </div>
          <div className="teamMember-contents">
            <span className="teamMember-name">이름 : 백승현</span>
            <span className="teamMember-position">직책 : 팀장</span>
            <span className="teamMember-major">전공 : 컴퓨터</span>
          </div>
        </div>
        <div className="member-block">
          <div className="teamMember-imgBox">
            <img className="teamMember-img" src="./images/icons/man.png" />
          </div>
          <div className="teamMember-contents">
            <span className="teamMember-name">이름 : 이재성</span>
            <span className="teamMember-position">직책 : 팀원</span>
            <span className="teamMember-major">전공 : 미술</span>
          </div>
        </div>
        <div className="member-block">
          <div className="teamMember-imgBox">
            <img className="teamMember-img" src="./images/icons/woman.png" />
          </div>
          <div className="teamMember-contents">
            <span className="teamMember-name">이름 : 공성경</span>
            <span className="teamMember-position">직책 : 팀원</span>
            <span className="teamMember-major">전공 : 화학</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default IntrocutTeam;
