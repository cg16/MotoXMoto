import React from "react";

import Header from "./components/Header/Header";
import Main from "./components/Main/Main";
import Footer from "./components/Footer/Footer";

export default function App() {
  return (
    <div className="App">
      <Header title="My header" subtitle="subtitle2" />
      <Main message="My content"/>
      <Footer note="Footer Note"/>
    </div>
  );
}