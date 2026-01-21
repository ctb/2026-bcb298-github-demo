import sys
import polars as pl

df = pl.read_csv(sys.argv[1])
print("Percent identified:", df['f_unique_weighted'].sum()*100)
