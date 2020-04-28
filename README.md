[![PyPI version](https://badge.fury.io/py/cbench.svg)](https://badge.fury.io/py/cbench)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/cbench)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Linux/MacOS: [![Build Status](https://travis-ci.org/cknowledge/cbench.svg?branch=master)](https://travis-ci.org/cknowledge/cbench)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/yjq5myrrrkx3rydc?svg=true)](https://ci.appveyor.com/project/gfursin/cbench)

## Introduction

cBench is a cross-platform client connected with the 
[open cKnowledge.io portal](https://cKnowledge.io/results)
to support collaborative and reproducible benchmarking,
optimization and co-design of computational systems
based on emerging technologies (AI, ML, quantum, IoT).

cBench is a part of the [Collective Knowledge technology](https://cKnowledge.org) 
and a wrapper around the [low-level CK SDK](https://github.com/ctuning/ck)
to simplify the user experience.

## Platform support:

|               | As a host platform | As a target platform |
|---------------|:------------------:|:--------------------:|
| Generic Linux | ✓ | ✓ |
| Linux (Arm)   | ✓ | ✓ |
| Raspberry Pi  | ✓ | ✓ |
| MacOS         | ✓ | ± |
| Windows       | ✓ | ✓ |
| Android       | ± | ✓ |
| iOS           | TBD | TBD |

## MLPref crowd-benchmarking demo on Ubuntu

Install prerequisites:

```
sudo apt update
sudo apt install git wget libz-dev curl cmake
sudo apt install gcc g++ autoconf autogen libtool
sudo apt install libfreetype6-dev
sudo apt install python3.7-dev
sudo apt install -y libsm6 libxext6 libxrender-dev
```

Install cbrain:

```
python3 -m pip install cbrain
```

Initialize the [CK solution for MLPerf](https://cknowledge.io/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows):

```
cb init demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows
```

Participate in crowd-benchmarking:

```
cb benchmark demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows
```

See results on a public [SOTA dashboard](https://cknowledge.io/c/result/sota-mlperf-object-detection-v0.5-crowd-benchmarking).

You can also use the stable Docker image to participate in crowd-benchmarking:

```
sudo docker run ctuning/cbench-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows /bin/bash -c "cb benchmark demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows"
```

You can also check [all dependencies for this solution](https://cknowledge.io/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows/#dependencies).

## Documentation

* [Online docs for the Collective Knowledge technology](https://cKnowledge.io/docs)

## Feedback

* This is an ongoing project - don't hesitate to [contact us](https://cKnowledge.org/contacts.html) 
  if you have any feedback and suggestions!

## Acknowledgments

We would like to thank all [CK partners](https://cKnowledge.org/partners.html) 
for fruitful discussions and feedback!


*Copyright 2020 [cTuning foundation and cKnowledge SAS](https://cTuning.org)*
