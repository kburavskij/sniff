import './App.css';
import {useState, useEffect} from 'react';
import { Counter } from './Components/Counter/Counter'

function App() {

  const [initialState, setState] = useState([])
  const url = "/api"
  
  useEffect(()=> {
    fetch(url).then(response => {
      if(response.status === 200){
        return response.json()
      }
    }).then(data => setState(data))
  }, [])

  return (
    <div className="App">
      <Counter data={initialState}/>
    </div>
  );
}

export default App;
