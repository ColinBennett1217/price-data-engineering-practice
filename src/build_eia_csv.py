

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
EIA_DIR = DATA_DIR / "us_eia"
OUTPUT_DIR = DATA_DIR / "csv_cleaned"
OUTPUT_DIR.mkdir(exist_ok=True)


def flatten_header(raw_df: pd.DataFrame, top_row: int = 10, bottom_row: int = 11) -> list[str]:
    header_top = raw_df.iloc[top_row].fillna("")
    header_bottom = raw_df.iloc[bottom_row].fillna("")

    cols = []
    for top, bottom in zip(header_top, header_bottom):
        top = str(top).strip()
        bottom = str(bottom).strip()

        if top and bottom:
            col = f"{top} {bottom}"
        elif top:
            col = top
        else:
            col = bottom

        cols.append(col)

    return cols


def build_clean_table(
    xlsx_path: Path,
    data_start_row: int = 13,
    top_row: int = 10,
    bottom_row: int = 11,
) -> pd.DataFrame:
    raw = pd.read_excel(xlsx_path, header=None)

    cols = flatten_header(raw, top_row=top_row, bottom_row=bottom_row)

    df = raw.iloc[data_start_row:].copy()
    df.columns = cols

    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all").reset_index(drop=True)

    df = df.replace({
        "*": pd.NA,
        "Q": pd.NA,
        "W": pd.NA,
        "--": pd.NA,
        "": pd.NA,
    })

    return df


def save_clean_csv(xlsx_path: Path) -> Path:
    df = build_clean_table(xlsx_path)
    out_path = OUTPUT_DIR / f"{xlsx_path.stem}.csv"
    df.to_csv(out_path, index=False)
    return out_path


def build_all_eia_csvs() -> None:
    for xlsx_path in sorted(EIA_DIR.glob("Table*.xlsx")):
        print(f"Processing {xlsx_path.name}...")
        out_path = save_clean_csv(xlsx_path)
        print(f"Saved: {out_path}")


if __name__ == "__main__":
    build_all_eia_csvs()