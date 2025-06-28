import argparse

parser = argparse.ArgumentParser()
parser.add_argument(    '--name', type=str, help='你的名字', required=True)
args = parser.parse_args()

print(f"你好，{args.name}！ 很高興見到你!")