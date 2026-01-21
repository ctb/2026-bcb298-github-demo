import sys
import polars as pl

df = pl.read_csv(sys.argv[1])
print("Fraction identified:", round(df['f_unique_weighted'].sum(), 2))
