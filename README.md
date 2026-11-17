# Atendimentos Projeto

Cliente Python para a API Opa Suite. Os contextos em `context/table_context`
agrupam os endpoints por recurso e usam `Manager` para autenticação e envio das
requisições.

## Requisitos

- Python 3.11 ou superior
- Uma URL base da API Opa Suite e um token de usuário com perfil de permissões
  do tipo API

## Instalação

No PowerShell, na pasta do projeto:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install requests python-dotenv
```

Configure as variáveis de ambiente em um arquivo `.env` na raiz:

```dotenv
OPA_API_URL=https://seu-dominio.com.br/api/v1
OPA_API_TOKEN=seu-token
```

Não compartilhe nem versione o arquivo `.env`.

## Exemplo de uso

Os contextos usam a URL base e o token fornecidos ao `Manager`. O caminho do
recurso é definido pelo contexto; não é necessário criar um `Manager` diferente
para cada recurso.

```python
import os

from dotenv import load_dotenv

from context.request.manager import Manager
from context.table_context.atendimento import AtendimentoContext
from models.atendimento import BodyList, Filter, OptionsList

load_dotenv()

manager = Manager(
    base_url=os.environ["OPA_API_URL"],
    token=os.environ["OPA_API_TOKEN"],
)
atendimento = AtendimentoContext(manager)

resultado = atendimento.listar_atendimentos(
    BodyList(
        filter=Filter(protocolo="OPA202210"),
        options=OptionsList(limit=100),
    )
)
print(resultado)
```

Para buscar um atendimento por ID:

```python
resultado = atendimento.buscar_atendimento_populado("ID_DO_ATENDIMENTO")
```

As respostas dos métodos implementados são os dados JSON retornados pela API.
Nos métodos de listagem, o corpo é opcional. Quando passado como modelo, ele é
convertido automaticamente para dicionário antes do envio; campos com valor
`None` são omitidos.

## Contextos disponíveis

Os contextos estão em `context/table_context`:

- `atendimento`
- `mensagens`
- `canais_de_comunicacao`
- `templates_de_mensagem`
- `cliente`
- `contatos`
- `usuario`
- `etiqueta`
- `departamentos`
- `motivos`
- `periodos`
- `notificacao`

As rotas `GET`, `POST`, `PUT`, `PATCH` e `DELETE` documentadas estão
implementadas. Os payloads de escrita são modelos com `to_dict`, convertidos
automaticamente pelo `Manager` antes do envio; campos opcionais com valor
`None` são omitidos. O modelo `ClientePatchBody` exige ao menos um campo não
nulo, e a criação de contatos exige `senha` e `repetir_senha`. Os modelos ficam
na pasta `models`; métodos `enviar_*` recebem automaticamente o sufixo `/send`
na URL pelo `Manager`.

## Testes

Execute os testes unitários a partir da raiz do projeto:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Os testes simulam as chamadas HTTP; não precisam de token nem acessam a API.

## Documentação da API

Consulte a [documentação oficial da API Opa Suite](https://api.opasuite.com.br/).
