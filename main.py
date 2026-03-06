# ライブラリ
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.dialects.oracle import NUMBER, VARCHAR2, DATE, TIMESTAMP
from sqlalchemy import inspect
import cx_Oracle
from tqdm import tqdm

# 接続情報
HOST = ""
PORT = 
SVS = ""
USER = ""
PASS = ""

engine_url = f'oracle+cx_oracle://{USER}:{PASS}@{HOST}:{PORT}/?service_name={SVS}'
engine = create_engine(engine_url)


# 検索内容
schema_name = '' # スキーマ名
search_word = '' # カラム名　含み検索できます 


# mainプログラム
# ========== 設定 ==========
inspector = inspect(engine)

# ========== スキーマ内の全テーブルを取得 ==========
tables = inspector.get_table_names(schema=schema_name)

# ========== 検索ワードを含むカラムを持つテーブルを抽出 ==========
matching_tables = []

for table in tables:
    columns = inspector.get_columns(table, schema=schema_name)
    column_names = [col['name'] for col in columns]
    
    # カラム名に検索ワードが含まれているか確認
    for col_name in column_names:
        if search_word in col_name:
            matching_tables.append(table)
            break  # 同じテーブルは1回だけ追加

# ========== DataFrame に格納 ==========
df_result = pd.DataFrame({
    'テーブル名': matching_tables
})

print(f"【検索結果】")
print(f"検索ワード: {search_word}")
print(f"該当テーブル数: {len(df_result)}\n")
print(df_result)



