# FlashAlert Mirror

A lightweight mirror of FlashAlert news feeds in JSONL format.

## Purpose

This repository automatically mirrors news feeds from [FlashAlert](https://www.flashalert.net/) and converts them to JSONL to provide:

- **Easy parsing**: No XML parser needed - just JSON
- **Clear diffs**: One item per line makes git diffs crystal clear
- **Faster access**: Direct file access without API delays
- **CORS-friendly**: GitHub Pages and raw content URLs work seamlessly in web applications
- **Reliability**: Cached copies continue working even if the source is temporarily unavailable

## Regions

The following FlashAlert regions are mirrored hourly:

| Region ID | Coverage Area | JSONL Feed |
|-----------|---------------|------------|
| 1 | Portland/Vancouver/Salem | [json/news-1.jsonl](json/news-1.jsonl) |
| 2 | Eugene/Springfield/Roseburg/Albany/Corvallis | [json/news-2.jsonl](json/news-2.jsonl) |
| 5 | Colorado Springs/Rocky Mountain Area | [json/news-5.jsonl](json/news-5.jsonl) |
| 7 | Spokane/Eastern Washington/Northern Idaho | [json/news-7.jsonl](json/news-7.jsonl) |
| 10 | Bend/Central Oregon/Eastern Oregon | [json/news-10.jsonl](json/news-10.jsonl) |
| 12 | Seattle/Western Washington | [json/news-12.jsonl](json/news-12.jsonl) |
| 13 | Columbia/Tri Cities/Pendleton/Yakima | [json/news-13.jsonl](json/news-13.jsonl) |
| 15 | Boise/Southern Idaho | [json/news-15.jsonl](json/news-15.jsonl) |
| 25 | Medford/Klamath Falls/Grants Pass | [json/news-25.jsonl](json/news-25.jsonl) |

## Format

Each file is JSONL (JSON Lines) format - one news item per line. Example:

```json
{"news_id": "184714", "effective_date": "2025-10-30 11:16:39", "category": "School Districts", "headline": "...", "detail": "...", "org": "..."}
{"news_id": "184522", "effective_date": "2025-10-21 13:45:59", "category": "School Districts", "headline": "...", "detail": "...", "org": "..."}
```

## Update Frequency

Feeds are automatically updated **every hour** via GitHub Actions.

## Source and license

All news content is provided by [FlashAlert Newswire](https://www.flashalertnewswire.net/). This repository is simply a mirror for convenience and does not claim ownership of the content. Only the structure and code is openly licensed per [LICENSE](LICENSE).

Original feed URLs follow this pattern:
```
https://www.flashalertnewswire.net/IIN/reportsX/flashnews_xml2.php?RegionID=[id]
```
