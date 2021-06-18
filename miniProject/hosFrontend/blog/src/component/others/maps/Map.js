<<<<<<< HEAD
import React, { Component } from "react";
=======
import React, { Component, useState } from "react";
>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
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
<<<<<<< HEAD
        { lat: 9.96233, lng: 49.80404 },
        { lat: 6.11499, lng: 50.76891 },
        { lat: 6.80592, lng: 51.53548 },
        { lat: 9.50523, lng: 51.31991 },
        { lat: 9.66089, lng: 48.70158 },
=======
        this.props.hosInfos.map((hosInfos) => {
          return {
            lat: hosInfos["loc_Latitude"],
            lng: hosInfos["loc_longitude"],
          };
        }),
>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
      ],
    };
  }

  showMarkers = () => {
<<<<<<< HEAD
    console.log("hosInfo : ", this.props.hosInfos);
    console.log("stateInfo : ", this.state);
    // this.setState(this.props.hosInfos);

    return this.state.cords.map((store, index) => {
      console.log(index);
=======
    console.log("cords", this.state[0]);
    console.log("hosInfo : ", this.props.hosInfos);
    console.log("stateInfo : ", this.state);

    return this.state.cords.map((store, index) => {
      // console.log(index);
>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
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
<<<<<<< HEAD
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
=======
>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
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

<<<<<<< HEAD
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
=======
  render() {
    // if (this.props.hosInfos != undefined) {
    //   let a = {};
    //   for (var i = 0; i < this.props.hosInfos.length; i++) {
    //     a.push({
    //       lat: this.props.hosInfos[i].loc_hosAddress,
    //       lng: this.props.hosInfos[i].loc_longitude,
    //     });
    //   }
    // }

>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
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
<<<<<<< HEAD
        {this.showMarker()}
        {/* <Marker
          title={"The marker`s title will appear as a tooltip."}
          name={"SOMA"}
          position={{ lat: 37.778519, lng: -122.40564 }}
=======
        {this.props.hosInfos.map((hosInfos, index) => {
          // console.log(hosInfos.loc_Latitude, hosInfos.loc_longitude);
          let mark = {
            lat: hosInfos.loc_Latitude,
            lng: hosInfos.loc_longitude,
          };
          // console.log(mark);
          // console.log("hosInfo : ", this.props.hosInfos[0]);
          var a = this.state.cords;
          console.log("cords : ", a[0]);
          // const { a, b } = this.state.cords;
          // console.log(a, b);
          return (
            <Marker
              key={index}
              id={index}
              title={hosInfos.loc_hosAddress}
              name={hosInfos.loc_hosName}
              position={this.state.cords[index]}
            />
          );
        })}

        <Marker
          title={"The marker`s title will appear as a tooltip."}
          name={"SOMA"}
          position={{ lat: 36.778519, lng: 128.25 }}
          onClick={() => console.log("Clicked")}
>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
        />
        <Marker
          title={"The marker`s title will appear as a tooltip."}
          name={"aa"}
<<<<<<< HEAD
          position={{ lat: 38.778519, lng: -122.40564 }}
        /> */}
        {this.showMarkers()}
=======
          position={{ lat: 35.778519, lng: 128.25 }}
          onClick={() => console.log("Clicked")}
        />
>>>>>>> a9430519e2a62ee2deb499bebf8f85c98498e7ca
      </Map>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: API_google,
})(MapContainer);
