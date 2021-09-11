import globalPluginHandler, webbrowser, ui, wx, gui, scriptHandler, os

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = ("websites")

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self._toggleGestures = False
		self.createMenu()

	def createMenu(self):
		self.submenu_websites = wx.Menu()
		self.submenu_chess = wx.Menu()
		item = self.submenu_chess.Append(wx.ID_ANY, "accessible chess\talt+control+shift+a")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.accessiblechess, item)
		item = self.submenu_chess.Append(wx.ID_ANY, "lichess\talt+control+shift+l")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.lichess, item)
		self.submenu_websites.Append(wx.ID_ANY, "chess", self.submenu_chess)
		self.submenu_english = wx.Menu()
		item = self.submenu_english.Append(wx.ID_ANY, "google\talt+control+windows+g")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.google, item)
		item = self.submenu_english.Append(wx.ID_ANY, "gmail\tcontrol+windows+g")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.gmail, item)
		item = self.submenu_english.Append(wx.ID_ANY, "blind help\talt+control+shift+b")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.blindhelp, item)
		self.submenu_websites.Append(wx.ID_ANY, "english", self.submenu_english)
		self.submenu_persian = wx.Menu()
		item = self.submenu_persian.Append(wx.ID_ANY, "محله نابینایان, گوش کن\talt+control+shift+g")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.gooshkon, item)
		item = self.submenu_persian.Append(wx.ID_ANY, "فیلم و سریال صوتی\talt+control+shift+m")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.mp3movies, item)
		item = self.submenu_persian.Append(wx.ID_ANY, "سانگ سرا - جهان موسیقی بی کلام\talt+control+shift+s")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.songsara, item)
		self.submenu_websites.Append(wx.ID_ANY, "persian", self.submenu_persian)
		self.submenu_turkish = wx.Menu()
		item = self.submenu_turkish.Append(wx.ID_ANY, "mp3indirdur\talt+control+shift+i")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.mp3indirdur, item)
		self.submenu_websites.Append(wx.ID_ANY, "turkish", self.submenu_turkish)
		item = self.submenu_websites.Append(wx.ID_ANY, "about add-on...")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.about, item)
		self.submenu_item = gui.mainFrame.sysTrayIcon.menu.InsertMenu(2, wx.ID_ANY, "websites", self.submenu_websites)

	def accessiblechess(self, event):
		webbrowser.open("http://accessiblechess.herokuapp.com")

	def script_accessiblechess(self, gesture):
		ui.message("accessible chess")
		webbrowser.open("http://accessiblechess.herokuapp.com")
	script_accessiblechess.__doc__ = ("سایت accessible chess رُ باز میکنه")

	def lichess(self, event):
		webbrowser.open("http://lichess.org")

	def script_lichess(self, gesture):
		ui.message("lichess")
		webbrowser.open("http://lichess.org")
	script_lichess.__doc__ = ("سایت lichess رُ باز میکنه")

	def google(self, event):
		webbrowser.open("http://google.com")

	def script_google(self, gesture):
		ui.message("گوگل")
		webbrowser.open("http://google.com")
	script_google.__doc__ = _("""سایت گوگل رُ باز میکنه.""")

	def gmail(self, event):
		webbrowser.open("http://gmail.com")

	def script_gmail(self, gesture):
		ui.message("gmail")
		webbrowser.open("http://gmail.com")
	script_gmail.__doc__ = ("""gmail رُ باز میکنه""")

	def blindhelp(self, event):
		webbrowser.open("http://blindhelp.net")

	def script_blindhelp(self, gesture):
		ui.message("blind help")
		webbrowser.open("http://blindhelp.net")
	script_blindhelp.__doc__ = ("""سایت blindhelp رُ باز میکنه.""")

	def gooshkon(self, event):
		webbrowser.open("http://gooshkon.ir")

	def script_gooshkon(self, gesture):
		ui.message("محله نابینایان")
		webbrowser.open("http://gooshkon.ir")
	script_gooshkon.__doc__ = _("""سایت محله نابینایان رُ باز میکنه.""")

	def mp3movies(self, event):
		webbrowser.open("http://mp3movies.ir")

	def script_mp3movies(self, gesture):
		ui.message("فیلم و سریال صوتی")
		webbrowser.open("http://mp3movies.ir")
	script_mp3movies.__doc__ = ("سایت فیلم و سریال صوتی (mp3movies) رُ باز میکنه")

	def songsara(self, event):
		webbrowser.open("http://songsara.net/")

	def script_songsara(self, gesture):
		ui.message("سانگ سرا - جهان موسیقی بی کلام")
		webbrowser.open("http://songsara.net/")
		script_songsara.__doc__ = ("سایت songsara رُ باز میکنه")

	def mp3indirdur(self,event):
		webbrowser.open("http://mp3indirdur.mobi")

	def script_mp3indirdur(self, gesture):
		ui.message("mp3indirdur")
		webbrowser.open("http://mp3indirdur.mobi")
	script_mp3indirdur.__doc__ = ("سایت mp3indirdur رُ باز میکنه")

	def about(self, event):
		gui.messageBox("version 1.0\nthis add-on is written by hamid rezayi from tabriz azerbayjan", "about add-on", wx.OK)

	__gestures = {
		"kb:alt+control+shift+a": "accessiblechess",
		"kb:alt+control+shift+l": "lichess",
		"kb:alt+control+windows+g": "google",
		"kb:control+windows+g":"gmail",
		"kb:alt+control+shift+b": "blindhelp",
		"kb:alt+control+shift+g": "gooshkon",
		"kb:alt+control+shift+m": "mp3movies",
		"kb:alt+control+shift+s": "songsara",
		"kb:alt+control+shift+i": "mp3indirdur",
		"kb:alt+control+shift+p": "programs_features",
	}