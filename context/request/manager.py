#from abc import abstractmethod
from functools import wraps
from typing import Any, Callable, Optional
from dataclasses import dataclass
import requests
from enums.methods import Actions


@dataclass
class RequestModel:
    url_data: str = ""
    body: Any = None


class Manager:
    def __init__(self, base_url: str, token: str, url_path: Optional[str] = None):
        self.url_path = url_path
        self.base_url =  base_url.rstrip("/")
        self.token = token.strip()

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
    def _inference_method(self, method_inference: list[str]) -> Actions:

        if method_inference[:2] == ["editar", "parcialmente"]:
            return Actions.EDIT_PARTIAL

        match method_inference[0]:
            case "buscar":
                return Actions.LIST
            case "listar":
                return Actions.LIST
            case "remover":
                return Actions.DELETE
            case "editar":
                return Actions.EDIT
            case "enviar" | "criar" | "adicionar":
                return Actions.INSERT
            case _:
                raise ValueError(
                    f"Não foi possível inferir o método: {method_inference}"
                )
                
    @staticmethod
    def make_request(method: Optional[Actions] = None):
        def decorator(func: Callable[..., RequestModel]):
            @wraps(func)
            def wrapper(context, *args, **kwargs) -> Any:
                request_model = func(context, *args, **kwargs)

                manager: Manager = context._manager

                request_method = method

                if request_method is None:
                    request_method = manager._inference_method(
                        func.__name__.split("_")
                    )

                url_path = getattr(context, "_url_path", manager.url_path)
                if not url_path:
                    raise ValueError("O contexto deve definir o caminho da API.")

                url = f"{manager.base_url}/{url_path.strip('/')}"

                if request_model.url_data:
                    url = f"{url}/{request_model.url_data}"

                body = request_model.body
                to_dict = getattr(body, "to_dict", None)
                if callable(to_dict):
                    body = to_dict()

                response = requests.request(
                    method=request_method.value.action,
                    url=url,
                    headers=manager.headers,
                    json=body,
                    timeout=15,
                )

                response.raise_for_status()

                return response.json()

            return wrapper

        return decorator