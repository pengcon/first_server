import pandas as pd

def create_dataframe_from_serializer(serializer):
    data = serializer.data
    df = pd.DataFrame([data])
    df = convert_columns_to_float(df, 'INCOME', 'TRAVEL_MOTIVE_1')
    # 시리얼라이저 데이터로부터 데이터프레임 생성
    return df  # 생성된 데이터프레임 반환



def convert_columns_to_float(df, start_col, end_col):
    cols_to_convert = df.columns[df.columns.get_loc(start_col):df.columns.get_loc(end_col)+1]
    df[cols_to_convert] = df[cols_to_convert].astype(float)
    return df