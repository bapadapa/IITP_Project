import React from "react";
import GoogleMap from "google-map-react";
import "./map.css"
import dotenv from "dotenv";

class Map extends React.Component {
  render() {

    const style = {
 
      border: '3px solid gray',
      margin: '3px'
 
    }

    return (
      <div style={style} >
        <div className="map">
        <GoogleMap
        	bootstrapURLKeys = {{ key: 'AIzaSyD8EgsVkN4piVZgJuoUGs-Qbg80GlbQzlM' }}
          	defaultZoom={15}
          	defaultCenter={{ lat: 37.5, lng: 127 }}
            
        ></GoogleMap>
        </div>
    </div>
    );
  }
}
dotenv.config();
export default Map;