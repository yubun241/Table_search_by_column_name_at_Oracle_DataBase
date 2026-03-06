## Table_search_by_column_name
OracleのDataBaseでカラム名とスキーマ名を入力するとテーブル名が出力されるコードです

## 概要

このツールは以下の機能を提供します：

- **スキーマ内のテーブル一覧取得** - 指定したスキーマ内の全テーブルをリスト化
- **カラム名検索**（部分一致） - 検索ワードを含むカラムを持つテーブルを自動抽出
- **DataFrame 形式で結果出力** - Pandas DataFrame として結果を取得、さらなる分析が可能

## 必要な環境

- Python 3.7 以上
- pandas
- sqlalchemy
- cx_Oracle（またはoracledb）

## インストール

### 1. 依存ライブラリのインストール

```bash
pip install pandas sqlalchemy cx_Oracle
