import unittest
from unittest.mock import Mock, patch

from context.request.manager import Manager
from context.table_context.atendimento import AtendimentoContext
from context.table_context.canais_de_comunicacao import (
    CanaisDeComunicacaoContext,
)
from context.table_context.cliente import ClienteContext
from context.table_context.contatos import ContatosContext
from context.table_context.departamentos import DepartamentosContext
from context.table_context.etiqueta import EtiquetaContext
from context.table_context.mensagens import MensagensContext
from context.table_context.motivos import MotivosContext
from context.table_context.notificacao import NotificacaoContext
from context.table_context.periodos import PeriodosContext
from context.table_context.templates_de_mensagem import TemplateDeMensagemContext
from context.table_context.usuario import UsuarioContext
from models.atendimento import (
    BodyList as AtendimentoBody,
    EtiquetaAtendimentoBody,
    Filter as AtendimentoFilter,
    MotivoAtendimentoBody,
    OptionsList as AtendimentoOptions,
    ObservacaoBody,
)
from models.canais_de_comunicacao import (
    BodyList as CanaisBody,
    Filter as CanaisFilter,
)
from models.cliente import (
    BodyList as ClienteBody,
    ClienteBody as ClientePayload,
    ClientePatchBody,
    Filter as ClienteFilter,
)
from models.contatos import (
    BodyList as ContatosBody,
    ContatoBody,
    Filter as ContatosFilter,
)
from models.departamentos import (
    BodyList as DepartamentosBody,
    DepartamentoBody,
    Filter as DepartamentosFilter,
)
from models.etiqueta import (
    BodyList as EtiquetaBody,
    CriarEtiquetaBody,
    Filter as EtiquetaFilter,
)
from models.mensagens import (
    BodyList as MensagensBody,
    Filter as MensagensFilter,
    MensagemEmAndamentoBody,
)
from models.motivos import (
    BodyList as MotivosBody,
    Filter as MotivosFilter,
)
from models.notificacao import NotificacaoBody
from models.periodos import (
    BodyList as PeriodosBody,
    Filter as PeriodosFilter,
)
from models.templates_de_mensagem import (
    BodyList as TemplatesBody,
    EnvioTemplateBody,
    Filter as TemplatesFilter,
)
from models.usuario import (
    BodyList as UsuarioBody,
    Filter as UsuarioFilter,
)


