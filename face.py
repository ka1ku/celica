from facenet_pytorch import MTCNN
from PIL import Image
import torch
import torchvision.transforms as transforms
from facenet_pytorch import InceptionResnetV1
from sklearn.metrics.pairwise import cosine_similarity

transform = transforms.ToPILImage()
mtcnn = MTCNN(image_size=224, keep_all=False)

id_face = mtcnn(Image.open("ben_id2.jpg"))
selfie_face = mtcnn(Image.open("ben_id.jpg"))

id_face_pil = transform(id_face)
id_selfie_face_pil = transform(selfie_face)

id_face_pil.show()
id_selfie_face_pil.show()


model = InceptionResnetV1(pretrained="vggface2").eval()

with torch.no_grad():
    emb1 = model(id_face.unsqueeze(0))
    emb2 = model(selfie_face.unsqueeze(0))
  
    
vec1 = emb1 / emb1.norm(dim=1, keepdim=True)
vec2 = emb2 / emb2.norm(dim=1, keepdim=True)

sim = cosine_similarity(vec1.cpu(), vec2.cpu())[0][0]
print(f"Cosine similarity: {sim:.4f}")

if sim > 0.8:
    print("Almost definitely the same person")
elif sim > 0.6:
    print("Probably the same person")
elif sim > 0.4:
    print("Unsure")
else:
    print("Not the same person")