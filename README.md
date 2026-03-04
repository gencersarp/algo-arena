# Algo-Arena CLI

An end-to-end CLI product designed for competitive programming and algorithm benchmarking. Given your focus on low-level C optimization and fast execution, this tool automates the tedious parts: rapidly bootstrapping problem environments, compiling C code with `-O3` optimizations, piping test inputs, verifying outputs against expected results, and accurately measuring execution time down to the millisecond.

## Installation

You can install this product globally on your machine so that the `arena` command is available everywhere:

```bash
git clone https://github.com/gencersarp/algo-arena.git
cd algo-arena
pip install -e .
```

## Usage

### 1. Initialize a Problem
Set up a new environment. This automatically creates a directory with a highly-optimized C template (`solution.c`), an `input.txt` file, and an `expected.txt` file.

```bash
arena init twosum
```

### 2. Write your code and tests
1. Edit `twosum/solution.c` with your algorithm.
2. Paste the problem's input into `twosum/input.txt`.
3. Paste the correct expected output into `twosum/expected.txt`.

### 3. Run and Benchmark
The CLI will compile the file with GCC (`-O3`), feed it the input, diff the output, and display an execution report.

```bash
arena run twosum
```

### Example Output
```text
[*] Compiling with gcc -O3 optimizations...
[*] Running test cases...
----------------------------------------
Execution Time : 1.245 ms
Result         : [PASS] ✅
----------------------------------------
```
