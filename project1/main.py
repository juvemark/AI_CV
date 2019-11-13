import cv2
import utils
import sys

if __name__ == '__main__':

    if sys.argv[1] and sys.argv[2]:
        image1, image2 = cv2.imread(sys.argv[1]), cv2.imread(sys.argv[2])
        stitch_match = utils.FindKeyPpointsAndMatching()
        kp1, kp2 = stitch_match.get_key_points(image1, image2)
        homo_matrix = stitch_match.match(kp1, kp2)
        merge_image = stitch_match.stitch_merge(image1, image2, homo_matrix)
        cv2.namedWindow('output', 0)
        cv2.imshow('output', merge_image)
        if cv2.waitKey() == 27:
            cv2.destroyAllWindows()
        cv2.imwrite(sys.argv[1].split('.')[0] + '-output.JPG', merge_image)
    else:
        print('Check input path.')