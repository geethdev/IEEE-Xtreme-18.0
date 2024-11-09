import csv
import sys
from collections import defaultdict

data = []
for line in sys.stdin:
    data.append(next(csv.reader([line.strip()])))

parent_events = {}
child_events = defaultdict(list)
for record in data:
    event_id, title, acronym, proj_code, proj_3d_code, record_type = record
    if not acronym:
        continue
    
    if record_type == "Parent Event":
        parent_events[event_id] = {
            "title": title,
            "acronym": acronym,
            "proj_code": proj_code,
            "proj_3d_code": proj_3d_code,
            "children": []
        }
    elif record_type == "IEEE Event":
        child_events[acronym].append({
            "event_id": event_id,
            "title": title,
            "proj_code": proj_code,
            "proj_3d_code": proj_3d_code,
            "parent_id": None 
        })

output_events = []
for acronym, children in child_events.items():
    parent = None
    parent_candidates = [p for p in parent_events.values() if p["acronym"] == acronym]
    
    if len(parent_candidates) == 1:
        parent = parent_candidates[0]
        parent_id = list(parent_events.keys())[list(parent_events.values()).index(parent)]
        
        unique_3d_codes = {child["proj_3d_code"] for child in children}
        parent["proj_3d_code"] = "???" if len(unique_3d_codes) > 1 else unique_3d_codes.pop()
        
        for child in children:
            child["parent_id"] = parent_id
            parent["children"].append(child)
        
        if parent["children"]:
            output_events.append((parent, sorted(parent["children"], key=lambda x: (x["title"], x["event_id"]))))

output_events.sort(key=lambda x: x[0]["acronym"])
for parent, children in output_events:
    print(f'{list(parent_events.keys())[list(parent_events.values()).index(parent)]},"{parent["title"]}","{parent["acronym"]}",,{parent["proj_3d_code"]},"Parent Event"')
    for child in children:
        print(f'{child["event_id"]},"{child["title"]}","{parent["acronym"]}",{child["proj_code"]},{child["proj_3d_code"]},"IEEE Event",{child["parent_id"]}')