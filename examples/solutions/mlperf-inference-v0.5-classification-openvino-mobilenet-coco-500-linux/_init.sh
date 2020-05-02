#! /bin/bash

export CK_REPOS=$PWD/CK
export CK_TOOLS=$PWD/CK-TOOLS

cb init mlperf-inference-v0.5-classification-openvino-mobilenet-coco-500-linux \
        --name="Object detection; MLPerf inference v0.5; OpenVINO; MobileNet v1 1.0 224; COCO; 500 images validation; Linux; benchmark; portable workflows" \
        --tags="validated,object-detection,mlperf,mlperf-inference,mlperf-inference-v0.5,openvino,mobilenet,mobilenet-v1,coco,500,benchmark,linux,portable-workflows" \
        --workflow_repo_url="local" \
        --workflow="program:mlperf-inference-v0.5" \
        --workflow_cmd_before="export NPROCS=\`grep -c processor /proc/cpuinfo\`" \
        --workflow_cmd="image-classification" \
        --workflow_cmd_extra="--repetitions=1 --no_state_check --skip_print_timers --env.CK_OPENVINO_MODEL_NAME=mobilenet --env.CK_LOADGEN_SCENARIO=Offline --env.CK_LOADGEN_MODE=Accuracy --env.CK_LOADGEN_DATASET_SIZE=500 --env.CK_OPENVINO_NTHREADS=\$NPROCS --env.CK_OPENVINO_NSTREAMS=\$NPROCS --env.CK_OPENVINO_NIREQ=\$NPROCS" \
        --workflow_output_dir="tmp" \
        --desc_prereq="$PWD/prereq.txt" \
        --desc_prepare="$PWD/prepare.txt" \
        --result_file="tmp/tmp-ck-timer.json" \
        --python_version_from="3.6" \
        --python_version_to="3.7.99" \
        --graph_convertor="$PWD/graph-convertor.json"
#        --update_meta_and_stop

