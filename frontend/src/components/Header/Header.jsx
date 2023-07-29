import React from 'react';
import './Header.css'
import { AiOutlineHome,AiOutlineUser } from 'react-icons/ai'

const Header = () => {
  return (
    <div className='header'>
      <div className="link">
        <AiOutlineHome />
        <a className='homepage' href='/'>HomePage</a>

      </div>
      <h2>Moto X Moto</h2>
      <div className="link">
        <AiOutlineUser />
        <a className='homepage' href='/login'>Login</a>

      </div>
    </div>
  );
};


export default Header;