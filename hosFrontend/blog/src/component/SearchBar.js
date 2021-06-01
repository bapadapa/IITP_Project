import React from "react";
// import Category from "../Category";
import "./SearchBar.css"
import {  Space, TreeSelect } from 'antd';


import { AudioOutlined } from '@ant-design/icons';
import Search from "antd/lib/transfer/search";

const { TreeNode } = TreeSelect;
const onSearch = value => console.log(value);
const suffix = (
    <AudioOutlined
      style={{
        fontSize: 20,
        color: '#1890ff',
      }}
    />
  );



class SearchBar extends React.Component{
  state = {
    value: undefined,
  };

  onChange = value => {
    console.log(value);
    this.setState({ value });
  };

    render(){
      const Subject = ['내과','신경과','정신건강의학과','외과','정형외과','신경외과','흉부외과','성형외과','마취통증의학과',
      '산부인과','소아청소년과','안과','이비인후과','피부과','비뇨의학과','비뇨기과','영상의학과','방사선종양학과',
      '병리과','진단검사의학과','결핵과','재활의학과','핵의학과','가정의학과','응급의학과','직업환경의학과','예방의학과',
      '치과','구강악안면외과','치과보철과','치과교정과','소아치과','치주과','치과보존과','구강내과','영상치의학과',
      '구강악안면방사선과','구강병리과','예방치과','통합치의학과','한방내과','한방부인과','한방소아과',
      '한방안·이비인후·피부과','한방안이비인후피부과','한방신경정신과','침구과','한방재활의학과','사상체질과','한방응급'];

      //서울
      const Subject01 = ['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구',
          '동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구',
          '종로구','중구','중랑구']
      
      //충남
      const Subject02 = ['계룡시', '공주시' ,'논산시', '당진시', '보령시', '서산시', '아산시', '천안시',
            '금산군', '부여군', '서천군', '예산군', '청양군', '태안군', '홍성군']

            //강원도
      const Subject03 = ['춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군', '고성군', '양양군']

      //충청북도
      const Subject04 = ['청주시', '충주시', '제천시', '보은군', '옥천군', '영동군', '증평군', '진천군', '괴산군', '음성군', '단양군']

      //전라북도
      const Subject05 = ['전주시', '군산시', '익산시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군', '장수군', '임실군', '순창군', '고창군', '부안군']

      //전라남도
      const Subject06 = ['목포시', '여수시', '순천시', '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군', '장흥군', '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군', '진도군', '신안군']

      //경상북도
      const Subject07 = ['포항시', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시', '상주시', '문경시', '경산시', '군위군', '의성군', '청송군', '영양군', '영덕군', '청도군', '고령군', '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군']

      //경상남도
      const Subject08 = ['창원시', '진주시', '통영시', '사천시', '김해시', '밀양시', '거제시', '양산시', '의령군', '함안군', '창녕군', '고성군', '남해군', '하동군', '산청군', '함양군', '거창군', '합천군']

      //제주도
      const Subject09 = ['제주시', '서귀포시']

      //부산
      const Subject10  = ['중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '강서구', '해운대구', '사하구', '금정구', '연제구', '수영구', '사상구', '기장군']

      //대구
      const Subject11 = ['중구', '동구', '서구', '남구', '북구', '수성구', '달서구', '달성군']

      //인천
      const Subject12 = ['중구', '동구', '미추홀구', '연수구', '남동구', '부평구', '계양구', '서구', '강화군', '옹진군']

      //광주
      const Subject13 = ['동구', '서구', '남구', '북구', '광산구']

      //대전
      const Subject14 = ['동구', '중구', '서구', '유성구', '대덕구']

      //울산
      const Subject15 = ['중구', '남구', '동구', '북구', '울주군']

      //경기도
      const Subject16 = ['수원시', '성남시', '안양시', '안산시', '용인시', '부천시', '광명시', '평택시', '과천시', '오산시', '시흥시', '군포시', '의왕시', '하남시', '이천시', '안성시', '김포시',
      '화성시', '광주시', '여주시', '양평군', '고양시', '구리시', '남양주시', '파주시', '양주시', '포천시', '연천군', '가평군']
      return (
        <div className="searchBar">
           
          <Space direction="vertical">
            {/* <Search> */}
            <TreeSelect 
            showSearch
            style={{ width: '250px'  }}
            placeholder = '시발 좀 되라' 
            onSearch={this.onSearch} 
            enterButton
            allowClear
            multiple
            treeDefaultExpandAll
            object
            suffix={suffix}
             >
    <TreeNode value="서울" title="서울">
{Subject01.map(Subjects01 =>{
       return(
       <TreeNode value={Subjects01} title={Subjects01}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="충청남도" title="충청남도">
{Subject02.map(Subjects02 =>{
       return(
       <TreeNode value={Subjects02} title={Subjects02}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="강원도" title="강원도">
{Subject03.map(Subjects03 =>{
       return(
       <TreeNode value={Subjects03} title={Subjects03}>
  
       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="충청북도" title="충청북도">
{Subject04.map(Subjects04 =>{
       return(
       <TreeNode value={Subjects04} title={Subjects04}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="전라북도" title="전라북도">
{Subject05.map(Subjects05 =>{
       return(
       <TreeNode value={Subjects05} title={Subjects05}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}  
       </TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="전라남도" title="전라남도">
{Subject06.map(Subjects06 =>{
       return(
       <TreeNode value={Subjects06} title={Subjects06}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="경상북도" title="경상북도">
{Subject07.map(Subjects07 =>{
       return(
       <TreeNode value={Subjects07} title={Subjects07}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="경상남도" title="경상남도">
{Subject08.map(Subjects08 =>{
       return(
       <TreeNode value={Subjects08} title={Subjects08}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="제주도" title="제주도">
{Subject09.map(Subjects09 =>{
       return(
       <TreeNode value={Subjects09} title={Subjects09}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="부산" title="부산">
{Subject10.map(Subjects10 =>{
       return(
       <TreeNode value={Subjects10} title={Subjects10}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="대구" title="대구">
{Subject11.map(Subjects11 =>{
       return(
       <TreeNode value={Subjects11} title={Subjects11}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="인천" title="인천">
{Subject12.map(Subjects12 =>{
       return(
       <TreeNode value={Subjects12} title={Subjects12}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="광주" title="광주">
{Subject13.map(Subjects13 =>{
       return(
       <TreeNode value={Subjects13} title={Subjects13}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="대전" title="대전">
{Subject14.map(Subjects14 =>{
       return(
       <TreeNode value={Subjects14} title={Subjects14}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="울산" title="울산">
{Subject15.map(Subjects15 =>{
       return(
       <TreeNode value={Subjects15} title={Subjects15}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

<TreeNode value="경기도" title="경기도">
{Subject16.map(Subjects16 =>{
       return(
       <TreeNode value={Subjects16} title={Subjects16}>

       {Subject.map(Subjects =>{
       return(
       <TreeNode value={Subjects} title={Subjects}></TreeNode>
       )
       })}
</TreeNode>
       )
       })}
</TreeNode>

            </TreeSelect>  
          </Space> 
       
        </div>
       )
    }    
}

export default SearchBar;