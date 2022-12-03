# FASTA-Cleaner
Clean input FASTA file that contains Amino acid sequences with rare Amino acids as 'X, U'

### Hardware-requirements
- CPU: **4 cores** is the **recommended minimum** number of cores
- Memory: **4GB RAM** is the required **minimum memory** size
- Disk Storage: Max of **100 MB** that accounts for size of the code, input and output files

### Software requirements

The code is written in python. The following steps are needed to run it.
1.  Make sure that **conda** is installed, follow the following guide.
https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
2. Create a conda environment with python version 3.10:
conda create -n v_env python=3.10
3. Activate the conda environment and install dependencies
    - conda activate v_env``

### Usage 
```
python3 .\ModellerSeq.py -in Sample.fasta -out test_process.fasta
```
