import numpy as np

WIDTH = 7768
HEIGHT = 3884
RESIZE_W = 2048
RESIZE_H = 1024

SIZE_CROP = 1024
CROP_DISTRIB_MU = 0.4
CROP_DISTRIB_SIGMA = 0.2
LIGHT_N = 3
device = "cuda:0"
BATCH_SIZE = 24

# WIDTH = 2048
# HEIGHT = 1024

GAUSSIAN_KERNEL_SIZE = 35
THRESH_GAUSSIAN_KERNEL_SIZE = 5


data_home_dir = "/media/winter/_hdd/LavalHDRDataset/"
# data_home_dir = "/home/winter/LEDataset/"
hdr_dataset_dir = data_home_dir+"IndoorHDRDataset2018/"
hdr_dataset_hdrformat_dir = data_home_dir+"IndoorHDRDataset2018/HDRFormat/"
light_param_file = data_home_dir+"HDR_results/light_param.txt"
light_sg_renderings_dir = data_home_dir+"HDR_results/light_sg_renderings/"
light_masks_dir_old = data_home_dir+"HDR_results/light_masks/"
light_masks_dir = data_home_dir+"HDR_results/light_semantic_maps/"
fusion_hdr_jpgs_dir = data_home_dir+"HDR_results/fusion_hdr_jpgs/"
ldr_dir = data_home_dir+"HDR_results/ldr_conversions/"
depth_files_dir = data_home_dir+'HDR_DepthFile/'
cropped_imgs_dir =data_home_dir+'CroppedImgs/'
cropped_imgs_dir_partial =data_home_dir+'CroppedImgs_partial/'
warped_exr_dir =data_home_dir+'WarpedEXR/'
resized_warped_exr_dir =data_home_dir+'ResizedWarpedEXR/'
warped_exr_jpg_dir =data_home_dir+'WarpedEXRJPG/'
cropped_param_file = data_home_dir+"HDR_results/cropped_light_param.txt"
modelsaving_dir = '/home/winter/code/Gardner2019/modelsavings/'

# for seg dataset
seg_dataset_dir = data_home_dir+"SegDataset/"
ldr_imgs = seg_dataset_dir+"ldr_imgs/"
seg_labels = seg_dataset_dir+"seg_labels/"
