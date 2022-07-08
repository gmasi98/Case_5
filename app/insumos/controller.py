from app.insumos.model import Insumos
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db


class InsumosCreate(MethodView): #/registro: rota

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
        codigo = body.get('codigo')
        data_validade = body.get('data_validade')
        preco = body.get('preco')

        # Tratamento dos dados, verificando se os dados estão corretos, se os atributos fazem sentido
        if isinstance(nome, str) and \
            isinstance(codigo, str) and \
                isinstance(data_validade, str) and \
                    isinstance(preco, str):
                        
            # buscar o obj dentro da classe
            # registrou o user no bd, este eh um obj dentro da classe user
            # insumos é igual a classe em que ele pertence.query, pegar algo da tabela, bd, uma query do bd
            # filtrar insumos, a query, pelo cpf (algo único)
            # aqui pode ser uma fonte de erro
            insumos = Insumos.query.filter_by(codigo=codigo).first() # vai pegar o primeiro cliente, nome que aparecer

            # tratar para que o insumo não se recadastre novamente, isto é, com o mesmo cdg
            # mostra que o insumo com aql id já foi cadastrado
            if insumos:
                return {'code_status': 'Dados inválidos, cliente já cadastrado'}, 400 #cdg de erro

            # criar obj, criar atributos
            insumos = Insumos(nome=nome, codigo=codigo, data_validade=data_validade, preco=preco)
            db.session.add(insumos)
            db.session.commit()
           
            # salvando obj no banco de dados
            insumos.save()
            
            # retornar uma resposta do que foi salvo, isto é, o que se encontra no json
            # 200 é o cdg que deu certo
            return insumos.json(), 200
            
        else:
            return {'code_status': 'Dados inválidos, cliente já cadastrado'}, 400 #cdg de erro
    
    # pegar no banco de dados
    def get(self):

        # pegando tds insumos do banco de dados
        insumos = Insumos.query.all()

        # retornando para o front, arq do json
        # lista de clientes, tudo contido no json, loop para pegar de cada um
        # pegando um cliente dentro de clientes 
        # verificar se eh clientes ou cliente
        return jsonify([insumos.json() for insumos in insumos])

class InsumosDetails(MethodView): #/modificar: rota para essa pág

    # função que pega um cliente específico no qual pega pelo id
    # gera um cdg de erro caso não haja o id
    def get(self, id):

        insumos = Insumos.query.get_or_404(id)

        return insumos.json()

    # pegar algo do front, atualizar atributos do obj
    # geralmente só se faz o patch, pois ele atualiza somente o atributo necessário, não todos
    def patch(self, id):

        body = request.json
        insumos = Insumos.query.get_or_404(id)

        nome = body.get('nome', insumos.nome)
        codigo = body.get('idade', insumos.codigo)
        data_validade = body.get('data_nascimento', insumos.data_validade)
        preco = body.get('cpf', insumos.preco)
        

        # Tratamento dos dados, verificando se os dados estão corretos, se os atributos fazem sentido
        # add idade, data_nascimento, login, senha, endereco
        if isinstance(nome, str) and \
            isinstance(codigo, str) and \
                isinstance(data_validade, str) and \
                    isinstance(preco, str):
                        
            
            insumos.nome = nome
            insumos.codigo = codigo
            insumos.data_validade = data_validade
            insumos.preco = preco
            
            insumos.update()

            return insumos.json(), 200

    def delete(self, id):

       insumos = Insumos.query.get_or_404(id)
       insumos.delete(insumos)

       return insumos.json()
