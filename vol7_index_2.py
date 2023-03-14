from txtai.embeddings import Embeddings
embeddings = Embeddings({

    "path" :"sentence-transformers/all-MiniLM-L6-v2"

    })
embeddings.load("vol7_index_2")
import json
with open ("vol7.json", "r") as f:
    data = json.load(f)["descriptions"]
res = embeddings.search("knife", 10)
for r in res:
    print (f"Text: {data[r[0]]}")
    #can also find similarity using {r[1]}
    print()
