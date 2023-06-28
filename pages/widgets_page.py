from playwright.sync_api import Page

from pages.homepage import HomePage
from pages.sidebar import Sidebar


class WidgetsPage(HomePage, Sidebar):

    def __init__(self, page: Page):
        HomePage.__init__(self, page)
        Sidebar.__init__(self, page)
