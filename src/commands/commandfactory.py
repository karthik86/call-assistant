from commands.command import Command
from commands.chat import Chat
from commands.summary import Summary
from commands.conversation import Conversation
from openaiclient import OpenAIClient

class CommandFactory:

    def __init__(self, aiclient: OpenAIClient, meeting_filepath: str):
        self.aiclient = aiclient
        self.meeting_filepath = meeting_filepath
        
    
    def get_command_processor(self, command: str) -> Command:
        commands = {
            'chat': Chat(self.aiclient, self.meeting_filepath),
            'summary': Summary(self.aiclient, self.meeting_filepath),
            'conversation': Conversation(self.aiclient, self.meeting_filepath)
        }

        command_processor = commands.get(command)
        if(command_processor == None):
            raise ValueError("unsupported opeartion")
        return command_processor
