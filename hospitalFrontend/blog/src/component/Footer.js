import cng from '../image/충남대.png'
// import footer from
import React from 'react';

class Footer extends React.Component{
    render(){
        const imagestyle = {
            height: "60px",  
            width: "150px",
            float: "right"
              };
      return (
<footer>
<a className="hos" href="http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=" target="_blank" rel="noopener noreferrer">
  <img 
    src={cng}
    style={imagestyle}
    className="ho"
    alt='코로나 링크' />
    </a>
    <div>
      <banner />
    </div>
  </footer>
      )
    };
}
export default Footer;