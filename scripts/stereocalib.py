import cv2
import numpy as np
import yaml
import sys


def stereocalib(side, img):

    with open("stereocalibfinal.yaml", 'r') as stream:
        try:
            ster = yaml.load(stream)
            #print(poop)
            
        except yaml.YAMLError as exc:
            print(exc)
    mtx_ll = np.asarray(ster['mtx_ll'])
    dist_ll = np.asarray(ster['dist_ll'])
    mtx_rr = np.asarray(ster['mtx_rr'])
    dist_rr = np.asarray(ster['dist_rr'])
    w_l = ster['w_l']
    h_l = ster['h_l']

    with open("stereorectifyfinal.yaml", 'r') as stream:
        try:
            rect = yaml.load(stream)
            
        except yaml.YAMLError as exc:
            print(exc)
    R1 = np.asarray(rect['R1'])
    P1 = np.asarray(rect['P1'])
    R2 = np.asarray(rect['R2'])
    P2 = np.asarray(rect['P2'])

    if side == 'left':
        
            mapLx, mapLy = cv2.initUndistortRectifyMap(mtx_ll, dist_ll, R1, P1, (w_l, h_l), m1type = cv2.CV_32FC1)
            finall = cv2.remap(img, mapLx, mapLy,interpolation = cv2.INTER_LINEAR)
            return finall
        
    elif side == 'right':
        
            mapRx, mapRy = cv2.initUndistortRectifyMap(mtx_rr, dist_rr, R2, P2, (w_l, h_l), m1type = cv2.CV_32FC1)#CV_16SC2,CV_32FC1
            finalr = cv2.remap(img, mapRx, mapRy,interpolation = cv2.INTER_LINEAR)
            return finalr

if __name__ == '__main__':
    argside = 0
    argimg = 0
    if len(sys.argv) > 1:
        #argside, argimg = sys.argv[1:2]
        argimg = sys.argv[1]
        argside = sys.argv[2]
        print len(sys.argv)
        stereocalib(argside, argimg)