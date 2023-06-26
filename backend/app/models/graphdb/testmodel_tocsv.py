import csv

nodes = [
    {"id": "w1", "name": "run", "metadata": {"language": "en"}, "label": "word"},
    {"id": "w2", "name": "manage", "metadata": {"language": "en"}, "label": "word"},
    {"id": "p1", "name": "I run the store", "label": "phrase"},
    {"id": "p2", "name": "I run to the store", "label": "phrase"},
]

edges = [
    {"source": "w1", "target": "p1", "relationship": "is_in"},
    {"source": "w1", "target": "p2", "relationship": "is_in"},
]

filename = "graph.csv"

with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["id:ID", "name", "metadata", ":LABEL", ":START_ID", ":END_ID", ":TYPE"]
    )  # Write header row

    for node in nodes:
        row = [
            node["id"],
            node["name"],
            node.get("metadata", {}),
            node.get("label", ""),
            "",
            "",
            "",
        ]
        writer.writerow(row)

    for edge in edges:
        row = ["", "", "", "", edge["source"], edge["target"], edge["relationship"]]
        writer.writerow(row)
