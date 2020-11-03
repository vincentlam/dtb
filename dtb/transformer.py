import pandas
from pandas import DataFrame


class Transformer:
    def __init__(self, df):
        assert isinstance(df, DataFrame), "df needs to be of pandas.DataFrame type!"
        self.df = df

    def drop_rows_from_first_na(self, column_name):
        self.df = self.df[self.df[column_name].isna().cumsum() == 0]

    def infer_column_to_datetime(self, column_name):
        self.df[column_name] = pandas.to_datetime(
            self.df[column_name], infer_datetime_format=True
        )

    def get_first_cell_value_for_column(self, column_name):
        return self.df.iloc[0][column_name]
