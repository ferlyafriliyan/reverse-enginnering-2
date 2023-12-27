import os, sys, requests, bs4, re, json, random
from rich import print

# RICH COLOR STYLE
Z2 = "[#000000]"  # Hitam
M2 = "[#FF0000]"  # Merah
H2 = "[#00FF00]"  # Hijau
K2 = "[#FFFF00]"  # Kuning
B2 = "[#00C8FF]"  # Biru
U2 = "[#AF00FF]"  # Ungu
N2 = "[#FF00FF]"  # Pink
O2 = "[#00FFFF]"  # Biru Muda
P2 = "[#FFFFFF]"  # Putih
J2 = "[#FF8F00]"  # Jingga
A2 = "[#AAAAAA]"  # Abu-Abu

UserAgentWindows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
HeadersGet = lambda i=UserAgentWindows: {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Dpr': '1', 'Pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-True-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace', 'Sec-Ch-Prefers-Color-Scheme': 'dark', 'Sec-Ch-Ua': '', 'Sec-Ch-Ua-Full-Version-List': '', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Model': '', 'Sec-Ch-Ua-Platform': '', 'Sec-Ch-Ua-Platform-Version': '', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': i}
HeadersPost = lambda i=UserAgentWindows: {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin':'https://web.facebook.com', 'Referer':'https://web.facebook.com', 'Sec-Ch-Prefers-Color-Scheme': 'dark', 'Sec-Ch-Ua': '', 'Sec-Ch-Ua-Full-Version-List': '', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Model': '', 'Sec-Ch-Ua-Platform': '', 'Sec-Ch-Ua-Platform-Version': '', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': i}

def clear(): 
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

def GetData(req):
    Author = 'Denventa'
    av = re.search('"actorID":"(.*?)"', str(req)).group(1)
    __user = av
    __a = str(random.randrange(1, 6))
    __hs = re.search('"haste_session":"(.*?)"', str(req)).group(1)
    dpr = '1.5'
    __ccg = re.search('"connectionClass":"(.*?)"', str(req)).group(1)
    __rev = re.search('"__spin_r":(.*?),', str(req)).group(1)
    __spin_r = __rev
    __spin_b = re.search('"__spin_b":"(.*?)"', str(req)).group(1)
    __spin_t = re.search('"__spin_t":(.*?),', str(req)).group(1)
    __hsi = re.search('"hsi":"(.*?)"', str(req)).group(1)
    __comet_req = '15'
    fb_dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}', str(req)).group(1)
    jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"}', str(req)).group(1)
    Data = {'av': av, '__user': __user, '__a': __a, '__hs': __hs, 'dpr': dpr, '__ccg': __ccg, '__rev': __rev, '__spin_r': __spin_r, '__spin_b': __spin_b, '__spin_t': __spin_t, '__hsi': __hsi, '__comet_req': __comet_req, 'fb_dtsg': fb_dtsg, 'jazoest': jazoest, 'lsd': lsd}
    return Data

def Execute():
    Cookie = '' # Put your Cookies here | # Taruh Cookie Anda di sini
    try: # Place your Sacrifice Account Cookie here | # Tempatkan Cookie Akun Pengorbanan Anda di sini
        InputID = input("Masukkan ID yang Ingin Di Follow: ")
        url = 'https://web.facebook.com/%s' % (InputID)
        r = requests.Session()
        req = r.get(url, headers=HeadersGet(), cookies={'cookie': Cookie}).text
        Data = GetData(req)
        with open("GraphQl.txt", "a") as f:
            f.write(f"\n\nData:\n{json.dumps(Data, indent=4)}\n\n")
        print(Data)
        Data.update({'fb_api_caller_class': 'RelayModern','server_timestamps': True})
        Var = {"input": {"attribution_id_v2": "ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,tap_bookmark,1700238612634,388758,100064626647103,,","is_tracking_encrypted": False,"subscribe_location": "PROFILE","subscribee_id": InputID,"tracking": None,"actor_id": Data['__user'],"client_mutation_id": "1"},"scale":1.5}
        Data.update({'fb_api_req_friendly_name': 'CometUserFollowMutation','variables': json.dumps(Var),'doc_id': '7123303487693025'})
        pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPost(), cookies={'cookie': Cookie}).json()
        with open("GraphQl.txt", "a") as f:
            f.write(f"\n\nResponse:\n{json.dumps(pos, indent=4)}\n\n")
        print(pos)
        print(f"Berhasil memfollow Akun: {InputID}")
        print(f"Response tersimpan di file: GraphQl.txt")

        # Memfollow akun kedua dengan ID 100073125893802
        Var2 = {"input": {"attribution_id_v2": "ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,tap_bookmark,1700238612634,388758,100064626647103,,","is_tracking_encrypted": False,"subscribe_location": "PROFILE","subscribee_id": "100073125893802","tracking": None,"actor_id": Data['__user'],"client_mutation_id": "1"},"scale":1.5}
        Data.update({'fb_api_req_friendly_name': 'CometUserFollowMutation','variables': json.dumps(Var2),'doc_id': '7123303487693025'})
        pos2 = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPost(), cookies={'cookie': Cookie}).json()

    except (Exception, AttributeError) as e:
        print("%s[%s•%s] %sCookies Invalid %s!%s " % (M2, A2, M2, P2, M2, P2))

if __name__ == '__main__':
    try:
        clear()
        Execute()
    except (KeyboardInterrupt, Exception, AttributeError) as e:
        exit(f"[ Error ]: {str(e).capitalize()}!")
