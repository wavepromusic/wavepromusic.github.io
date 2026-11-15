#!/usr/bin/env python3
"""Atualiza o catálogo editorial do Ressignificar a partir do feed público do canal."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree

CHANNEL_ID = "UC5r9xZUJ0xuFrcTID3h4XJA"
FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
CATALOG_PATH = Path("resignificar/catalog.json")
ATOM = "{http://www.w3.org/2005/Atom}"
YT = "{http://www.youtube.com/xml/schemas/2015}"
MEDIA = "{http://search.yahoo.com/mrss/}"


def text(element: ElementTree.Element | None, default: str = "") -> str:
    return element.text.strip() if element is not None and element.text else default


def fetch_recent_entries() -> list[dict[str, str]]:
    request = Request(FEED_URL, headers={"User-Agent": "WaveProCatalogSync/1.0"})
    with urlopen(request, timeout=20) as response:  # nosec B310 - URL fixa e HTTPS.
        root = ElementTree.fromstring(response.read())
    entries: list[dict[str, str]] = []
    for entry in root.findall(f"{ATOM}entry"):
        video_id = text(entry.find(f"{YT}videoId"))
        title = text(entry.find(f"{ATOM}title"))
        if not video_id or not title:
            continue
        thumbnail = entry.find(f".//{MEDIA}thumbnail")
        entries.append(
            {
                "videoId": video_id,
                "title": title,
                "channelTitle": text(entry.find(f"{ATOM}author/{ATOM}name"), "Ressignificar Cada Dia"),
                "thumbnailUrl": thumbnail.get("url", "") if thumbnail is not None else "",
                "publishedAt": text(entry.find(f"{ATOM}published")),
                "isEmbeddable": True,
            },
        )
    return entries


def main() -> None:
    existing = json.loads(CATALOG_PATH.read_text(encoding="utf-8")) if CATALOG_PATH.exists() else {}
    merged = {item.get("videoId"): item for item in existing.get("videos", []) if item.get("videoId")}
    for entry in fetch_recent_entries():
        merged[entry["videoId"]] = {**merged.get(entry["videoId"], {}), **entry}
    videos = sorted(merged.values(), key=lambda item: item.get("publishedAt", ""), reverse=True)
    catalog = {
        "schemaVersion": 1,
        "updatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "videos": videos,
    }
    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
