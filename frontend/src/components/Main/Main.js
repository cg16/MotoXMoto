import React from 'react';
import './ProductSelection.css'; 

const ProductSelection = () => {
  return (
    <div className="container">
      <div className="rectangle">
        <button className='buttons'>
          Compare
        </button>
        <div className="selects">
          <select className="productSelect">
            <option value="moto1">Escolha sua moto 1</option>
          </select>

          <select className="productSelect">
            <option value="moto2">Escolha sua moto 2</option>
          </select>
        </div>
      </div>
    </div>
  );
};

export default ProductSelection;