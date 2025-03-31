import cv2
from skimage.metrics import structural_similarity as compare_ssim

def ImageComparer(Image1, Image2):
    # Load the images
    img = cv2.imread(Image1)
    img_2 = cv2.imread(Image2)
    size1 = img.shape
    size2 = img_2.shape

    if size1 != size2:
        return 0

    # Split the images into R, G, B channels
    r1, g1, b1 = cv2.split(img)
    r2, g2, b2 = cv2.split(img_2)

    # Compute SSIM for each channel
    ssim_r = compare_ssim(r1, r2)
    ssim_g = compare_ssim(g1, g2)
    ssim_b = compare_ssim(b1, b2)

    # Average the SSIM for all channels
    ssim_mean = (ssim_r + ssim_g + ssim_b) / 3
    
    #print(f"Average SSIM (RGB): {ssim_mean}")
    return ssim_mean
