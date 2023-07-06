from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from yacs.config import CfgNode as CN


_C = CN()

# ----- BASIC SETTINGS -----
_C.NAME = "default"
_C.OUTPUT_DIR = "/home/VQAMed/output"
_C.RESULTS_DIR = "/home/VQAMed/output"
_C.PIN_MEMORY = True
_C.COLOR_SPACE = "RGB"
_C.RESUME_MODEL = ""
_C.RESUME_MODE = "all"
_C.CPU_MODE = False
_C.SHOW_STEP = 50
_C.INPUT_SIZE = (224, 224)
_C.EVAL_MODE = False

# ----- DATASET BUILDER -----
_C.DATASET = CN()
_C.DATASET.DATASET = "RAD"
_C.DATASET.DATA_DIR = "./data"
_C.DATASET.DATA_TYPE = "jpg"
_C.DATASET.TRAIN_JSON = ""
_C.DATASET.VALID_JSON = ""

# ----- LOSS BUILDER -----
_C.LOSS = CN()
_C.LOSS.LOSS_TYPE = "CrossEntropy"

# ----- TRAIN BUILDER -----
_C.TRAIN = CN()
_C.TRAIN.MAX_SEQ_LENGTH = 32
_C.TRAIN.BATCH_SIZE = 32
_C.TRAIN.N_EPOCH = 60
_C.TRAIN.SHUFFLE = True
_C.TRAIN.NUM_WORKERS = 8
_C.TRAIN.RESUME = False
_C.TRAIN.INPUT_SNAPSHOT = ""
_C.TRAIN.VISION_ENCODER = "ViT-B/32"

# ----- OPTIMIZER -----
_C.TRAIN.OPTIMIZER = CN()
_C.TRAIN.OPTIMIZER.TYPE = "SGD"
_C.TRAIN.OPTIMIZER.BASE_LR = 0.1
_C.TRAIN.OPTIMIZER.MOMENTUM_CNN = 0.9
_C.TRAIN.OPTIMIZER.EPS = 0.9
_C.TRAIN.OPTIMIZER.WEIGHT_DECAY = 4e-4

# ----- TRANSFORM
_C.TRANSFORMS = CN()
_C.TRANSFORMS.TRAIN_TRANSFORMS = ("random_resized_crop", "random_horizontal_flip")
_C.TRANSFORMS.TEST_TRANSFORMS = ("shorter_resize_for_crop", "center_crop")
_C.TRANSFORMS.PROCESS_DETAIL = CN()
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_CROP = CN()
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_CROP.PADDING = 4
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_RESIZED_CROP = CN()
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_RESIZED_CROP.SCALE = (0.08, 1.0)
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_RESIZED_CROP.RATIO = (0.75, 1.333333333)

# ----- TEST
_C.TEST = CN()
_C.TEST.BATCH_SIZE = 32
_C.TEST.NUM_WORKERS = 8


def update_config(cfg, args):
    cfg.defrost()
    cfg.merge_from_file(args.cfg)

    cfg.freeze()
