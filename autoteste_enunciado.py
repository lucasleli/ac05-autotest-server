from flask import Flask,jsonify,abort
from flask import make_response
from flask import request


app = Flask(__name__)
app.url_map.strict_slashes = False #barras no fim da URL


questoes = [
    {
        'id': 1,
        'pergunta': 'O que quer dizer RPC?',
        'erradas': ['Random Person Changer', 'Renato passa pelo centro' ],
        'corretas': ['Remote procedure call']
    },
    {
        'id': 2,
        'pergunta': 'Quanto vale 2**6?',
        'erradas': [12,36,26,32],
        'corretas': [64]
    }
]

respostas = {
        'marcio':{1:'Random Person Changer'},
        'maria':{1:'Remote procedure call', 2: 64},
        }


#tem uma certa magia envolvida nesse reseta.
#nao precisa se preocupar com isso, tudo
#referente ao reseta já está feito :)
@app.route('/autoteste/reseta', methods = ['POST'])
def reseta_request():
    reseta()
    return {'status':'resetado'}

@app.route('/')
def index():
        return "Testes automáticos!"
'''
REPARE:

Suas funções devem alterar os objetos respostas e questoes

NAO ALTERE NUNCA os objetos respostas_iniciais e questoes_iniciais

A idéia desses respostas_inicias e questoes_iniciais é serem um
valor padrão de referência pros testes
'''

'''
Ao acessar a URL /autoteste/questoes com o verbo GET o usuario deve receber
uma lista completa de todas as questoes

Com isso, passaremos o teste 001 e o 001a (esse ultimo usa as questoes que já vem definidas no servidor, como 'O que quer dizer RPC" e "quanto vale 2**6"
'''

'''
Ao acessar a URL /autoteste/respostas o usuario deve receber
um objeto representando as pessoas e suas respostas, como
definido no inicio do arquivo

Com isso, passaremos o teste 002 e o 002a
'''


'''
Podemos acessar uma questao especifica na URL
/autoteste/questao/<int:q_id>

Se a questao existir, retorne a questao

Se nao existir, retorne um texto de erro e o codigo 404

Com isso, passaremos o teste 003
'''

'''

Ao usarmos o verbo POST na url autoteste/questao

queremos criar uma nova questao.

no corpo da mensagem, enviamos o texto da questao (na chave pergunta),
uma lista de alternativas incorretas (na chave erradas) e uma lista
de alternativas corretas (na chave corretas).

Por exemplo:
    {
        'pergunta': 'O que quer dizer RPC?',
        'erradas': ['Random Person Changer', 'Renato passa pelo centro' ],
        'corretas': ['Remote procedure call']
    }

voce deve armazenar essa nova questao e retornar 
uma representacao JSON dela. Também devolva o codigo de status 201 (created)

Se um dos 3 campos estiver faltando, voce deve retornar um 
texto de erro, e o codigo 400

Com isso feito, passaremos o teste 004. O 004a é referente a um upgrade,
que será descrito em breve

'''

'''
Agora melhore sua funçao, fazendo com que, ao ser acrescentada uma
questão, ela automaticamente ganhe a próxima id disponível
(perceba que o dicionario enviado nao tem id, quem vai ter que escolher é o
servidor)

Essa melhoria é referente ao teste 004a

O teste 005 deveria vir de graça
'''
'''
Agora faça um upgrade na sua busca por questões, dando
um erro quando a questão não é encontrada
Acessando /autoteste/questao/10, por exemplo,
se a questão 10 não existe, devemos ter um cod status 404

Isso se refere ao teste 006
'''

'''
Agora faça um upgrade na criação de questões, dando
um erro quando o dicionário enviado não contém os
3 campos necessários (pergunta, erradas e corretas)
Se faltar a chave erradas, por exemplo,
devemos ter um cod status 400

Isso se refere ao teste 007
'''
'''
Ao usarmos o verbo PUT na url 
/autoteste/questao/<int:q_id>/erradas

queremos adicionar mais alternativas erradas à questão.

enviamos, no corpo do request, uma lista de alternativas 
incorretas, e elas devem ser acrescentadas à questão.

por exemplo:
    {"erradas":[1,2,3,4,5]}

Se a questao não existir, devemos retornar o codigo 404
e uma mensagem de erro

Se a questão existir, devemos retornar a questao modificada

Isso se refere ao teste 008a
'''

