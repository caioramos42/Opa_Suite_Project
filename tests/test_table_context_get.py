import unittest
from unittest.mock import Mock, patch

from context.request.manager import Manager
from context.table_context.atendimento import (
    AtendimentoContext,
    BodyList as AtendimentoBody,
    Filter as AtendimentoFilter,
    OptionsList as AtendimentoOptions,
)
from context.table_context.canais_de_comunicacao import (
    BodyList as CanaisBody,
    CanaisDeComunicacaoContext,
    Filter as CanaisFilter,
)
from context.table_context.cliente import (
    BodyList as ClienteBody,
    ClienteContext,
    Filter as ClienteFilter,
)
from context.table_context.contatos import (
    BodyList as ContatosBody,
    ContatosContext,
    Filter as ContatosFilter,
)
from context.table_context.departamentos import (
    BodyList as DepartamentosBody,
    DepartamentosContext,
    Filter as DepartamentosFilter,
)
from context.table_context.etiqueta import (
    BodyList as EtiquetaBody,
    EtiquetaContext,
    Filter as EtiquetaFilter,
)
from context.table_context.mensagens import (
    BodyList as MensagensBody,
    Filter as MensagensFilter,
    MensagensContext,
)
from context.table_context.motivos import (
    BodyList as MotivosBody,
    Filter as MotivosFilter,
    MotivosContext,
)
from context.table_context.notificacao import NotificacaoContext
from context.table_context.periodos import (
    BodyList as PeriodosBody,
    Filter as PeriodosFilter,
    PeriodosContext,
)
from context.table_context.templates_de_mensagem import (
    BodyList as TemplatesBody,
    Filter as TemplatesFilter,
    TemplateDeMensagemContext,
)
from context.table_context.usuario import (
    BodyList as UsuarioBody,
    Filter as UsuarioFilter,
    UsuarioContext,
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

    def assert_get_request(
        self,
        call,
        path: str,
        body=None,
    ) -> None:
        self.request.reset_mock()

        self.assertEqual(call(), self.response_body)
        self.request.assert_called_once_with(
            method="GET",
            url=f"{self.base_url}/{path}",
            headers=self.manager.headers,
            json=body,
            timeout=15,
        )
        self.response.raise_for_status.assert_called()

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

    def test_non_get_routes_are_explicitly_unimplemented(self) -> None:
        atendimento = self.contexts["atendimento"]
        cliente = self.contexts["cliente"]
        contatos = self.contexts["contatos"]
        departamentos = self.contexts["departamentos"]
        etiqueta = self.contexts["etiqueta"]
        mensagens = self.contexts["mensagens"]
        templates = self.contexts["templates"]
        notificacao = self.contexts["notificacao"]

        calls = (
            ("criar observação", lambda: atendimento.criar_observacao("at-1", "note")),
            ("adicionar etiqueta", lambda: atendimento.adicionar_etiqueta("at-1", "tag-1")),
            ("adicionar motivo", lambda: atendimento.adicionar_motivo("at-1", "reason-1")),
            ("remover etiqueta", lambda: atendimento.remover_etiqueta("at-1", "tag-1")),
            ("enviar mensagem", lambda: mensagens.enviar_mensagem_em_atendimento_em_andamento({})),
            ("enviar template", lambda: templates.enviar_template({})),
            ("criar cliente", lambda: cliente.criar_cliente({})),
            ("editar cliente", lambda: cliente.editar_cliente("client-1", {})),
            ("editar parcialmente cliente", lambda: cliente.editar_parcialmente_cliente("client-1", {})),
            ("remover cliente", lambda: cliente.remover_cliente("client-1")),
            ("criar contato", lambda: contatos.criar_contato({})),
            ("editar contato", lambda: contatos.editar_contato("contact-1", {})),
            ("remover contato", lambda: contatos.remover_contato("contact-1")),
            ("criar etiqueta", lambda: etiqueta.criar_etiqueta({})),
            ("enviar notificação", lambda: notificacao.enviar_notificacao({})),
            ("criar departamento", lambda: departamentos.criar_departamento({})),
            ("editar departamento", lambda: departamentos.editar_departamento("department-1", {})),
        )

        for route_name, call in calls:
            with self.subTest(route=route_name):
                with self.assertRaises(NotImplementedError):
                    call()

        self.request.assert_not_called()


if __name__ == "__main__":
    unittest.main()
