import pandas as pd


def read_csv_file(file_path):
    """
    读取CSV文件并返回一个DataFrame。

    参数:
    file_path (str): CSV文件的路径。
    columns (list, optional): 指定需要读取的列名。
    dtype (dict, optional): 指定列的数据类型。
    na_values (scalar, str, list-like, or dict, optional): 替换特定值为NA/NaN。
    parse_dates (list, optional): 指定需要解析为日期的列。

    返回:
    pd.DataFrame: 读取的DataFrame。
    """
    try:
        df = pd.read_csv(file_path, encoding='GB18030')
        return df
    except Exception as e:
        print(f"读取CSV文件时出错: {e}")
        return None
