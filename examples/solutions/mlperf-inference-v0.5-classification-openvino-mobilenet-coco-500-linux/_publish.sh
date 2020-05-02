#! /bin/bash

export CK_REPOS=$PWD/CK
export CK_TOOLS=$PWD/CK-TOOLS

cb setup
cb publish solution:mlperf-inference-v0.5-classification-openvino-mobilenet-coco-500-linux --force
