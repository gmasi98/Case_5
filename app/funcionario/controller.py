#verificar se cliente é com C maiúsculo ou minúsculo
from app.funcionario.model import Funcionario
import bcrypt
from flask_jwt_extended import create_access_token
from flask import render_template, request, jsonify
from flask.views import MethodView
from app.extensions import db,mail
# enviar email de confirmação
from flask_mail import Message



class FuncionarioCreate(MethodView): #/registro: rota

    # criando algo do bd, registrando numa tabela
    # adiciona no sistema um funcionario
    def post(self):

        # pegando o corpo da requisição
        body = request.json 

        # atributos associados ao módulo
        # os atributos devem estar relacionados ao cadastro
        # sendo assim deve-se considerar estes
        # os atributos que estão listados abaixo se referem aos do json

        id = body.get('id')
        nome = body.get('nome')
        idade = body.get('idade') 
        data_nascimento = body.get('data_nascimento')
        cpf = body.get('cpf')
        telefone = body.get('telefone')
        endereco = body.get('endereco')
        email = body.get('email')
        senha = body.get('senha')
        # pega a senha que veio como string, add salt e faz um hash da senha
        # pra fazer um hash a senha deve estar em binario
        # senha.encode, passa a senha de string paara binario
        # decode transforma de bin para string
        senha = bcrypt.hashpw(senha.encode(),bcrypt.gensalt()).decode()


        # Tratamento dos dados, verificando se os dados estão corretos, se os atributos fazem sentido
        # add idade, data_nascimento, login, senha, endereco
        if isinstance(nome, str) and \
            isinstance(idade, str) and \
                isinstance(data_nascimento, str) and \
                    isinstance(endereco, str) and \
                        isinstance(cpf, str) and \
                            isinstance(email, str) and \
                                isinstance(senha, str) and \
                                    isinstance(telefone, str):

            # buscar o obj dentro da classe
            # registrou o user no bd, este eh um obj dentro da classe user
            # funcionario é igual a classe em que ele pertence.query, pegar algo da tabela, bd, uma query do bd
            # filtrar o funcionario, a query, pelo cpf (algo único)
            # aqui pode ser uma fonte de erro
            funcionario = Funcionario.query.filter_by(cpf=cpf).first() # vai pegar o primeiro funcioanrio, nome que aparecer

            # tratar para que o funcionario não se recadastre novamente, isto é, com o mesmo cpf
            # mostra que o cliente com aql id já foi cadastrado
            if funcionario:
                return {'code_status': 'Dados inválidos, funcionario já cadastrado'}, 400 #cdg de erro

            # criar obj, criar atributos
            funcionario = Funcionario(nome=nome, idade = idade, data_nascimento = data_nascimento, endereco = endereco, cpf=cpf, email=email, senha = senha, telefone=telefone)

            db.session.add(funcionario)
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
            funcionario.save()
            
            # retornar uma resposta do que foi salvo, isto é, o que se encontra no json
            # 200 é o cdg que deu certo
            return funcionario.json(), 200
            
        else:
            return {'code_status': 'Dados inválidos, cliente já cadastrado'}, 400 #cdg de erro
    
    # pegar no banco de dados
    def get(self):

        # pegando tds funcionarios do banco de dados
        funcionarios = Funcionario.query.all()

        # retornando para o front, arq do json
        # lista de funcionarios, tudo contido no json, loop para pegar de cada um
        # pegando um dono dentro de clientes 
        return jsonify([funcionario.json() for funcionario in funcionarios])

class FuncionarioDetails(MethodView): #/modificar: rota para essa pág

    # função que pega um funcionario específico no qual pega pelo id
    # gera um cdg de erro caso não haja o id
    def get(self, id):

        funcionario = Funcionario.query.get_or_404(id)

        return funcionario.json()

    # pegar algo do front, atualizar atributos do obj
    # geralmente só se faz o patch, pois ele atualiza somente o atributo necessário, não todos
    def patch(self, id):

        body = request.json
        funcionario = Funcionario.query.get_or_404(id)

        nome = body.get('nome', funcionario.nome)
        idade = body.get('idade', funcionario.idade)
        data_nascimento = body.get('data_nascimento', funcionario.data_nascimento)
        cpf = body.get('cpf', funcionario.cpf)
        email = body.get('email', funcionario.email)
        senha = body.get('senha', funcionario.senha)
        telefone = body.get('telefone', funcionario.telefone)
        endereco = body.get('endereco', funcionario.endereco)
        

        # Tratamento dos dados, verificando se os dados estão corretos, se os atributos fazem sentido
        # add idade, data_nascimento, login, senha, endereco
        if isinstance(nome, str) and \
            isinstance(idade, str) and \
                isinstance(data_nascimento, str) and \
                    isinstance(endereco, str) and \
                        isinstance(cpf, str) and \
                            isinstance(email, str) and \
                                isinstance(senha, str) and \
                                    isinstance(telefone, str):
            
            funcionario.nome = nome
            funcionario.idade = idade
            funcionario.data_nascimento = data_nascimento
            funcionario.endereco = endereco
            funcionario.cpf = cpf
            funcionario.email = email
            funcionario.senha = senha
            funcionario.telefone = telefone

            funcionario.update()

            return funcionario.json(), 200

    def delete(self, id):

       funcionario = Funcionario.query.get_or_404(id)
       funcionario.delete(funcionario)

       return funcionario.json()

class Login(MethodView):
    def post(self):

        body = request.json
        nome = body.get('nome')
        idade = body.get('idade')
        data_nascimento = body.get('data_nascimento')
        cpf = body.get('cpf')
        email = body.get('email')
        senha = body.get('senha')
        telefone = body.get('telefone')
        endereco = body.get('endereco')
       

        funcionario.nome = nome
        funcionario.idade = idade
        funcionario.data_nascimento = data_nascimento
        funcionario.endereco = endereco
        funcionario.cpf = cpf
        funcionario.email = email
        funcionario.senha = senha
        funcionario.telefone = telefone
    

        funcionario = Funcionario.query.filter_by(cpf=cpf).first()

        if funcionario and bcrypt.checkpw(senha.encode(),funcionario.senha.encode()):
            return {'token':create_access_token(funcionario.id,additional_claims={"funcionario":"logado"})}
        return {"msg":"não existe esse funcionario"}, 400

