from platform import python_version
print(python_version())
from txtai.embeddings import Embeddings
import json
embeddings  = Embeddings({
    
    "path": "sentence-transformers/all-MiniLM-L6-v2"
})
with open ("vol7.json", "r") as f:
    data = json.load(f)["descriptions"]
len(data)
data[0]
txtai_data = []
i=0
for text in data:
    txtai_data.append((i, text, None))
    i=i+1
print(txtai_data[0])
embeddings.index(txtai_data)
res = embeddings.search("knife", 10)
for r in res:
    print (f"Text: {data[r[0]]}")
    #can also find similarity using {r[1]}
    print()
embeddings.save("vol7_index_2")
    

    
    
