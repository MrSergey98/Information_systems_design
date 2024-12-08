from abc import ABC, abstractmethod
from http.server import BaseHTTPRequestHandler

from firma.ClientRepFile import ClientRepFile
from firma.ClientRepFileAdapter import ClientRepFileAdapter
from firma.ClientRepJson import ClientRepJson


class BasicController(ABC):

    def __init__(self):
        self.repository = ClientRepFileAdapter(ClientRepFile(ClientRepJson))

    @abstractmethod
    def get_web_view(self, **kwargs):
        pass

    @abstractmethod
    def get_app_view(self, **kwargs):
        pass