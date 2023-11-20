import os
import requests
from os import system, mkdir
from random import choice
from rich.console import Console
from rich.panel import Panel

result_image_path = '/sdcard/resultImage/'  # line:1
clear_command = 'clear'  # line:2
color_code = '\x1b[1;9'  # line:3
M, H, K, U, B, C, P = color_code + '1m', color_code + '2m', color_code + '3m', color_code + '4m', color_code + '5m', color_code + '6m', color_code + '7m'  # line:4

class Main:  # line:15
    def __init__(self):  # line:16
        content_type = 'application/json'
        self.url_api = 'https://fast-apiimggen--etwg34dassad211.repl.co/'
        self.url_generator_image = self.url_api + 'generate-image'
        self.url_image = self.url_api + 'image'
        self.headers = {'accept': content_type, 'Content-Type': content_type}
        self.status_error = False
        self.load = '/-\\|'
        self.titik = ['.', '..', '...']
        self.warna = [M, K, H, U, B, C]
        self.decode = 'Denventa'
        self.version = '1.1.0'
        self.release = '20/11/2023'
        self.deobfuscate = '20/11/2023'
        self.session = requests.Session()  # line:16

    def GeneratorImage(self, prompt, headers):  # line:17
        while True:  # line:18
            params = {'prompt': prompt, 'status_error': self.status_error}
            new_headers = self.headers.copy()  # Copy existing headers
            new_headers.update(headers.headers)  # Update with headers from the response object
            try:
                request_image = self.session.post(self.url_generator_image, headers=new_headers, json=params)  # line:20
            except Exception as error:
                print(f"{M}[!]{K} {str(error)}")  # line:21
            if request_image.text == 'null':
                continue  # line:22
            else:
                break  # line:23

    def Home(self):  # line:24
        client_host_key = 'client_host'
        white_color = 'white'
        left_justify = 'left'
        system(clear_command)  # line:25
        try:
            self.read_root = self.session.get(self.url_api)  # line:26
        except Exception as error:
            print(f"{M}[!]{K} {error}")  # line:27
        console = Console()  # Added line

        # Menempatkan informasi dalam variabel
        panel_info = Panel("""[#00BFFF]   Open link : https://pastebin.com/2D0t2xSj
   Disclaimer : ChatGPT
   Decrypt by : Ferly Afriliyan [#808080] V : [1.1.0]
        """, title='[#FF8F00][ [#00FF33]By Ferly Afriliyan [#FF8F00]]',
            subtitle='[#FF8F00][ [#00FF33]Create images using text[#FF8F00]]', style='#FFFFFF')

        # Mencetak informasi yang disimpan dalam variabel
        console.print(panel_info)
        print(f"{K}[{H}#{K}] {P}Client Host : {H}{self.read_root.json()[client_host_key]}")
        self.prompt = input(f"{K}[{H}+{K}] {P}Input prompt : {H}")
        system(clear_command)
        console.print(panel_info)

        print(f" {K}[{H}#{K}] {P}Client Host: {H}{self.read_root.json()[client_host_key]}")
        console.print(Panel('[green]' + self.prompt, title=f"[green]( [white]Prompt [green])",
            style=white_color, width=40))
        self.GeneratorImage(self.prompt, self.read_root)  # line:28

        while True:  # line:29
            print(
                f"{K}[{choice(self.warna)}{choice(self.load)}{K}] {P}Generate Image{choice(self.titik)}    ",
                end='\r')  # line:30
            try:
                self.list_image = requests.get(self.url_image).json()  # line:31
            except Exception as error:
                print(f"{M}[!]{K} {error}")  # line:32
            if self.list_image['status_gen'] == True:
                break  # line:33
            else:
                continue  # line:34
        self.result_url = self.list_image['images']
        self.NumberOfImages = len(self.result_url)  # line:35
        for link in self.result_url:  # line:36
            try:
                response = requests.get(link)  # line:37
            except Exception as error:
                print(f"{M}[!]{K} {error}")  # line:38
            open(result_image_path + link.replace(self.url_image, ''), 'wb').write(response.content)  # line:39

        # Mencetak informasi yang disimpan dalam variabel
        console.print(
            Panel(f"[green]Success Created {self.NumberOfImages} Image Saved In:{result_image_path}",
                  title=f"[green]( [white]Success [green])",  # Modified line
                  style=white_color, width=40))  # Modified line

if __name__ == '__main__':  # line:41
    try:
        mkdir(result_image_path)  # line:42
    except:
        pass  # line:43
    system('git pull')
    Main().Home()
