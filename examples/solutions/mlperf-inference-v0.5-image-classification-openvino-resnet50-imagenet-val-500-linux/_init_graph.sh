#! /bin/bash

cbench init-graph mlperf-inference-v0.5-classification --version=1.0.0 --desc_file="$PWD/graph-desc.json" \
       --name="MLPerf Inference v0.5 - Image Classification - crowd-benchmarking" \
       --tags="benchmarking,reproducible-benchmarking,crowd-benchmarking,reproduced-results,mlperf,mlperf-inference,mlperf-inference-v0.5"
