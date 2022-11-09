import os

def get_columns_from_text(file_path='',delimeter=' ',columns="1,2"):    
    os.system(f"""cut -d'{delimeter}' -f{columns} < {file_path}""")

