import json

with open("jobb.json", encoding="utf-8") as f:
    read_data = f.read()
    data = json.loads(read_data)

    ids = {}
    ids2 = []
    jobb = []
    for index in data:
        ids[index["id"]] = 1
        ids2.append(index["id"])
        # print(index["id"])
        title = index["title"]
        workplaceName = index["workplaceName"]
        occupation = index["occupation"]

        # print(f"{workplaceName:30}, {occupation:50}, {title:100}")
    data = sorted(data, key=lambda student: student["occupation"])
    blacklist_jobs = ["Torgförsäljare/Marknadsförsäljare"]
    filtered_data = []
    for jobb in data:
        if jobb["occupation"] not in blacklist_jobs:
            filtered_data.append(jobb)

    data = filtered_data
    for index in data:
        title = index["title"]
        workplaceName = index["workplaceName"]
        occupation = index["occupation"]
        link = "https://arbetsformedlingen.se/platsbanken/annonser/" + index["id"]
        print(f"{occupation:30.30} \t{workplaceName:30.30} \t{title:60.60} \t{link}")

    print(len(ids))
    print(len(ids2))

    # {
    #     "id": "28200255",
    #     "publishedDate": "2023-10-31T13:02:07Z",
    #     "lastApplicationDate": "2023-12-31T22:59:59Z",
    #     "title": "Sjuksköterska",
    #     "occupation": "Sjuksköterska, grundutbildad",
    #     "workplace": "Norrtälje",
    #     "workplaceName": "Attendo Sverige",
    #     "unspecifiedWorkplace": false,
    #     "published": true,
    #     "positions": 1,
    #     "sourceLinks": null
    # },
