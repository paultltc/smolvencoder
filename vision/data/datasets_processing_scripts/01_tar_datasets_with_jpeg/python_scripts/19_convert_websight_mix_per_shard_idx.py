import argparse
import logging
from pathlib import Path

from datasets import set_caching_enabled

from m4.training.types import DatasetTypes
from m4.utils.datasets.create_webdataset_tar import export_dataset_all_shard_idx_to_tar


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

set_caching_enabled(False)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ds_path", type=Path, required=True)
    parser.add_argument("--saving_dir", type=Path, required=True)
    parser.add_argument("--num_examples_per_shard", type=int)
    parser.add_argument("--s3_uri", type=str)
    parser.add_argument("--num_proc", type=int, required=True)
    parser.add_argument("--min_num_shards", type=int)
    parser.add_argument("--save_shard_prefix", type=str, default="")

    args = parser.parse_args()
    return args


def main(args):
    ds_paths = [args.ds_path]
    ds_type = DatasetTypes.IMAGE_CAPTION_PAIRS

    export_dataset_all_shard_idx_to_tar(
        hf_datasets_paths=ds_paths,
        saving_dir=args.saving_dir,
        ds_type=ds_type,
        num_examples_per_shard=args.num_examples_per_shard,
        s3_uri=args.s3_uri,
        num_proc=args.num_proc,
        min_num_shards=args.min_num_shards,
        save_shard_prefix=args.save_shard_prefix,
    )


if __name__ == "__main__":
    args = get_args()
    main(args)
