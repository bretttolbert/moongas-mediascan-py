import json
from typing import Set

from mediascan.artists_loader import load_artists_yaml


regions_code_name_map_json_path = "../../../mediaserver/app/static/json_data/region_code_name_map.json"
artists_yaml_path = "../../out/artists.yaml"
artists = load_artists_yaml(artists_yaml_path)

with open(regions_code_name_map_json_path) as f:
    missing: Set[str] = set()
    code_name_map = json.loads(f.read())
    for a in artists.artists:
        if a.artist_data.region_code not in code_name_map:
            missing.add(a.artist_data.region_code)
    if len(missing):
        for code in missing:
            print(code)
    else:
        print("No codes missing")
