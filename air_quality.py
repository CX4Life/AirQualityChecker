import bs4
import time
from datetime import datetime
import requests
import matplotlib.pyplot as plt

__author__ = 'Tim Woods'
__copyright__ = 'Copyright (c) 2018, Tim Woods'
__license__ = 'MIT'

bellingham_site_url = 'https://fortress.wa.gov/ecy/enviwa/StationInfo.aspx?ST_ID=195'


class AQI:
    def __init__(self, site_url):
        self.air_quality_site_url = site_url
        self.start_time = None
        self.times = []
        self.scores = []

    @staticmethod
    def _seconds_from_datetime(date_time):
        return (((date_time.hour * 60) + date_time.minute) * 60) + date_time.second

    def report(self):
        plt.plot(self.times, self.scores, '-ro')
        plt.ylabel('AQI')
        plt.show()

    def scrape(self):
        aqi_page = requests.get(self.air_quality_site_url)
        soup = bs4.BeautifulSoup(aqi_page.content, 'html.parser')
        try:
            current_score = int(soup.find('span', {'id': 'lblCurrentIndex'}).text)
            now = datetime.now().time()
            if self.start_time is None:
                self.start_time = self._seconds_from_datetime(now)
            self.times.append(self.start_time - self._seconds_from_datetime(now))
            self.scores.append(current_score)
        except AttributeError:
            pass


def main():
    score_reporter = AQI(bellingham_site_url)
    count = 0
    while True:
        score_reporter.scrape()
        if count % 5 == 0:
            score_reporter.report()
        count += 1
        time.sleep(60)


if __name__ == '__main__':
    main()
