import pandas as pd
from nicegui import app, events, ui
import os

class DataAnalysis:
    dataframe = pd.DataFrame()
    
    def load_csv_file(self, e: events.UploadEventArguments) -> pd.DataFrame:
        try:
            upload_dir = 'uploads'
            os.makedirs(upload_dir, exist_ok=True)

            file_path = os.path.join(upload_dir, e.name) 
            
            with open(file_path, 'wb') as f:
                f.write(e.content.read())

            ui.notify(f'Arquivo "{e.name}" salvo em: {file_path}', type='positive')

            self.dataframe = pd.read_csv(file_path)

            return ui.aggrid.from_pandas(self.dataframe).classes('max-h-40')
        

        except Exception as ex:
            ui.notify(f'Erro ao processar ou salvar o arquivo CSV: {ex}', type='negative')
        

    def describe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        describe = dataframe.describe()
        return describe