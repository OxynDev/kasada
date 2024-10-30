import random, string, asyncio, traceback, time, colorama
from curl_cffi.requests import AsyncSession

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

proxies = open("proxies.txt","r").read().splitlines()

async def thread(api_key):
    while True:
        try:
            
            async with AsyncSession(http_version=1, verify=False) as session_captcha:
                
                data = {
                    "api_key": api_key,
                }

                s = time.time()
                res = await session_captcha.post("http://liveboost.net/v1/solv",json=data, timeout=30)
                #print("res",time.time()-s,res.text)
                res = res.json()
                if res['success'] == True:
                    
                    device = res['captcha']['device']
                    useragent = res['captcha']['useragent']
                    captcha_token = res['captcha']['integrity']
                    
                    user = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                    symbol = ['@', '$', '&', '_']
                    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + random.choice(symbol)
                    
                    headers = {
                        "Accept": "application/vnd.twitchtv.v3+json",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": 'en-US,en;q=0.5',
                        "Api-Consumer-Type": "mobile; Android/2104006",
                        "Client-ID": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                        "Connection": "Keep-Alive",
                        "Content-Type": "application/json; charset=UTF-8",
                        "Host": "passport.twitch.tv",
                        "User-Agent": useragent, 
                        "X-Device-ID": device,
                        "X-App-Version": "21.4.0",
                    }

        
                    email = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '@gmail.com'

                    data = '{"username":"'+user+'","password":"'+password+'","email":"'+email+'","birthday":{"day":'+str(random.randint(1,28))+',"month":'+str(random.randint(1,12))+',"year":'+str(random.randint(1981,1998))+'},"client_id":"kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code": true,"integrity_token":"'+captcha_token+'"}'
                    
                    proxy = "http://" + random.choice(proxies)
                    async with AsyncSession(proxy=proxy, http_version=1, verify=False, max_clients=1000, timeout=30) as session:
                        try:
                            response = await session.post('https://passport.twitch.tv/protected_register', headers=headers, data=data)
                            if "access_token" in response.text:
                                access = response.json()['access_token']
                                
                                print((
                                    colorama.Fore.GREEN +
                                    f" [ V ] " +
                                    colorama.Fore.RESET + 
                                    f" {access}" 
                                ))
                                
                                open('tokens.txt', 'a').write(f'{access}\n')
                            else:
                                print((
                                    colorama.Fore.RED +
                                    f" [ X ] " +
                                    colorama.Fore.RESET + 
                                    f" Failed" 
                                ))
                        except:
                            print((
                                colorama.Fore.YELLOW +
                                f" [ ! ] " +
                                colorama.Fore.RESET + 
                                f" Error" 
                            ))
        except:
            print((
                colorama.Fore.YELLOW +
                f" [ ! ] " +
                colorama.Fore.RESET + 
                f" Error" 
            ))
            #traceback.print_exc()
            pass
        

    
async def main(tasks_count, api_key):
    tasks = []
    for i in range(tasks_count):
        tasks.append(thread(api_key))
        
    await asyncio.gather(*tasks)

