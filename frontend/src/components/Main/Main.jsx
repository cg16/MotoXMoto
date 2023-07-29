import React, { useEffect, useState } from 'react';
import './ProductSelection.css';

const ProductSelection = () => {
  const [bikeOptions, setBikeOptions] = useState([]);
  const [bike1, setBike1] = useState('')
  const [bike2, setBike2] = useState('')
  const [isCompareClicked, setIsCompareClicked] = useState(false)
  const [bikeFilter, setBikeFilter] = useState([])

  const handleClick = () => {
    if (!bike1) {
      return alert('Selecione a moto 1')
    }
    if (!bike2) {
      return alert('Selecione a moto 2')

    }
    if (bike1 === bike2) {
      return alert('As motos não podem ser iguais ')
    }
    setIsCompareClicked(true)
    const filter = bikeOptions.filter((bike) => bike.NomeMoto === bike1 || bike.NomeMoto === bike2)
    setBikeFilter(filter)
    console.log(filter)

  }
  useEffect(() => {
    // Função para buscar as opções do endpoint '/bike_list'
    const fetchBikeOptions = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/bike_list');

        const data = await response.json();
        console.log(data)
        setBikeOptions(data); // Armazena as opções no estado
      } catch (error) {
        console.error(error);
      }
    };

    fetchBikeOptions(); // Chama a função para buscar as opções
  }, []); // O array vazio como segundo argumento faz com que o useEffect seja executado apenas uma vez, ao montar o componente.

  return (
    <div className="container">
      {!isCompareClicked ? (
        <div className="rectangle">
          <button className='buttons' onClick={() => handleClick()}>
            Compare
          </button>
          <div className="selects">
            <select className="productSelect" onChange={(e) => setBike1(e.target.value)}>
              <option value="">Escolha sua moto 1</option>
              {/* Mapeia as opções e cria um option para cada uma */}
              {bikeOptions.map((bike, index) => {
                return (
                  <option key={index} value={bike.NomeMoto} >
                    {bike.NomeMoto}
                  </option>
                )
              })}
            </select>

            <select className="productSelect" onChange={(e) => setBike2(e.target.value)}>
              <option value="">Escolha sua moto 2</option>
              {/* Mapeia as opções e cria um option para cada uma */}
              {bikeOptions.map((bike, index) => (
                <option key={index} value={bike.NomeMoto} >
                  {bike.NomeMoto}
                </option>
              ))}
            </select>
          </div>
        </div>
      ) : (
        <div className="rectangle_result">
          <div className="bike">

            <img src={bikeFilter[0].UrlImagem} alt="" />
            <h1>{bikeFilter[0].NomeMoto }</h1>
            <ul>
              <li>Marca: {bikeFilter[0].MarcaMoto}</li>
              <li>Cilindrada: {bikeFilter[0].CilindradaMoto}</li>
              <li>Ano: {bikeFilter[0].AnoMoto}</li>
              <li>Tabela FIPE: {bikeFilter[0].TabelaFipe}</li>
              <li>Consumo na cidade: {bikeFilter[0].ConsumoMotoCidade}</li>
              <li>Consumo na estrada: {bikeFilter[0].ConsumoMotoEstrada}</li>
              <li>0-100: {bikeFilter[0].TempoZeroCemMoto}</li>
              <li>Velocidade maxima{bikeFilter[0].VelocidadeMaximaMoto}</li>
              <li>Media de seguro: {bikeFilter[0].MediaSeguroMoto}</li>
              <li>Indice de roubo: {bikeFilter[0].DescIndiceRoubosMoto}</li>
              <li>Codigo de indice de roubo: {bikeFilter[0].CodigoIndiceRoubosMoto}</li>
              <li>Tanque de combustivel: {bikeFilter[0].TanqueCombustivelLitros}</li>
              <li>Procedencia da moto: {bikeFilter[0].ProcedenciaMoto}</li>
              
            </ul>
          </div>
          <div className="bike">
            <img src={bikeFilter[1].UrlImagem} alt="" />
            <h1>{bike2}</h1>
            <ul>
              <li>Marca: {bikeFilter[1].MarcaMoto}</li>
              <li>Cilindrada: {bikeFilter[1].CilindradaMoto}</li>
              <li>Ano: {bikeFilter[1].AnoMoto}</li>
              <li>Tabela FIPE: {bikeFilter[1].TabelaFipe}</li>
              <li>Consumo na cidade: {bikeFilter[1].ConsumoMotoCidade}</li>
              <li>Consumo na estrada: {bikeFilter[1].ConsumoMotoEstrada}</li>
              <li>0-100: {bikeFilter[1].TempoZeroCemMoto}</li>
              <li>Velocidade maxima{bikeFilter[1].VelocidadeMaximaMoto}</li>
              <li>Media de seguro: {bikeFilter[1].MediaSeguroMoto}</li>
              <li>Indice de roubo: {bikeFilter[1].DescIndiceRoubosMoto}</li>
              <li>Codigo de indice de roubo: {bikeFilter[1].CodigoIndiceRoubosMoto}</li>
              <li>Tanque de combustivel: {bikeFilter[1].TanqueCombustivelLitros}</li>
              <li>Procedencia da moto: {bikeFilter[1].ProcedenciaMoto}</li>

            </ul>
          </div>

        </div>
      )}

    </div>
  );
};

export default ProductSelection;