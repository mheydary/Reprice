import pandas as pd


class DataManagement:
    def __init__(self):
        self.state_URL = 'http://files.zillowstatic.com/research/public/State/State_MedianValuePerSqft_AllHomes.csv'
        self.county_URL = 'http://files.zillowstatic.com/research/public/County/County_MedianValuePerSqft_AllHomes.csv'
        self.city_URL = 'http://files.zillowstatic.com/research/public/City/City_MedianValuePerSqft_AllHomes.csv'
        self.neighborhood_URL = 'http://files.zillowstatic.com/research/public/Neighborhood/Neighborhood_MedianValuePerSqft_AllHomes.csv'

    @staticmethod
    def retrieveData(url):
        df_front = pd.read_csv(url, header=0, usecols=[0, 1, 2])

        cols_month = pd.read_csv(url, nrows=1).columns
        df_month = pd.read_csv(url, header=0, usecols=cols_month[-3:])

        df = pd.concat([df_front, df_month], axis=1)
        df.fillna(method='ffill', axis=0, inplace=True)

        return df

    def getState(self, stateName):
        df = self.retrieveData(self.state_URL)
        df = df[df['RegionName'] == stateName]
        return df.values[0, -3:]

    def getCounty(self, countyName):
        df = self.retrieveData(self.county_URL)
        df = df[df['RegionName'] == countyName]
        return df.values[0, -3:]

    def getCity(self, cityName):
        df = self.retrieveData(self.city_URL)
        df = df[df['RegionName'] == cityName]
        return df.values[0, -3:]

    def getNeighborhood(self, neighborhoodName):
        df = self.retrieveData(self.neighborhood_URL)
        df = df[df['RegionName'] == neighborhoodName]
        return df.values[0, -3:]

def main():
    dm = DataManagement()
    print(dm.getCity("New York"))


if __name__ == "__main__": main()