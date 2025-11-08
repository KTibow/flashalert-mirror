#!/usr/bin/env python3
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.request import urlopen

REGIONS = [1, 2, 5, 7, 10, 12, 13, 15, 25]
json_dir = Path("json")
json_dir.mkdir(exist_ok=True)

for region_id in REGIONS:
    url = f"https://www.flashalertnewswire.net/IIN/reportsX/flashnews_xml2.php?RegionID={region_id}"
    print(f"Fetching region {region_id}...")

    with urlopen(url) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)
    items = []

    # Parse news items
    for category in root.findall(".//news_category"):
        for report in category.findall("news_report"):
            item = {
                "news_id": report.get("news_id"),
                "effective_date": report.get("effective_date"),
                "category": category.get("name"),
                "headline": report.findtext("headline", ""),
                "detail": report.findtext("detail", ""),
            }
            orgname = report.find("orgname")
            if orgname is not None:
                item["org"] = orgname.text
            items.append(item)

    # Parse emergency items
    for category in root.findall(".//emergency_category"):
        for report in category.findall("emergency_report"):
            item = {
                "report_id": report.get("report_id"),
                "effective_date": report.get("effective_date"),
                "category": category.get("name"),
                "detail": report.findtext("detail", ""),
                "operating_code": report.get("operating_code"),
            }
            orgname = report.find("orgname")
            if orgname is not None:
                item["org"] = orgname.text
            items.append(item)

    items.sort(key=lambda x: x.get("news_id") or x.get("report_id", ""))

    with open(json_dir / f"news-{region_id}.jsonl", "w") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"  ✓ {len(items)} items")
