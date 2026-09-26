"""Run against a deployed RPC to collect gas/latency records.
No network or private key is required for the simulation pipeline."""
import argparse,csv,json,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument("--rpc",required=True);p.add_argument("--out",default="gas_report.csv");a=p.parse_args()
try:
 from web3 import Web3
except ImportError: raise SystemExit("Install web3 to collect live blockchain measurements.")
w3=Web3(Web3.HTTPProvider(a.rpc)); start=time.perf_counter(); block=w3.eth.block_number; latency=time.perf_counter()-start
Path(a.out).write_text("operation,gas_used,latency_seconds\nblock_number,0,%s\n"%latency)
print(json.dumps({"connected":w3.is_connected(),"block":block,"latency_seconds":latency}))
