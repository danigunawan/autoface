import tensorflow as tf
from align import detect_face
import cv2
import imutils
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--imgpath", type = str, required=True)
args = parser.parse_args()

# some constants kept as default from facenet
minsize = 20
threshold = [0.6, 0.7, 0.7]
factor = 0.709
margin = 44
input_image_size = 160

sess = tf.Session()
# read pnet, rnet, onet models from align directory and files are det1.npy, det2.npy, det3.npy
pnet, rnet, onet = detect_face.create_mtcnn(sess, None)

def getFace(img):
    faces = []
    img_size = np.asarray(img.shape)[0:2]
    bounding_boxes, _ = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
    if not len(bounding_boxes) == 0:
        for face in bounding_boxes:
            if face[4] > 0.50:
                det = np.squeeze(face[0:4])
                bb = np.zeros(4, dtype=np.int32)
                bb[0] = np.maximum(det[0] - margin / 2, 0)
                bb[1] = np.maximum(det[1] - margin / 2, 0)
                bb[2] = np.minimum(det[2] + margin / 2, img_size[1])
                bb[3] = np.minimum(det[3] + margin / 2, img_size[0])
                cropped = img[bb[1]:bb[3], bb[0]:bb[2], :]
                resized = cv2.resize(cropped, (input_image_size,input_image_size),interpolation=cv2.INTER_AREA)
                faces.append({'face':resized,'rect':[bb[0],bb[1],bb[2],bb[3]]})
    return faces

for f in os.listdir(args.imgpath):
    if f == '.' or f == '..':
        continue

    img = cv2.imread(os.path.join(args.imgpath, f))
    img = imutils.resize(img,width=1000)
    faces = getFace(img)
    rets = []
    for face in faces:
        x1 = face['rect'][0]
        y1 = face['rect'][1]
        x2 = face['rect'][2]
        y2 = face['rect'][3]  
        #cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        croped = img[y1:y2, x1:x2]
        rets.append(croped)

    for i, img in enumerate(rets):
        img = imutils.resize(img,width=250)
        cv2.imwrite('%d_%s'% (i,f), img)
        #cv2.imshow("faces", img)

    #cv2.waitKey(0)
    cv2.destroyAllWindows()