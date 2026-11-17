from dotenv import load_dotenv
import os
import json

from context.request.manager import Manager
from context.table_context.atendimento import AtendimentoContext, BodyList, Filter, OptionsList
load_dotenv()
        
manager = Manager(
    os.getenv("OPA_API_URL"),
    os.getenv("OPA_API_TOKEN")
)
client = AtendimentoContext(manager)
response = json.dumps(client.buscar_atendimento_populado(
    BodyList(filter=Filter(), options=OptionsList(limit=2))
))

with open("test.json", "w") as file:
    file.write(response)
