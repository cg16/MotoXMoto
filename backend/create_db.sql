--Creating a sqlite database with info about motorcycles

CREATE TABLE Moto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeMoto TEXT NOT NULL,
    MarcaMoto TEXT NOT NULL,
    CilindradaMoto INTEGER NOT NULL,
    AnoMoto INTEGER NOT NULL,
    TabelaFipe INTEGER NOT NULL,
    ConsumoMotoCidade DECIMAL NOT NULL,
    ConsumoMotoEstrada DECIMAL NOT NULL,
    TempoZeroCemMoto DECIMAL NOT NULL,
    VelocidadeMaximaMoto INTEGER NOT NULL,
    MediaSeguroMoto DECIMAL NOT NULL,
    DescIndiceRoubosMoto TEXT NOT NULL,
    CodigoIndiceRoubosMoto INTEGER NOT NULL,
    TanqueCombustivelLitros INTEGER NOT NULL,
    ProcedenciaMoto TEXT NOT NULL,
    UrlImagem TEXT NOT NULL
)

CREATE TABLE Comentario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeUsuario TEXT NOT NULL,
    Comentario TEXT NOT NULL,
    MotoId INTEGER NOT NULL,
    FOREIGN KEY(MotoId) REFERENCES Moto(id)
)

CREATE TABLE Usuario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeUsuario TEXT NOT NULL,
    SenhaUsuario TEXT NOT NULL
)