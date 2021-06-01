import { TreeSelect, Space } from 'antd';
import React from "react";
import './Text.css'

const { TreeNode } = TreeSelect;

class Text extends React.Component {
  state = {
    value: undefined,
  };

  onChange = value => {
    console.log(value);
    this.setState({ value });
  };

  render() {
    const Subject = ['내과','신경과','정신건강의학과','외과','정형외과','신경외과','흉부외과','성형외과','마취통증의학과',
'산부인과','소아청소년과','안과','이비인후과','피부과','비뇨의학과','비뇨기과','영상의학과','방사선종양학과',
'병리과','진단검사의학과','결핵과','재활의학과','핵의학과','가정의학과','응급의학과','직업환경의학과','예방의학과',
'치과','구강악안면외과','치과보철과','치과교정과','소아치과','치주과','치과보존과','구강내과','영상치의학과',
'구강악안면방사선과','구강병리과','예방치과','통합치의학과','한방내과','한방부인과','한방소아과',
'한방안·이비인후·피부과','한방안이비인후피부과','한방신경정신과','침구과','한방재활의학과','사상체질과','한방응급'];
    const Subject01 = ['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구',
    '동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구',
    '종로구','중구','중랑구']


    const Subject02 = ['계룡시', '공주시' ,'논산시', '당진시', '보령시', '서산시', '아산시', '천안시',
      '금산군', '부여군', '서천군', '예산군', '청양군', '태안군', '홍성군']



return (
  <Space direction="vertical">
      <TreeSelect
        showSearch
        style={{ width: '200px'  }}
        value={this.state.value}
        // dropdownStyle={{ maxHeight: 500, overflow: 'auto', }}
        placeholder="시발 좀 되라"
        allowClear
        multiple
        treeDefaultExpandAll
        onChange={this.onChange}
        enterButton
      >
        {/* <section> 의료시설 상세검색 */}
          <TreeNode value="서울" title="서울">
          {Subject01.map(Subjects01 =>{
                return(
                  <TreeNode value={Subjects01} title={Subjects01}>

              {Subject.map(Subjects =>{
                return(
                  <TreeNode value={Subjects} title={Subjects}></TreeNode>
                )
              })}
          <TreeNode value="검색" title={<b style={{ color: '#08c' }}>검색</b>} />
          </TreeNode>
                )
              })}
            </TreeNode>
         
        {/* </section> */}
 {/* <section> 의료시설 상세검색 */}
 <TreeNode value="충청남도" title="충청남도">
          {Subject02.map(Subjects02 =>{
                return(
                  <TreeNode value={Subjects02} title={Subjects02}>

              {Subject.map(Subjects =>{
                return(
                  <TreeNode value={Subjects} title={Subjects}></TreeNode>
                )
              })}
          <TreeNode value="검색" title={<b style={{ color: '#08c' }}>검색</b>} />
          </TreeNode>
                )
              })}
            </TreeNode>
         
        {/* </section> */}

       
      </TreeSelect>
      </Space>
    );
  }
}

// render(<Text />);
export default Text