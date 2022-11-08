import React from 'react';
import './App.css';
import {Text, BlogInit} from './components'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import PageLayout from "./pages/Layout";

function App() {
  return (
      // 路由配置
      <BrowserRouter>
        <div className="App">
          <Routes>
              <Route path='/' element={<PageLayout/>}>
                  <Route path='/text/format' element={<Text/>}/>
                  <Route path='/text/blog' element={<BlogInit/>}/>
              </Route>
          </Routes>
        </div>
      </BrowserRouter>
  );
}

export default App;
