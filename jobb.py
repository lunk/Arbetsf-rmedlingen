import requests
import datetime
from datetime import date, timedelta
import json

now = datetime.datetime.now().isoformat() + "Z"
last_month = (datetime.datetime.now() - timedelta(days=60)).isoformat() + "Z"
max_records = 100


def get_jobs(index):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en;q=0.5",
        "INT_SYS": "platsbanken_web_beta",
        # "Content-Type": "application/json",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
    }
    payload = {
        "filters": [{"type": "freetext", "value": "norrtälje"}],
        "fromDate": last_month,
        "order": "date",
        "maxRecords": max_records,
        "startIndex": index,
        "toDate": now,  # format: "2023-11-01T15:37:14.751986Z"
        "source": "pb",
    }
    # python = "2023-11-01T16:26:14.611605"
    # curlll = "2023-11-01T14:24:26.516Z"
    url = "https://platsbanken-api.arbetsformedlingen.se/jobs/v1/search"

    r = requests.post(url, headers=headers, json=payload)
    return r.json()


result = get_jobs(0)
jobs = result["ads"]
numberOfAds = result["numberOfAds"]
print("numberOfAds=", numberOfAds)

for index in range(max_records, numberOfAds, max_records):
    result = get_jobs(index)
    jobs += result["ads"]
    print("len(jobs)", len(jobs), 'len(result["ads"])', len(result["ads"]))

f = open("jobb.json", "w", encoding="utf-8")
f.write(json.dumps(jobs))
f.close()
