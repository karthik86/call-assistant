from openaiclient import OpenAIClient
from downloadhelper import DownloadHelper
from commands.commandfactory import CommandFactory
import argparse

class CLI:
        
    def run(self):
        parser = argparse.ArgumentParser(description='Intelligent meeting assistant.')
        parser.add_argument("token", type=str, help="access token for open ai")
        args = parser.parse_args()

        options = {
            "1":"conversation",
            "2":"summary",
            "3":"chat"
        }
        print("\nprovide video/audio youtube url of recorded meeting")
        url = input("url: ")
        helper = DownloadHelper(url=url)
        aiclient = OpenAIClient(args.token)
        print("\nChoose one of the following options:")
        print("1. Print conversation")
        print("2. Summarize conversation")
        print("3. Ask questions about meeting")
        choice = input("select options from 1-3 : ")
        command = options.get(choice)
        if command == None:
            print("Invalid command")
        else:
            command_factory = CommandFactory(aiclient, helper.download())
            command_processor = command_factory.get_command_processor(command=command)
            command_processor.execute()


if __name__ == '__main__':
    cli = CLI()
    cli.run()
            

            




    