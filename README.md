# parquet-to-tsv
Convert Parquet files to TSV format

Use this simple command line script to convert Parquet files to TSV.
Should work on Linux and MacOS.

### Dependencies:
- Python >=3
- pandas >=2
- pyarrow

### Installation:
If you use conda, you can set up the whole script as follows:
```bash
conda create -n parquet-to-tsv -c conda-forge pandas pyarrow
conda activate parquet-to-tsv

git clone https://github.com/jmtsuji/parquet-to-tsv.git
cd parquet-to-tsv
./parquet-to-tsv.py -h # a help message should appear
```

### Usage:
To convert a single parquet file to TSV format:
```bash
# Substitute the text in brackets with the path to your input file and the desired path to your output file
./parquet-to-tsv.py -i [input_file.parquet] -o [output_file.tsv]
```

To convert every .parquet file in a folder to TSV format:
```bash
# Run this command while you are inside the folder that contains parquet-to-tsv.py
# Set [my_folder_name] to the directory you want to search for parquet files
parquet_files=($(find [my_folder_name] -type f -name "*.parquet"))

for parquet_file in "${parquet_files}"; do
  echo "Converting file ${parquet_file}"
  ./parquet-to-tsv.py -i "${parquet_file}" -o "${parquet_file%.parquet}.tsv"
done
```
This will create a .tsv file in the same folder as each .parquet file with the same file name
(e.g., `my_folder/some_file.parquet` will be converted as `my_folder/some_file.tsv`).
The original `.parquet` files will all be kept, too.
