import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Form from "./components/Form";
import Title from "./components/Title";

function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('http://localhost:5000/flask/hello').then(response => {
      console.log("SUCCESS", response)
      console.log(response)
      setGetMessage(response.data.message)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <div className='main-container'>
      <Title/>
      <Form/>
    </div>
  );
}

export default App;