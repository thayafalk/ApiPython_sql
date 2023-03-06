
from flask import Flask, make_response,jsonify,request
import mysql.connector

 
connection = mysql.connector.connect(host='localhost',
    user='root',
    password='12345',
    database='db_apart')
 
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False



# ver todos os apartamentos
@app.route('/apartamentos',methods=['GET'])
def get_apartamentos():
     
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT * FROM apartamentos" )
    meus_apartamentos = my_cursor.fetchall()
    
    apartamentos = list()
    for apartamento in meus_apartamentos:
        apartamentos.append(
            {
               'id': apartamento[0],
               'edificio': apartamento[1],
               'statutos': apartamento[2],
               'valor_aluguel':apartamento[3],
               'locador':apartamento[4]
            }
        )
    
    return make_response(
        jsonify(
            mensagem='Lista de apartamentos',
            dados=apartamentos
        )


    )

# criar apartamento
@app.route('/apartamentos_criar', methods=['POST'])
def createjson():
    data = request.get_json()
    nome_edificio = data['nome_edificio']
    locador = data['locador']
    statutos = data['statutos']
    return jsonify({'resultado' : 'Apartamento criado com sucesso!',
                    'nome_edificio' : nome_edificio,
                    'locador' : locador,
                    'statutos': statutos})
# testar 

#"nome_edificio":"ana",
#"locador":"ana",
#"statutos":"ana"


# criar edificio
@app.route('/edificio_criar', methods=['POST'])
def processjson():
    data = request.get_json()
    nome_edificio = data['nome_edificio']
    endereco = data['endereco']
    return jsonify({'resultado' : 'Apartamento criado com sucesso!',
                    'nome_edificio' : nome_edificio,
                    'endereco' : endereco})
#testar 

#"nome_edificio":"ana",
#"endereco":"ana"




#ver apartamentos disponiveis
@app.route('/apartamentos/statutos',methods=['GET'])
def get_statutos():
     
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT * FROM apartamentos WHERE statutos='disponivel'" )
    meus_apartamentos = my_cursor.fetchall()
    
    apartamentos = list()
    for apartamento in meus_apartamentos:
        apartamentos.append(
            {
               'id': apartamento[0],
               'edificio': apartamento[1],
               'statutos': apartamento[2],
               'valor_aluguel':apartamento[3],
               'locatario_nome':apartamento[4]
            }
        )
    
    return make_response(
        jsonify(
            mensagem='Lista de apartamentos',
            dados=apartamentos
        )


    )
 # alugar apartamento
@app.route('/apartamento_alugar', methods=['POST'])
def alugarjson():
    data = request.get_json()
    nome_locador = data['nome_locador']
    return jsonify({'resultado' : 'Apartamento que você alugou!',
                    'nome_locador' : nome_locador,
                    'valor_aluguel' : '1200,00',
                    'locador': 'Thayna Falkemback',
                    'edificio': 'Rosas'   })

#testar
#"nome_locador": "Paula"





app.run()


