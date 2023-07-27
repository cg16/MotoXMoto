import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

#Criar tabelas

c.execute('''
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
    TanqueCombustivelLitros DECIMAL NOT NULL,
    ProcedenciaMoto TEXT NOT NULL,
    UrlImagem TEXT NOT NULL
);
''')

c.execute('''CREATE TABLE Comentario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeUsuario TEXT NOT NULL,
    UsuarioId INTEGER NOT NULL,
    Comentario TEXT NOT NULL,
    MotoId INTEGER NOT NULL,
    FOREIGN KEY(MotoId) REFERENCES Moto(id),
    FOREIGN KEY(UsuarioId) REFERENCES Usuario(id)
);''')

c.execute('''CREATE TABLE Usuario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeUsuario TEXT NOT NULL,
    SenhaUsuario TEXT NOT NULL
);
''')

#Inserir uma moto na tabela motos

#CB 300R
c.execute('''INSERT INTO Moto 
(NomeMoto, MarcaMoto, CilindradaMoto, AnoMoto, TabelaFipe, ConsumoMotoCidade, 
ConsumoMotoEstrada, TempoZeroCemMoto, VelocidadeMaximaMoto, MediaSeguroMoto, 
DescIndiceRoubosMoto, CodigoIndiceRoubosMoto, TanqueCombustivelLitros, 
ProcedenciaMoto, UrlImagem) 
VALUES ('CB 300R', 'Honda', 300, 2014, 12000, 25.6, 30.1, 7.8, 160, 1900, 
'Moto muito roubada', 10, 18, 'Nacional', 
'https://i.ytimg.com/vi/Svbv-NuZd4w/maxresdefault.jpg')'''
)

#CG 160 FAN

c.execute('''INSERT INTO Moto
(NomeMoto, MarcaMoto, CilindradaMoto, AnoMoto, TabelaFipe, ConsumoMotoCidade,
ConsumoMotoEstrada, TempoZeroCemMoto, VelocidadeMaximaMoto, MediaSeguroMoto,
DescIndiceRoubosMoto, CodigoIndiceRoubosMoto, TanqueCombustivelLitros,
ProcedenciaMoto, UrlImagem)
VALUES ('CG 160 FAN', 'Honda', 160, 2014, 9000, 35.4, 40.0, 8.8, 150, 1000,
'Moto muito roubada', 7, 14.6, 'Nacional',
'https://cdn.awsli.com.br/2500x2500/960/960087/produto/35684479/55bb666b5e.jpg')'''
)
          
#Suzuki Intruder 125

c.execute('''INSERT INTO Moto
(NomeMoto, MarcaMoto, CilindradaMoto, AnoMoto, TabelaFipe, ConsumoMotoCidade,
ConsumoMotoEstrada, TempoZeroCemMoto, VelocidadeMaximaMoto, MediaSeguroMoto,
DescIndiceRoubosMoto, CodigoIndiceRoubosMoto, TanqueCombustivelLitros,
ProcedenciaMoto, UrlImagem)
VALUES ('Suzuki Intruder 125', 'Suzuki', 125, 2014, 7000, 39.1, 45.1, 10.8, 110, 650.0,
'Moto pouco roubada', 2, 18, 'Nacional',
'https://images.tcdn.com.br/img/img_prod/872576/suzuki_intruder_125_ce_2012_2013_preta_5739_1_ba18223c978dfa30dd4215d96be92875.jpeg')'''
)

#Kawasaki Ninja 300

c.execute('''INSERT INTO Moto
(NomeMoto, MarcaMoto, CilindradaMoto, AnoMoto, TabelaFipe, ConsumoMotoCidade,
ConsumoMotoEstrada, TempoZeroCemMoto, VelocidadeMaximaMoto, MediaSeguroMoto,
DescIndiceRoubosMoto, CodigoIndiceRoubosMoto, TanqueCombustivelLitros,
ProcedenciaMoto, UrlImagem)
VALUES ('Kawasaki Ninja 300', 'Kawasaki', 300, 2014, 25000, 25.6, 30.1, 7.8, 190, 1200,
'Moto pouco roubada', 4, 18, 'Estangeira',
'https://motosnovas.com.br/wp-content/uploads/2014/03/ninja-300-2014.jpg')'''
)

#Commitando as alterações

conn.commit()