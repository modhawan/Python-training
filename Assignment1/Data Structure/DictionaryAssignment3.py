sampleDict = {"name": "kelly", "age": 25, "salary": 8000, "city": "New york"}
sampleDict["location"] = sampleDict.get("city")
sampleDict.pop("city")
print(sampleDict)