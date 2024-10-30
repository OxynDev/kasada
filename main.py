import json, colorama, os, time, asyncio, traceback
from utils import gen, follow

banner = """  _//     _//_//      _//_///////  _////////
  _//     _// _//    _// _//    _//_//      
  _//     _//  _// _//   _//    _//_//      
  _////// _//    _//     _///////  _//////  
  _//     _//    _//     _//       _//      
  _//     _//    _//     _//       _//      
  _//     _//    _//     _//       _//////// .gg/kasada"""
                                          
class Aio:
    def __init__(self):
        os.system("cls")
        self.config = json.loads(open("config.json","r").read())
        self.api_key = ""
        
        self.menu = {
            "1": "Generator",
            "2": "Follow"
            }
        
        self.draw_menu()

    
    def print_banner(self):
        os.system("cls")
        print('\n' + colorama.Fore.GREEN + banner + '\n\n' + colorama.Fore.RESET)
    
    def draw_menu(self):
        while True:
            self.print_banner()
            if not self.check_api_key():
                print((
                    colorama.Fore.RED +
                    " [ X ] " +
                    colorama.Fore.RESET + 
                    " Put hype api key in config.json (discord.gg/kasada)\n" 
                    ))
                time.sleep(3)
                os._exit(1)
            else:
                for i in self.menu:
                    print((
                    colorama.Fore.BLUE +
                    f" [ {i} ] " +
                    colorama.Fore.RESET + 
                    f" {self.menu[i]}" 
                    ))
                print()
                select = input((
                    colorama.Fore.YELLOW +
                    " [ . ] " +
                    colorama.Fore.RESET + 
                    " >> " 
                    ))
                
                try:
                    selected = self.menu[select]
                    print(selected)
                    os.system("cls")
                    
                    if selected == 'Generator':
                        asyncio.run(gen.main(self.config['gen_tasks'], self.api_key))
                    elif selected == 'Follow':
                        
                        target = input((
                            colorama.Fore.YELLOW +
                            " [ . ] " +
                            colorama.Fore.RESET + 
                            " target >> " 
                            ))
                        
                        count = input((
                            colorama.Fore.YELLOW +
                            " [ . ] " +
                            colorama.Fore.RESET + 
                            " count >> " 
                            ))
                        
                        os.system("cls")
                        
                        asyncio.run(follow.main(target, count))
                        
                    time.sleep(3)
                except:
                    traceback.print_exc()
                    print((
                        "\n" + 
                        colorama.Fore.RED +
                        " [ X ] " +
                        colorama.Fore.RESET + 
                        " Invalid\n" 
                        ))
                    time.sleep(2)
                    continue
        
    def check_api_key(self):
        self.api_key = self.config.get("api_key", "")
        if self.api_key == "":
            return False
        else:
            return True
        

if __name__ == "__main__":
    Aio()