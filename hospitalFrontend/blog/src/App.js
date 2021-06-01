import React from "react";
// import SearchBar from "./component/SearchBar";
import Map from "./component/Map";
import './App.css';
import ss from './image/ss.png'
// import Text from './component/Text'
import Footer from"./component/Footer";
import Banner from "./component/Banner"
import Search from "antd/lib/transfer/search";
import SearchBar from "./component/SearchBar";
import Icon from "./component/Icon"


const App = () => {
  return (
  <div className ="full"> 

    <div>

        <header className='h'> 
          <Banner />
        </header>
      <section>


        <div className="App">
          <div className="App-header">
            <div className="searhbox">  

              <div>  
                <img className='image1' src={ss}   alt="통합의료" />
              </div>

              <div className="A">
                <div>
                  <SearchBar />
                  <Icon />
                  
                </div> 
                <div>
                  <Map/>
                </div>  
              </div>
              
            </div> 
          </div>
        </div>

      </section>

    <div>

    <div>
      <div>
        <div className='under'>

          <section>

            <div className='ho'>
              <Footer />
            </div> 

          </section>

        </div>
      </div>
    </div>

  </div>
  </div>
  </div>
  )
};
  

export default App;




