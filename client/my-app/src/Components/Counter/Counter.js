import React from 'react';

export const Counter = ({data})=> {

    function activateLasers1() {
        console.log('You clicked 1.');
    }
        
  return(
    <div>
        <h1>
            I will sniff packets for 30s.
        </h1>
        <button onClick={activateLasers1}>
            Start sniffing
        </button>
    </div>
  )
}