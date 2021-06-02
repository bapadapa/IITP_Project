import React from "react";
import { Route } from "react-router";

import Map from "../Map";
import hData from "../others/data"
import ss from "../../image/ss.png";
import SearchBar from "../others/serchBar";
import dream from "../../image/dream.png"


const Main2 = () => {

    // const [hosinfos, setHos_infos] = React.useState([]);
    // //   const [latitute,setLatitue]
    //   axios
    //     // .get(`${API_URL}/hosloc/`)
    //     .get(`${API_URL}/"세종시"/city/"세종시"/county/`)
    //     .then(function (result) {
    //       const hos_infos = result.data;
    //       setHos_infos(hos_infos);
    //       //  console.log("병원정보 : ", hos_infos);
    //     })
    //     .catch(function (error) {
    //       console.log("Fail to Conn API", error);
    //     });
    

    return (
<div className="full">
    <div className="All">
        <div className ="AK">
            <div className="App0">
                <div className="Ap">
                    <div className="App01">
                        <SearchBar />
                    <div className="App02">
                </div>
            </div>       
        </div>
    </div>
        <div className="App11">
            <div className="App1">
                <Map/>
            </div>
        </div>
        <div >
            <img 
            src={dream}
            border=" 3px solid black"
            width="100%"
            alt="통합검색" />\
            
        </div>
    </div>
</div>
</div>

)
}
    export default Main2;