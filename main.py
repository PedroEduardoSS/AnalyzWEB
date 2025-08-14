from nicegui import ui
import pandas as pd
from views.data_analysis_view import *

dark = ui.dark_mode()

ui.markdown('''
            # Data Analysis workplace
            ''')

ui.switch('Dark mode').bind_value(dark)

data_analysis_view()

ui.run()