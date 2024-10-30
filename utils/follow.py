import random, string, asyncio, traceback, time, colorama, json, requests
from curl_cffi.requests import AsyncSession

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

proxies = open("proxies.txt","r").read().splitlines()


def get_id(target):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US',
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'Content-Type': 'text/plain;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }
        
    try:
        data = '''{
            "operationName":"ChannelRoot_AboutPanel",
            "variables":{
                "channelLogin":"'''+target+'''",
                "skipSchedule":false
            },
            "extensions":{
                "persistedQuery":{
                    "version":1,
                    "sha256Hash":"6089531acef6c09ece01b440c41978f4c8dc60cb4fa0124c9a9d3f896709b6c6"
                }
            }
        }'''

        response = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)
        return response.json()['data']['user']['id']
    except:
        return ''




async def thread(token, target):
    try:

        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "pl-PL",
            "Authorization": "OAuth " + token,
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Device-Id": "YmxdMQzWguuvpfAA11TS7LnPHOYpzteC",
            "Host": "gql.twitch.tv",
        }

        proxy = "http://" + random.choice(proxies)
        
        payload = json.dumps([
            {
                "operationName": "FollowUserMutation",
                "variables": {
                "targetId": str(target),
                "disableNotifications": False
                },
                "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "cd112d9483ede85fa0da514a5657141c24396efbc7bac0ea3623e839206573b8"
                }
                }
            }
        ])
        
        async with AsyncSession(proxy=proxy, http_version=1, verify=False, max_clients=1000, timeout=30) as session:
            try:
                res = await session.post('https://gql.twitch.tv/gql', headers=headers, data=payload)
                res = res.text
                if not "FORBIDDEN" in str(res) and not "Unauthorized" in str(res) and "FollowUserMutation" in str(res) and not "failed integrity check" in str(res):
                    print((
                        colorama.Fore.GREEN +
                        f" [ V ] " +
                        colorama.Fore.RESET + 
                        f" Sent" 
                    ))
                    
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
        

    
async def main(target, count):
    
    target_id = get_id(target)
    
    tasks = []
    tokens = open("tokens.txt","r").read().splitlines()
    
    for i, token in enumerate(tokens):
        tasks.append(thread(token, target_id))
        if i >= int(count):
            break
        
    await asyncio.gather(*tasks)
    await asyncio.sleep(5)