'''
Faça um upgrade na sua funcao de adicionar alternativas erradas

Se a alternativa já existir, nao adicione duas vezes

Isso se refere ao teste 008b

Faça também com que tentar adicionar alternativa a uma questão
que não existe resulte cod status 404 

Isso se refere ao teste 008c

'''


'''
faça o mesmo, adicionando alternativas corretas extras

(testes 009a, 009b e 009c)
'''



'''
Respondendo às perguntas

Fazendo um PUT na URL /autoteste/responder/1
o usuario 'fulano' pode responder à pergunta de id 1

ele deve mandar um json como o seguinte:
    { "usuario": "fulano",
      "resposta": "Remote Procedure Call"}
(o número da pergunta nao aparece no json porque
já está na URL)

A sua resposta deve ser armazenada no dicionario respostas

Relembrando:
respostas_iniciais = {
        'marcio':{1:'Random Person Changer'},
        'maria':{1:'Remote Procedure Call', 2: 64},
        }
é um dicionario, cada pessoa é uma chave
o valor da pessoa é um dicionário
(o valor do maria é {1:'Remote Procedure Call', 2: 64})
olhando para esse dicionario, associado a maria, temos 2
chaves, uma para cada pergunta que ela respondeu.
O valor associado a chave 1 é a resposta que maria deu
para a pergunta 1

Se o usuário ja respondeu a pergunta, devemos retornar um erro 
descritivo e o codigo 409 (confito de edição)

Se ele respondeu com uma alternativa que nao está
nem na lista de corretas nem na lista de incorretas
, devemos retornar
um erro descritivo e o codigo 400 (bad request)

Se o usuário nao está na lista de respostas, devemos adicionar
ele (podemos criar um usuário novo ao enviar uma resposta!)

Tudo isso se refere ao teste 010. Leia o teste, ele diz linha a linha o que fazer.
Lembre-se que o python te fala a linha em que o teste parou, você pode ir
aumentando esse número aos poucos

Faça também com que seja retornado um erro 404 quando a questão que
o usuário tentou responder não existe. Isso é referente ao teste 010a
'''

'''
O usuario deve poder ver quantas perguntas ainda nao
respondeu, quantas acertou e quantas errou.

Acessando a url /autoteste/<username>/resultados com o verbo GET
O usuario deve receber um json como o seguinte:

    {
    "usuario": "fulano",
    "acertos": 3,
    "erros": 2,
    "nao respondidas": 2
    }

Por exemplo, se acessarmos a url /autoteste/maria/resultados,
devemos receber

    {
    "usuario": "maria",
    "acertos": 2,
    "erros": 0,
    "nao respondidas": 0
    }


ja vimos urls como /aluno/<int:id_aluno>
Agora, estamos recebendo uma string em vez de uma id.
Para isso, é só escrever /autoteste/<nome_aluno>/resultados no app.route
                            (quando você não indica o tipo, ele 
                            automaticamente considera string)

Ao implementar essa funcionalidade, deve passar o teste 011a e 011b.

Se todas as outras URLs estiverem funcionando direito, também
passará 0 011c e o 011d. Eles dependem da funcionalidade de
o usuário responder à questao.


'''

'''
Agora, os proximos testes vao verificar mais algumas coisas
sobre as ids das questoes. 

Se você seguiu todas as instruções corretamente, os proximos testes
devem passar "de graça", e a atividade terá terminado

Se não, verifique as regras de ids. A idéia é que se a última questão tem
id 10, e inserirmos uma nova, essa nova terá id 11

-- testes 100 e 101
'''
       
import copy
respostas_iniciais = copy.deepcopy(respostas)
questoes_iniciais = copy.deepcopy(questoes)
def reseta():
    global respostas
    global questoes
    respostas = copy.deepcopy(respostas_iniciais)
    questoes = copy.deepcopy(questoes_iniciais)

reseta()

if __name__ == '__main__':
   app.url_map.strict_slashes = False
   app.run(debug=True, host='0.0.0.0',port = 5004)

