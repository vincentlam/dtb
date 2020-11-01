from pandas import DataFrame


class Transformer:
    """
    import pandas as pd
    from dtb.reader import pd_input
    src = pd_input('https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv')
    df = pd.read_csv(src)
    df[df['date'].isna().cumsum() == 0]
    """

    def __init__(self, df):
        assert isinstance(df, DataFrame), "df needs to be of pandas.DataFrame type!"
        self.df = df
