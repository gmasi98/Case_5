#verificar se cliente é com C maiúsculo ou minúsculo
from app.dono.model import Dono
import bcrypt
from flask_jwt_extended import create_access_token
from flask import render_template, request, jsonify
from flask.views import MethodView
from app.extensions import db,mail
# enviar email de confirmação
from flask_mail import Message



class DonoCreate(MethodView): #/registro: rota

    # criando algo do bd, registrando numa tabela
    # adiciona no sistema um dono
    def post(self):

        # pegando o corpo da requisição
        body = request.json 

        # atributos associados ao módulo
        # os atributos devem estar relacionados ao cadastro
        # sendo assim deve-se considerar estes
        # os atributos que estão listados abaixo se referem aos do json

        id = body.get('id')
        nome = body.get('nome')
        email = body.get('email')
        senha = body.get('senha')
        # pega a senha que veio como string, add salt e faz um hash da senha
        # pra fazer um hash a senha deve estar em binario
        # senha.encode, passa a senha de string paara binario
        # decode transforma de bin para string
        senha = bcrypt.hashpw(senha.encode(),bcrypt.gensalt()).decode()
        telefone = body.get('telefone')
        
        # Tratamento dos dados, verificando se os dados estão corretos, se os atributos fazem sentido
        if isinstance(nome, str) and \
            isinstance(email, str) and \
                isinstance(senha, str) and \
                    isinstance(telefone, str):

            # buscar o obj dentro da classe
            # registrou o user no bd, este eh um obj dentro da classe user
            # dono é igual a classe em que ele pertence.query, pegar algo da tabela, bd, uma query do bd
            # filtrar o dono, a query, pelo cpf (algo único)
            # aqui pode ser uma fonte de erro
            dono = Dono.query.filter_by(nome=nome).first() # vai pegar o primeiro cliente, nome que aparecer

            # tratar para que o dono não se recadastre novamente, isto é, com o mesmo cpf
            # mostra que o cliente com aql id já foi cadastrado
            if dono:
                return {'code_status': 'Dados inválidos, dono já cadastrado'}, 400 #cdg de erro

            # criar obj, criar atributos
            dono = Dono(nome=nome, email=email, senha = senha, telefone=telefone)

            db.session.add(dono)
            db.session.commit()
            # o arq html eh o corpo do email, e o render_template vai carregar isso

            # envio de confirmação do email
            # aplicação sendgrid, pode ser uma possível fonte de erros, 
            # não consegui utilizar a plataforma por falta de autorização por parte da mesma
            # assim não consegui pegar alguns atributos essenciais para o correto funcionamento do código
            msg = Message(sender = 'gabrielmarinhobom@poli.ufrj.br',
            recipients=[email], subject = "Cadastro Realizado com sucesso!",
            html = render_template('email.html', nome=nome))
            # envia a mensagem de confirmação
            mail.send(msg)
           
            # salvando obj no banco de dados
            dono.save()
            
            # retornar uma resposta do que foi salvo, isto é, o que se encontra no json
            # 200 é o cdg que deu certo
            return dono.json(), 200
            
        else:
            return {'code_status': 'Dados inválidos, cliente já cadastrado'}, 400 #cdg de erro
    
    # pegar no banco de dados
    def get(self):

        # pegando tds donos do banco de dados
        donos = Dono.query.all()

        # retornando para o front, arq do json
        # lista de clientes, tudo contido no json, loop para pegar de cada um
        # pegando um cliente dentro de clientes 
        # verificar se eh clientes ou cliente
        return jsonify([dono.json() for dono in donos])

class DonoDetails(MethodView): #/modificar: rota para essa pág

    # função que pega um dono específico no qual pega pelo id
    # gera um cdg de erro caso não haja o id
    def get(self, id):

        dono = Dono.query.get_or_404(id)

        return dono.json()

    # pegar algo do front, atualizar atributos do obj
    # geralmente só se faz o patch, pois ele atualiza somente o atributo necessário, não todos
    def patch(self, id):

        body = request.json
        dono = Dono.query.get_or_404(id)

        nome = body.get('nome', dono.nome)
        email = body.get('email', dono.email)
        senha = body.get('senha', dono.senha)
        telefone = body.get('telefone', dono.telefone)

        # Tratamento dos dados, verificando se os dados estão corretos, se os atributos fazem sentido
        if isinstance(nome, str) and \
            isinstance(email, str) and \
                isinstance(senha, str) and \
                    isinstance(telefone, str):
            
            dono.nome = nome
            dono.email = email
            dono.senha = senha
            dono.telefone = telefone
            dono.update()

            return dono.json(), 200

    def delete(self, id):

       dono = Dono.query.get_or_404(id)
       Dono.delete(dono)

       return dono.json()

class Login(MethodView):
    def post(self):

        body = request.json
        nome = body.get('nome')
        email = body.get('email')
        senha = body.get('senha')
        telefone = body.get('telefone')

        dono.nome = nome
        dono.email = email
        dono.senha = senha
        dono.telefone = telefone
        

        dono = Dono.query.filter_by(nome=nome).first()

        if dono and bcrypt.checkpw(senha.encode(),dono.senha.encode()):
            return {'token':create_access_token(dono.id,additional_claims={"dono":"logado"})}
        return {"msg":"não existe esse dono"}, 400

