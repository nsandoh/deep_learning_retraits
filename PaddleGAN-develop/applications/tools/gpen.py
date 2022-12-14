#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

sys.path.append(".")
import argparse
import paddle
from ppgan.apps import GPENPredictor

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_path",
                        type=str,
                        default='output_dir',
                        help="path to output image dir")

    parser.add_argument("--weight_path",
                        type=str,
                        default=None,
                        help="path to model checkpoint path")

    parser.add_argument("--test_img",
                        type=str,
                        default='data/gpen/lite_data/15006.png',
                        help="path of test image")

    parser.add_argument("--model_type",
                        type=str,
                        default=None,
                        help="type of model for loading pretrained model")

    parser.add_argument("--seed",
                        type=int,
                        default=None,
                        help="sample random seed for model's image generation")

    parser.add_argument("--size",
                        type=int,
                        default=256,
                        help="resolution of output image")

    parser.add_argument("--style_dim",
                        type=int,
                        default=512,
                        help="number of style dimension")

    parser.add_argument("--n_mlp",
                        type=int,
                        default=8,
                        help="number of mlp layer depth")

    parser.add_argument("--channel_multiplier",
                        type=int,
                        default=1,
                        help="number of channel multiplier")

    parser.add_argument("--narrow",
                        type=float,
                        default=0.5,
                        help="number of channel narrow")

    parser.add_argument("--cpu",
                        dest="cpu",
                        action="store_true",
                        help="cpu mode.")

    args = parser.parse_args()

    if args.cpu:
        paddle.set_device('cpu')

    predictor = GPENPredictor(output_path=args.output_path,
                              weight_path=args.weight_path,
                              model_type=args.model_type,
                              seed=args.seed,
                              size=args.size,
                              style_dim=args.style_dim,
                              n_mlp=args.n_mlp,
                              narrow=args.narrow,
                              channel_multiplier=args.channel_multiplier)
    predictor.run(args.test_img)
