import React, { Component } from "react";
import { Map, GoogleApiWrapper, Marker } from "google-maps-react";
import { API_google } from "../../constants";

const mapStyles = {
  width: "100%",
  height: "100%",
};

export class MapContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cords: [
        { lat: 9.96233, lng: 49.80404 },
        { lat: 6.11499, lng: 50.76891 },
        { lat: 6.80592, lng: 51.53548 },
        { lat: 9.50523, lng: 51.31991 },
        { lat: 9.66089, lng: 48.70158 },
      ],
    };
  }

  showMarkers = () => {
    console.log("hosInfo : ", this.props.hosInfos);
    console.log("stateInfo : ", this.state);
    // this.setState(this.props.hosInfos);

    return this.state.cords.map((store, index) => {
      console.log(index);
      return (
        <Marker
          key={index}
          id={index}
          position={{
            lat: store.lat,
            lng: store.lng,
          }}
          onClick={() => console.log("Clicked")}
        />
      );
    });
  };

  handleLoc = () => {
    console.log(this.props.hosInfos);
    if (this.props.hosInfos.length != 0)
      this.setState({
        cords: [
          this.props.hosInfos.map((hosInfos) => {
            return {
              lat: hosInfos["loc_Latitude"],
              lng: hosInfos["loc_longitude"],
            };
          }),
        ],
      });
  };

  showMarker = () => {
    console.log("hosInfo : ", this.props.hosInfos);
    console.log("stateInfo : ", this.state);

    return this.props.hosInfos.map((store, index) => {
      console.log(store.loc_Latitude, store.loc_longitude);
      return (
        <Marker
          key={index}
          id={index}
          position={{
            lat: store.loc_Latitude,
            lng: store.loc_longitude,
          }}
          onClick={() => console.log("Clicked")}
        />
      );
    });
  };

  handleL = () => {
    return this.props.hosInfos.map((hosInfos, index) => {
      return (
        <Marker
          key={index}
          id={index}
          title={"The marker`s title will appear as a tooltip."}
          position={{
            lat: hosInfos.loc_Latitude,
            lng: hosInfos.loc_longitude,
          }}
        />
      );
    });
  };
  render() {
    return (
      <Map
        google={this.props.google}
        zoom={8}
        style={mapStyles}
        initialCenter={{
          lat: 35.95,
          lng: 128.25,
        }}
      >
        {this.showMarker()}
        {/* <Marker
          title={"The marker`s title will appear as a tooltip."}
          name={"SOMA"}
          position={{ lat: 37.778519, lng: -122.40564 }}
        />
        <Marker
          title={"The marker`s title will appear as a tooltip."}
          name={"aa"}
          position={{ lat: 38.778519, lng: -122.40564 }}
        /> */}
        {this.showMarkers()}
      </Map>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: API_google,
})(MapContainer);
