from arqf.config import ExperimentConfig
from arqf.experiment import run
def test_experiment_creates_artifacts(tmp_path):
    out=tmp_path/'test1'; run(ExperimentConfig(participants=30,projects=5,seeds=2),out)
    assert all((out/x).exists() for x in ('results.csv','summary.csv','metadata.json'))
