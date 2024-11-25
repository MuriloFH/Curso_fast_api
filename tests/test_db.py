from sqlalchemy import select

from curso_fast_api.Models.models import User


def test_db_create_user(session):
    # depois com base no model, ele cria um objeto de teste
    newUser = User(username="Murilouco", email="murilouco@gmail.com", password="coxinhadataaniversario")

    session.add(newUser)  # aqui eu falo para a sessão que eu quero criar um novo user
    session.commit()

    # fazendo o objeto encontrar o objeto criado diretamente no banco

    # .scalar ele pega o primeiro resultado da busca e faz uma operação de converter o resultado do banco de dados
    #   em um Objeto criado pelo SQLAlchemy, nesse caso, caso encontre um resultado, ele irá converter na classe User
    find_user = session.scalar(select(User).where(User.username == "Murilouco"))

    assert find_user.username == "Murilouco"
