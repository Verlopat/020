import argparse,json
from pathlib import Path
from .config import ExperimentConfig
from .experiment import run
def next_output(root='output'):
    root=Path(root); root.mkdir(exist_ok=True)
    nums=[int(p.name[4:]) for p in root.glob('test*') if p.name[4:].isdigit()]
    return root/f'test{max(nums,default=0)+1}'
def main():
    p=argparse.ArgumentParser(description='Adaptive Randomized Quadratic Funding experiment runner')
    p.add_argument('--participants',type=int,default=500); p.add_argument('--projects',type=int,default=20)
    p.add_argument('--seeds',type=int,default=20); p.add_argument('--matching-pool',type=float,default=100000)
    p.add_argument('--output-root',default='output'); a=p.parse_args()
    out=next_output(a.output_root); run(ExperimentConfig(a.participants,a.projects,a.matching_pool,a.seeds),out)
    print(json.dumps({'status':'complete','output':str(out)},indent=2))
