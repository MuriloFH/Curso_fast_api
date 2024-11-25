from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

# registry = registra metadados(nome de tabela, campos, tipos...) das tabelas no banco

table_register = registry()


# aqui é criado uma classe que vai representar somente uma tabela no banco
@table_register.mapped_as_dataclass
class User:
    __tablename__ = "users"  # definindo o nome da tabela

    # O Mapped[] permite dizermos qual é o tipo da coluna da tabela
    # Mapped[str] se referiria a um atributo de string que seria mapeado para uma coluna de string correspondente

    # mapped_column serve como restrições da coluna, nela podemos definir PK, FK, unique, index, nullable...

    # O init=False do mapped_column, significa que o campo não pode ser passado na construção do objeto, pois é PK

    # server_default = func.now() diz que, quando a classe for instanciada, o resultado de func.now() será o valor atribuído a esse atributo. No caso,
    #   a data e hora em que ele foi instanciado.

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now(), onupdate=func.now())
