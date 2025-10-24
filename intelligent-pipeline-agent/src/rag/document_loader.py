
import os, glob
def load_markdown(d): 
    res=[]
    for fp in glob.glob(os.path.join(d,"*.md")):
        res.append({"path":fp,"text":open(fp,'r',encoding='utf-8').read()})
    return res
def chunk_text(t, size=800, overlap=100):
    out=[]; i=0
    while i < len(t):
        out.append(t[i:i+size]); i += size-overlap
    return out
