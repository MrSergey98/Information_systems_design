from abc import ABC, abstractmethod

from firma.ClientRepFile import ClientRepFile
from firma.ClientRepFileAdapter import ClientRepFileAdapter
from firma.ClientRepJson import ClientRepJson
from http.server import BaseHTTPRequestHandler


class BasicWebController(ABC):

    def __init__(self, request_handler: BaseHTTPRequestHandler):
        self.repository = ClientRepFileAdapter(ClientRepFile(ClientRepJson))
        self.request_handler = request_handler
        if self.request_handler.command == 'GET':
            self.handle_get()
        if self.request_handler.command == 'POST':
            self.handle_post()

    @abstractmethod
    def handle_get(self):
        pass

    @abstractmethod
    def handle_post(self):
        pass