import pandas
from pandas import DataFrame
from copy import deepcopy


class Transformer:
    def __init__(self, df):
        assert isinstance(df, DataFrame), "df needs to be of pandas.DataFrame type!"
        self.df = deepcopy(df)

    def drop_rows_from_first_na(self, column_name):
        self.df = self.df[self.df[column_name].isna().cumsum() == 0]

    def infer_column_to_datetime(self, column_name):
        self.df[column_name] = pandas.to_datetime(
            self.df[column_name], infer_datetime_format=True
        )

    def get_first_cell_value_for_column(self, column_name):
        return self.df.iloc[0][column_name]

    def upsert_into(self, target_df):
        assert isinstance(
            target_df, DataFrame
        ), "target_df needs to be of pandas.DataFrame type!"
        self.df = pandas.concat(
            [target_df[~target_df.index.isin(self.df.index)], self.df]
        )
