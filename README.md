# parquet-to-tsv
Convert Parquet files to TSV format

Use this simple command line script to convert Parquet files to TSV.
Should work on Linux and MacOS.

Dependencies:
- Python >=3
- pandas >=2
- pyarrow


Installation:
```bash
conda create -n parquet-to-tsv -c conda-forge pandas pyarrow
conda activate parquet-to-tsv

git clone https://github.com/jmtsuji/parquet-to-tsv.git
cd parquet-to-tsv
parquet-to-tsv.py -h # a help message should appear
```

Usage:
```bash
# Substitute the text in brackets with the path to your input file and the desired path to your output file
parquet-to-tsv.py -i [input_file.parquet] -o [output_file.tsv]
```
