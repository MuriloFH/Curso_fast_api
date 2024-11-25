import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from curso_fast_api.app import app
from curso_fast_api.Models.models import table_register


@pytest.fixture
def client():  # criando o client, aonde ele vai procurar os endpoints passados nos testes
    return TestClient(app=app)  # Arrange(organização)


@pytest.fixture
def session():
    # criando uma engine do db
    engine = create_engine("sqlite:///:memory:")

    # aqui eu to dizendo que o table_register criado no meu model deve criar todas as tabelas a partir dos models
    #   que tem a anotação @table_register.mapped_as_dataclass usando a engine criada
    table_register.metadata.create_all(engine)

    with Session(engine) as session:  # criando uma sessão com base na engine criada
        yield session
        # yield session: fornece uma instância de Session que será injetada em cada teste que solicita a fixture session.
        #     Essa sessão será usada para interagir com o banco de dados de teste.

    table_register.metadata.drop_all(engine)
    # quando os testes acabarem, ele destroi o banco em momoria
    #    usado em todos os testes que herdam essa classe ou fixture
