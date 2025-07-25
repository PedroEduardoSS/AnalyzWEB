from nicegui import ui
import pandas as pd
from views.data_analysis_tab import *

ui.html("Data Analysis workplace", tag='h1')

with ui.tabs().classes('w-full') as tabs:
    tab1 = ui.tab('Data Analysis')
    tab2 = ui.tab('extraTab')
with ui.tab_panels(tabs).classes('w-full'):
    with ui.tab_panel(tab1):
        data_analysis_tab()
    with ui.tab_panel(tab2):
        ui.label('Second tab')

ui.run()