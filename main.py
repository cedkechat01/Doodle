import os

# Source - https://stackoverflow.com/a/287944
class bcolors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def main():
    intro = """
    Welcome to:


    888888ba                          dP dP           
    88    `8b                         88 88           
    88     88 .d8888b. .d8888b. .d888b88 88 .d8888b. 
    88     88 88'  `88 88'  `88 88'  `88 88 88ooood8 
    88    .8P 88.  .88 88.  .88 88.  .88 88 88.  ... 
    8888888P  `88888P' `88888P' `88888P8 dP `88888P'
    
            Developed by: cedkechat

    A simple terminal for speak with people. (Need Internet connection)


    ___________________________________________
    | 1. Start Conversation                   |
    | 2. Settings                             |
    | 3. Help                                 |
    | 4. Exit                                 |
    |_________________________________________|
    
    
    """


    print(bcolors.BLUE + intro + bcolors.RESET)


if __name__ == "__main__":
    main()