class TableContextGetTests(unittest.TestCase):
    base_url = "https://api.example.test/api/v1"
    response_body = {"status": "success", "data": []}

    def setUp(self) -> None:
        self.manager = Manager(self.base_url, "test-token")
        self.contexts = {
            "atendimento": AtendimentoContext(self.manager),
            "mensagens": MensagensContext(self.manager),
            "canais": CanaisDeComunicacaoContext(self.manager),
            "templates": TemplateDeMensagemContext(self.manager),
            "cliente": ClienteContext(self.manager),
            "usuario": UsuarioContext(self.manager),
            "contatos": ContatosContext(self.manager),
            "etiqueta": EtiquetaContext(self.manager),
            "departamentos": DepartamentosContext(self.manager),
            "motivos": MotivosContext(self.manager),
            "periodos": PeriodosContext(self.manager),
            "notificacao": NotificacaoContext(self.manager),
        }

        self.response = Mock()
        self.response.json.return_value = self.response_body
        self.request_patcher = patch(
            "context.request.manager.requests.request",
            return_value=self.response,
        )
        self.request = self.request_patcher.start()
        self.addCleanup(self.request_patcher.stop)

    def assert_api_request(
        self,
        call,
        method: str,
        path: str,
        body=None,
    ) -> None:
        self.request.reset_mock()
        self.response.raise_for_status.reset_mock()

        self.assertEqual(call(), self.response_body)
        self.request.assert_called_once_with(
            method=method,
            url=f"{self.base_url}/{path}",
            headers=self.manager.headers,
            json=body,
            timeout=15,
        )
        self.response.raise_for_status.assert_called_once_with()

    def assert_get_request(self, call, path: str, body=None) -> None:
        self.assert_api_request(call, "GET", path, body)

    def test_atendimento_get_endpoints(self) -> None:
        context = self.contexts["atendimento"]
        self.assert_get_request(
            lambda: context.buscar_atendimento_populado("at-1"),
            "atendimento/at-1",
        )
        self.assert_get_request(
            lambda: context.listar_atendimentos(
                AtendimentoBody(
                    filter=AtendimentoFilter(
                        id_atendente="user-1",
                        canal_id="channel-1",
                        id_cliente="client-1",
                        motivos_idMotivo="reason-1",
                        evaluations_ai_rating="5",
                    ),
                    options=AtendimentoOptions(skip=10, limit=20),
                )
            ),
            "atendimento",
            {
                "filter": {
                    "id_atendente": "user-1",
                    "canal_id": "channel-1",
                    "id_cliente": "client-1",
                    "motivos.idMotivo": "reason-1",
                    "evaluations.ai.rating": "5",
                },
                "options": {"skip": 10, "limit": 20},
            },
        )

    def test_mensagens_get_endpoints(self) -> None:
        context = self.contexts["mensagens"]
        self.assert_get_request(
            lambda: context.listar_mensagens_atendimento(
                MensagensBody(filter=MensagensFilter(id_rota="route-1"))
            ),
            "atendimento/mensagem",
            {"filter": {"id_rota": "route-1"}},
        )
        self.assert_get_request(
            lambda: context.buscar_mensagem_atendimento_pupulada("message-1"),
            "atendimento/mensagem/message-1",
        )

    def test_canais_get_endpoints(self) -> None:
        context = self.contexts["canais"]
        self.assert_get_request(
            lambda: context.listar_canais_de_comunicacao(
                CanaisBody(filter=CanaisFilter(id_atendente="user-1"))
            ),
            "canal-comunicacao",
            {"filter": {"id_atendente": "user-1"}},
        )
        self.assert_get_request(
            lambda: context.buscar_canal_de_comunicacao_populado("channel-1"),
            "canal-comunicacao/channel-1",
        )
        self.assert_get_request(
            lambda: context.buscar_os_templates_de_mensagem_por_canal("channel-1"),
            "canal-comunicacao/channel-1/template",
        )
        self.assert_get_request(
            lambda: context.buscar_limites_diarios_de_envio_de_templates_de_mensagem(
                "channel-1"
            ),
            "canal-comunicacao/channel-1/template/limites-diarios-envio",
        )

    def test_templates_get_endpoints(self) -> None:
        context = self.contexts["templates"]
        self.assert_get_request(
            lambda: context.listar_templates(
                TemplatesBody(
                    filter=TemplatesFilter(tipo_mensagem="dialog360")
                )
            ),
            "template",
            {"filter": {"tipo_mensagem": "dialog360"}},
        )
        self.assert_get_request(
            lambda: context.buscar_template_populado("template-1"),
            "template/template-1",
        )

    def test_cliente_get_endpoints(self) -> None:
        context = self.contexts["cliente"]
        self.assert_get_request(
            lambda: context.listar_clientes(
                ClienteBody(
                    filter=ClienteFilter(
                        id_fornecedor="supplier-1",
                        cpf_cnpj="123",
                        cliente=True,
                    )
                )
            ),
            "cliente",
            {
                "filter": {
                    "id_fornecedor": "supplier-1",
                    "cpf_cnpj": "123",
                    "cliente": True,
                }
            },
        )
        self.assert_get_request(
            lambda: context.buscar_cliente_populado("client-1"),
            "cliente/client-1",
        )

    def test_usuario_list_uses_no_body_when_omitted(self) -> None:
        context = self.contexts["usuario"]
        self.assert_get_request(
            lambda: context.listar_usuarios(),
            "usuario",
        )
        self.assert_get_request(
            lambda: context.listar_usuarios(
                UsuarioBody(filter=UsuarioFilter(status="A", tipo="user"))
            ),
            "usuario",
            {"filter": {"status": "A", "tipo": "user"}},
        )

    def test_contatos_get_endpoints(self) -> None:
        context = self.contexts["contatos"]
        self.assert_get_request(
            lambda: context.listar_contatos(
                ContatosBody(
                    filter=ContatosFilter(
                        email_principal="user@example.test",
                        fones_numero="+5511999999999",
                    )
                )
            ),
            "contato",
            {
                "filter": {
                    "email_principal": "user@example.test",
                    "fones.numero": "+5511999999999",
                }
            },
        )
        self.assert_get_request(
            lambda: context.buscar_contato_populado("contact-1"),
            "contato/contact-1",
        )

    def test_etiqueta_list_endpoint(self) -> None:
        context = self.contexts["etiqueta"]
        self.assert_get_request(
            lambda: context.listar_etiquetas(
                EtiquetaBody(filter=EtiquetaFilter(id_criador="user-1"))
            ),
            "etiqueta",
            {"filter": {"id_criador": "user-1"}},
        )

    def test_departamentos_get_endpoints(self) -> None:
        context = self.contexts["departamentos"]
        self.assert_get_request(
            lambda: context.listar_departamentos(
                DepartamentosBody(
                    filter=DepartamentosFilter(
                        cod_pabx="123",
                        realizaAtendimento=True,
                    )
                )
            ),
            "departamento",
            {
                "filter": {
                    "cod_pabx": "123",
                    "realizaAtendimento": True,
                }
            },
        )
        self.assert_get_request(
            lambda: context.buscar_departamento_populado("department-1"),
            "departamento/department-1",
        )

    def test_motivos_get_endpoints(self) -> None:
        context = self.contexts["motivos"]
        self.assert_get_request(
            lambda: context.listar_motivos(
                MotivosBody(filter=MotivosFilter(departamentos="department-1"))
            ),
            "motivo",
            {"filter": {"departamentos": "department-1"}},
        )
        self.assert_get_request(
            lambda: context.buscar_motivo("reason-1"),
            "motivo/reason-1",
        )

    def test_periodos_get_endpoints(self) -> None:
        context = self.contexts["periodos"]
        self.assert_get_request(
            lambda: context.listar_periodos(
                PeriodosBody(
                    filter=PeriodosFilter(segunda=True, feriado=False),
                )
            ),
            "atendimento/periodo",
            {"filter": {"segunda": True, "feriado": False}},
        )
        self.assert_get_request(
            lambda: context.buscar_periodo("period-1"),
            "atendimento/periodo/period-1",
        )

    def test_contexts_share_manager_without_overwriting_routes(self) -> None:
        self.assert_get_request(
            lambda: self.contexts["atendimento"].buscar_atendimento_populado("at-1"),
            "atendimento/at-1",
        )
        self.assert_get_request(
            lambda: self.contexts["mensagens"].buscar_mensagem_atendimento_pupulada(
                "message-1"
            ),
            "atendimento/mensagem/message-1",
        )
        self.assertIsNone(self.manager.url_path)

    def test_atendimento_write_endpoints(self) -> None:
        atendimento = self.contexts["atendimento"]
        self.assert_api_request(
            lambda: atendimento.criar_observacao(
                "at-1", ObservacaoBody(message="note")
            ),
            "POST",
            "atendimento/at-1/observacao",
            {"message": "note"},
        )
        self.assert_api_request(
            lambda: atendimento.adicionar_etiqueta(
                "at-1", EtiquetaAtendimentoBody(tag_id="tag-1")
            ),
            "POST",
            "atendimento/at-1/etiqueta",
            {"tagId": "tag-1"},
        )
        self.assert_api_request(
            lambda: atendimento.adicionar_motivo(
                "at-1", MotivoAtendimentoBody(reason_id="reason-1")
            ),
            "POST",
            "atendimento/at-1/motivo",
            {"reasonId": "reason-1"},
        )
        self.assert_api_request(
            lambda: atendimento.remover_etiqueta("at-1", "tag-1"),
            "DELETE",
            "atendimento/at-1/etiqueta/tag-1",
        )

    def test_message_and_template_send_endpoints(self) -> None:
        self.assert_api_request(
            lambda: self.contexts["mensagens"].enviar_mensagem_em_atendimento_em_andamento(
                MensagemEmAndamentoBody(
                    customer_service_id="service-1",
                    content={"type": "text", "text": "Hello"},
                )
            ),
            "POST",
            "atendimento/mensagem/send",
            {
                "customerServiceId": "service-1",
                "content": {"type": "text", "text": "Hello"},
            },
        )
        self.assert_api_request(
            lambda: self.contexts["templates"].enviar_template(
                EnvioTemplateBody(
                    contato={"canalCliente": "+5511999999999"},
                    template={
                        "_id": "template-1",
                        "variaveis": ["first", "second"],
                    },
                    canal="channel-1",
                )
            ),
            "POST",
            "template/send",
            {
                "contato": {"canalCliente": "+5511999999999"},
                "template": {
                    "_id": "template-1",
                    "variaveis": ["first", "second"],
                },
                "canal": "channel-1",
            },
        )

    def test_cliente_write_endpoints_and_patch_validation(self) -> None:
        cliente = self.contexts["cliente"]
        body = ClientePayload(
            nome="Arnold Schwarzenegger",
            status="A",
            prospect=False,
            cliente=True,
            fornecedor=False,
            prestador_servico=False,
            cpf_cnpj="640.642.910-93",
            tags=["tag-1"],
        )
        payload = {
            "nome": "Arnold Schwarzenegger",
            "status": "A",
            "prospect": False,
            "cliente": True,
            "fornecedor": False,
            "prestadorServico": False,
            "cpf_cnpj": "640.642.910-93",
            "tags": ["tag-1"],
        }
        self.assert_api_request(
            lambda: cliente.criar_cliente(body),
            "POST",
            "cliente",
            payload,
        )
        self.assert_api_request(
            lambda: cliente.editar_cliente("client-1", body),
            "PUT",
            "cliente/client-1",
            payload,
        )
        self.assert_api_request(
            lambda: cliente.editar_parcialmente_cliente(
                "client-1", ClientePatchBody(prospect=False)
            ),
            "PATCH",
            "cliente/client-1",
            {"prospect": False},
        )
        self.assert_api_request(
            lambda: cliente.remover_cliente("client-1"),
            "DELETE",
            "cliente/client-1",
        )
        self.request.reset_mock()
        with self.assertRaisesRegex(ValueError, "ao menos um campo"):
            ClientePatchBody()
        self.request.assert_not_called()

    def test_contato_write_endpoints(self) -> None:
        contatos = self.contexts["contatos"]
        common = {
            "nome": "Arnold Schwarzenegger",
            "requerAutenticacaoSempre": True,
            "habilitarAlerta": True,
            "lead": False,
            "historico_email": True,
        }
        create_body = ContatoBody(
            nome="Arnold Schwarzenegger",
            requer_autenticacao_sempre=True,
            habilitar_alerta=True,
            lead=False,
            historico_email=True,
            celular_completo="+5549988776655",
            senha="secret",
            repetir_senha="secret",
        )
        self.assert_api_request(
            lambda: contatos.criar_contato(create_body),
            "POST",
            "contato",
            {
                **common,
                "celularCompleto": "+5549988776655",
                "senha": "secret",
                "repetirSenha": "secret",
            },
        )
        update_body = ContatoBody(
            nome="Arnold Schwarzenegger",
            requer_autenticacao_sempre=True,
            habilitar_alerta=True,
            lead=False,
            historico_email=True,
            celular_completo="+5549988776655",
        )
        self.assert_api_request(
            lambda: contatos.editar_contato("contact-1", update_body),
            "PUT",
            "contato/contact-1",
            {**common, "celularCompleto": "+5549988776655"},
        )
        self.assert_api_request(
            lambda: contatos.remover_contato("contact-1"),
            "DELETE",
            "contato/contact-1",
        )
        self.request.reset_mock()
        with self.assertRaisesRegex(ValueError, "senha e repetir_senha"):
            contatos.criar_contato(update_body)
        self.request.assert_not_called()

    def test_tag_notification_and_department_write_endpoints(self) -> None:
        self.assert_api_request(
            lambda: self.contexts["etiqueta"].criar_etiqueta(
                CriarEtiquetaBody(nome="Urgente", cor="blue", tipo="empresa")
            ),
            "POST",
            "etiqueta",
            {"nome": "Urgente", "cor": "blue", "tipo": "empresa"},
        )
        self.assert_api_request(
            lambda: self.contexts["notificacao"].enviar_notificacao(
                NotificacaoBody(
                    type="news",
                    title="Title",
                    description="Description",
                    users=["user-1"],
                    link="https://example.test",
                )
            ),
            "POST",
            "notificacao/send",
            {
                "type": "news",
                "title": "Title",
                "description": "Description",
                "users": ["user-1"],
                "link": "https://example.test",
            },
        )
        self.assert_api_request(
            lambda: self.contexts["departamentos"].criar_departamento(
                DepartamentoBody(
                    nome="Teste API",
                    status="A",
                    tipo_encaminhamento_ligacoes="S",
                )
            ),
            "POST",
            "departamento",
            {
                "nome": "Teste API",
                "status": "A",
                "tipoEncaminhamentoLigacoes": "S",
            },
        )
        self.assert_api_request(
            lambda: self.contexts["departamentos"].editar_departamento(
                "department-1",
                DepartamentoBody(
                    nome="Departamento",
                    status="I",
                    tipo_encaminhamento_ligacoes="S",
                    cod_pabx="332",
                ),
            ),
            "PUT",
            "departamento/department-1",
            {
                "nome": "Departamento",
                "status": "I",
                "tipoEncaminhamentoLigacoes": "S",
                "cod_pabx": "332",
            },
        )



if __name__ == "__main__":
    unittest.main()
