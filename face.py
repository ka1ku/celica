import insightface
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity
import cv2
import logging

logging.basicConfig(level=logging.ERROR)

app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=-1, det_size=(640, 640))

img1 = cv2.imread("photos/ben_id5.jpg")
img2 = cv2.imread("photos/ben_id6.jpg")

faces1 = app.get(img1)
faces2 = app.get(img2)

assert faces1 and faces2, "Face not detected in one or both images."

emb1 = faces1[0].embedding
emb2 = faces2[0].embedding

sim = cosine_similarity([emb1], [emb2])[0][0]
print(f"Similarity score: {sim:.4f}")

if sim > 0.45:
  print("same")
else:
  print("diff")
