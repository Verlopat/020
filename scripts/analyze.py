import argparse
from arqf.analysis import summarize_csv,make_figures
p=argparse.ArgumentParser();p.add_argument("results");p.add_argument("outdir");a=p.parse_args()
summarize_csv(a.results,a.outdir);print(make_figures(a.results,a.outdir))
