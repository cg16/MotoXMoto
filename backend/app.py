from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sqlite3
import html # Para evitar injeção de código HTML
import bcrypt


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def fetch_bike_data(nome):
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    nome = html.escape(nome) # Evita injeção de código HTML

    # Executa a consulta para obter os dados com base nas entradas do usuário
    query = """
    SELECT NomeMoto, MarcaMoto, CilindradaMoto, AnoMoto, TabelaFipe, ConsumoMotoCidade,
           ConsumoMotoEstrada, TempoZeroCemMoto, VelocidadeMaximaMoto, MediaSeguroMoto,
           DescIndiceRoubosMoto, CodigoIndiceRoubosMoto, TanqueCombustivelLitros,
           ProcedenciaMoto, UrlImagem
    FROM Moto
    WHERE NomeMoto = ?
    """
    cursor.execute(query, (nome,))
    data = cursor.fetchall()

    # Fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Formata os resultados da consulta em uma lista de dicionários
    bike_data = []
    for row in data:
        bike = {
            "NomeMoto": row[0],
            "MarcaMoto": row[1],
            "CilindradaMoto": row[2],
            "AnoMoto": row[3],
            "TabelaFipe": row[4],
            "ConsumoMotoCidade": row[5],
            "ConsumoMotoEstrada": row[6],
            "TempoZeroCemMoto": row[7],
            "VelocidadeMaximaMoto": row[8],
            "MediaSeguroMoto": row[9],
            "DescIndiceRoubosMoto": row[10],
            "CodigoIndiceRoubosMoto": row[11],
            "TanqueCombustivelLitros": row[12],
            "ProcedenciaMoto": row[13],
            "UrlImagem": row[14]
        }
        bike_data.append(bike)

    return bike_data

# Função para obter lista de todas as motos para o dropdown

@app.route('/bike_list', methods=['GET'])

def fetch_bike_list():
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Executa a consulta para obter os dados com base nas entradas do usuário
    query = """
    SELECT *
    FROM Moto
    """
    
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    # Formata os resultados da consulta em uma lista de dicionários
    bike_list = []
    for row in data:
        bike = {
            "IdMoto": row[0],
            "NomeMoto": row[1], 
            "MarcaMoto":row[2], 
            "CilindradaMoto":row[3], 
            "AnoMoto":row[4], 
            "TabelaFipe":row[5], 
            "ConsumoMotoCidade":row[6],
            "ConsumoMotoEstrada":row[7],
             "TempoZeroCemMoto":row[8], 
             "VelocidadeMaximaMoto":row[9], 
             "MediaSeguroMoto":row[10],
             "DescIndiceRoubosMoto":row[11], 
             "CodigoIndiceRoubosMoto":row[12],
             "TanqueCombustivelLitros":row[13],
             "ProcedenciaMoto":row[14], 
             "UrlImagem":row[15]
        }
        bike_list.append(bike)

    return bike_list

def autenticar_usuario(usuario, senha):
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    usuario = html.escape(usuario)
    senha = html.escape(senha)

    # Executa a consulta para verificar se o usuário existe e a senha corresponde
    query = """
    SELECT id, Senha FROM Usuario WHERE Usuario = ?
    """
    cursor.execute(query, (usuario,))
    user_data = cursor.fetchone()

    # Se o usuário for encontrado e a senha corresponder, retorna o user_id
    if user_data and bcrypt.checkpw(senha.encode('utf-8'), user_data[1]):
        user_id = user_data[0]
        return user_id

    # Fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

    return None

def cadastrar_usuario(usuario, senha):
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    usuario = html.escape(usuario)
    senha = html.escape(senha)

    hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())


    try:
        # Executa a consulta para inserir o novo registro de usuário
        query = """
        INSERT INTO Usuario (Usuario, Senha) VALUES (?, ?)
        """
        cursor.execute(query, (usuario, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Se o nome de usuário já existe (violação de restrição UNIQUE)
        return False
    finally:
        # Fecha a conexão com o banco de dados
        cursor.close()
        conn.close()

@app.route('/compare_bikes', methods=['POST'])
def comparar_motos():
    # Obtém a entrada do usuário a partir do payload JSON enviado pelo frontend
    data = request.get_json()

    nome_moto = html.escape(data.get('NomeMoto'))
    # marca_moto = data.get('MarcaMoto')
    # ano_moto = data.get('AnoMoto') #celsinho pediu pra tirar

    # Obtém os dados das motos no banco de dados
    motos = fetch_bike_data(nome_moto)

    # Retorna a resposta JSON com os dados das motos
    return jsonify(motos)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = html.escape(data.get('usuario'))
    senha = html.escape(data.get('senha'))

    # Autentica o usuário
    autenticado = autenticar_usuario(usuario, senha)

    # Retorna o resultado da autenticação em JSON
    return jsonify({"autenticado": autenticado})

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = html.escape(data.get('usuario'))
    senha = html.escape(data.get('senha'))

    # Registra o novo usuário
    sucesso = cadastrar_usuario(usuario, senha)

    # Retorna o resultado do registro em JSON
    return jsonify({"sucesso": sucesso})

def inserir_comentario(nome_usuario, usuario_id, comentario, moto_id):
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    nome_usuario = html.escape(nome_usuario)
    comentario = html.escape(comentario)

    try:
        # Executa a consulta para inserir um novo comentário na tabela Comentarios
        query = """
        INSERT INTO Comentarios (NomeUsuario, UsuarioId, Comentario, MotoId)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (nome_usuario, usuario_id, comentario, moto_id))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Erro ao inserir comentário: {e}")
        return False
    finally:
        # Fecha a conexão com o banco de dados
        cursor.close()
        conn.close()

def ler_comentarios_por_moto(moto_id):
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Executa a consulta para obter os comentários relacionados à moto específica
    query = """
    SELECT NomeUsuario, Comentario FROM Comentarios WHERE MotoId = ?
    """
    cursor.execute(query, (moto_id,))
    data = cursor.fetchall()

    # Fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Formata os resultados da consulta em uma lista de dicionários
    comentarios = []
    for row in data:
        comentario = {
            "NomeUsuario": row[0],
            "Comentario": row[1],
        }
        comentarios.append(comentario)

    return comentarios

@app.route('/inserir_comentario', methods=['POST'])
def inserir_comentario_route():
    data = request.get_json()
    nome_usuario = data.get('nome_usuario')
    usuario_id = data.get('usuario_id')
    comentario = data.get('comentario')
    moto_id = data.get('moto_id')

    # Insere o novo comentário na tabela Comentarios
    sucesso = inserir_comentario(nome_usuario, usuario_id, comentario, moto_id)

    # Retorna o resultado da inserção em JSON
    return jsonify({"sucesso": sucesso})

@app.route('/ler_comentarios_por_moto', methods=['POST'])
def ler_comentarios_por_moto_route():
    data = request.get_json()
    moto_id = int(data.get('moto_id'))

    # Obtém os comentários relacionados à moto no banco de dados
    comentarios = ler_comentarios_por_moto(moto_id)

    # Retorna a resposta JSON com os comentários
    return jsonify(comentarios)

if __name__ == "__main__":
    app.run(debug=True)
