import React from 'react';
import './Header.css'

const Header = () => {
  return (
    <div className='header'>
      <button className='homepage' onClick={() => alert('Página Inicial')}>HomePage</button>
      <h2>Moto X Moto</h2>
      <button className='loginbutton' onClick={() => alert('Clique em Login')}>Login</button>
    </div>
  );
};


export default Header;