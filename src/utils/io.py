from pathlib import Path
import pandas as pd

def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

def read_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    return pd.read_csv(path, **kwargs)

def to_csv(df: pd.DataFrame, path: str | Path, index: bool = False):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index)
