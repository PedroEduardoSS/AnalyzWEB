import pandas as pd
from nicegui import app, events, ui
import os

class DataAnalysis:
    dataframe = pd.DataFrame()
    
    def load_csv_file(self, e: events.UploadEventArguments):
        try:
            upload_dir = 'uploads'
            os.makedirs(upload_dir, exist_ok=True)

            file_path = os.path.join(upload_dir, e.name) 
            
            with open(file_path, 'wb') as f:
                f.write(e.content.read())

            ui.notify(f'Arquivo "{e.name}" salvo em: {file_path}', type='positive')

            self.dataframe = pd.read_csv(file_path)

            return ui.aggrid.from_pandas(self.dataframe).classes('max-h-100')
        

        except Exception as ex:
            ui.notify(f'Erro ao processar ou salvar o arquivo CSV: {ex}', type='negative')
        

    def describe(self) -> pd.DataFrame:
        describe = self.dataframe.describe()
        describe_column = ui.column()
        with describe_column:
            ui.label(f"{describe.iloc[0]}").classes('w-full')
            ui.label(f"{describe.iloc[1]}").classes('w-full')
            ui.label(f"{describe.iloc[2]}").classes('w-full')
            ui.label(f"{describe.iloc[3]}").classes('w-full')
            ui.label(f"{describe.iloc[4]}").classes('w-full')
            ui.label(f"{describe.iloc[5]}").classes('w-full')
            ui.label(f"{describe.iloc[6]}").classes('w-full')
            ui.label(f"{describe.iloc[7]}").classes('w-full')
        return describe_column