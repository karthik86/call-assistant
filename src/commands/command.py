from openaiclient import OpenAIClient
from abc import ABC, abstractmethod

class Command(ABC):

    def __init__(self, aiclient: OpenAIClient, meeting_filepath: str):
        self.aiclient = aiclient
        self.meeting_filepath = meeting_filepath
    
    @abstractmethod
    def execute(self):
        pass