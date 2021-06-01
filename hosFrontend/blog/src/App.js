import React from "react";
import SearchBar from "./component/SearchBar";
import Map from "./component/Map";
import './App.css';
import ss from './image/ss.png'
import Footer from "./component/Footer"
import Banner from "./component/Banner"

const App = () => {
  return (
  <div>  
    <section>
      <div>
        <Banner />
      </div>
      <div>
        <div className="App">
          <header className="App-header">       
           <img src={ss}  alt="통합의료" />
            <div>
              <SearchBar/>
                
             </div> 
            <div>
              <Map/>
            </div>
          </header>
        </div>
      </div>
    </section>
    <section>
      <footer>
        <Footer />
      </footer>
    </section>
  </div>
  
  )};
  

  
  

export default App;




