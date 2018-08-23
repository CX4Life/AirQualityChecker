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
        self.times = []
        self.scores = []

    def report(self):
        plt.plot(self.times, self.scores, '-ro')
        plt.ylabel('AQI')
        plt.show()

    def scrape(self):
        aqi_page = requests.get(self.air_quality_site_url)
        soup = bs4.BeautifulSoup(aqi_page.content, 'html.parser')
        current_score = int(soup.find('span', {'id': 'lblCurrentIndex'}).text)
        now = datetime.now().time()
        self.times.append((((now.hour * 60) + now.minute) * 60) + now.second)
        self.scores.append(current_score)


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
