#verificar se cliente é com C maiúsculo ou minúsculo
from app.cliente.model import Cliente
from flask import request, jsonify
from flask.views import MethodView


class ClienteCreate(MethodView):

    # criando algo do bd, registrando numa tabela
    def post(self):

        # pegando o corpo da requisição
        body = request.json 

        # atributos associados ao módulo
        # os atributos devem estar relacionados ao cadastro
        # sendo assim deve-se considerar estes
        # os atributos que estão listados abaixo se referem aos do json
        id = body.get('id')
        nome = body.get('nome')
        cpf = body.get('cpf')
        email = body.get('email')
        telefone = body.get('telefone')
        data_consulta = body.get('data_consulta')

        # Tratamento dos dados, verificando se os dados estão corretos, se os atributos fazem sentido
        if isinstance(id, int) and \
            isinstance(nome, str) and \
                isinstance(cpf, str) and \
                    isinstance(email, str) and \
                        isinstance(telefone, str) and \
                            isinstance(data_consulta, str):

            # buscar o obj dentro da classe
            # registrou o user no bd, este eh um obj dentro da classe user
            # cliente é igual a classe em que ele pertence.query, pegar algo da tabela, bd, uma query do bd
            # filtrar o cliente, a query, pelo id (algo único)
            cliente = Cliente.query.filter_by(id=id).first() # vai pegar o primeiro cliente, nome que aparecer

            # tratar para que o user não se recadastre novamente, isto é, com o mesmo cpf
            # mostra que o cliente com aql id já foi cadastrado
            if cliente:
                return {'code_status': 'Dados inválidos, cliente já cadastrado'}, 400 #cdg de erro

            # criar obj, criar atributos
            cliente = Cliente(nome=nome, cpf=cpf, email=email, telefone=telefone, data_consulta=data_consulta)
           
            # salvando obj no banco de dados
            cliente.save()
            
            # retornar uma resposta do que foi salvo, isto é, o que se encontra no json
            # 200 é o cdg que deu certo
            return cliente.json(), 200
    
    # pegar no banco de dados
    def get(self):

        # pegando tds clientes do banco de dados
        clientes = Cliente.query.all()

        # retornando para o front, arq do json
        # lista de clientes, tudo contido no json, loop para pegar de cada um
        # pegando um cliente dentro de clientes 
        # verificar se eh clientes ou cliente
        return jsonify([cliente.json() for cliente in clientes])

class ClienteDetails(MethodView): #/registro: rota para essa pág

    # função que pega um cliente específico no qual pega pelo id
    # gera um cdg de erro caso não haja o id
    def get(self, id):

        cliente = Cliente.query.get_or_404(id)

        return cliente.json()

    # pegar algo do front, atualizar atributos do obj
    # geralmente só se faz o patch, pois ele atualiza somente o atributo necessário, não todos
    def patch(self, id):

        body = request.json
        cliente = Cliente.query.get_or_404(id)

        nome = body.get('nome', cliente.nome)
        cpf = body.get('cpf', cliente.cpf)
        email = body.get('email', cliente.email)
        telefone = body.get('telefone', cliente.telefone)
        data_consulta = body.get('data_consulta', cliente.data_consulta)

        # Tratamento dos dados, verificando se os dados estão corretos, se os atributos fazem sentido
        if isinstance(nome, str) and \
            isinstance(cpf, str) and \
                isinstance(email, str) and \
                    isinstance(telefone, str) and \
                        isinstance(data_consulta, str):
            
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.email = email
            cliente.telefone = telefone
            cliente.data_consulta = data_consulta

            cliente.update()

            return cliente.json(), 200

    def delete(self, id):

       cliente = Cliente.query.get_or_404(id)
       cliente.delete(cliente)

       return cliente.json()

