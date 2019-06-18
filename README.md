### Testing environment for pentavium
- Original source file: **pentavium_stream.py**
- Benchmark source file 1: **proj.py**
- Benchmark source file 2: **cavium.py**

## Testing process
- Make _assess_ file executable `chmod +x assess'
- Execute _assess_ with required sequence length
- Select corresponding input file
- Apply necessary statistical test
- Results are stored in _experiments/AlgorithmTesting/finalAnalysisReport.txt
- Check corresponding **p-values** with thresholds for various statistical test to assign pass/fail
