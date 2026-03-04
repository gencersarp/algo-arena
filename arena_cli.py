import argparse
import os
import subprocess
import time
import sys

def init_problem(args):
    os.makedirs(args.name, exist_ok=True)
    with open(os.path.join(args.name, 'solution.c'), 'w') as f:
        f.write("#include <stdio.h>\n\nint main() {\n    // Write your optimized solution here\n    return 0;\n}\n")
    with open(os.path.join(args.name, 'input.txt'), 'w') as f:
        f.write("")
    with open(os.path.join(args.name, 'expected.txt'), 'w') as f:
        f.write("")
    print(f"[*] Initialized problem environment '{args.name}' with C template and test cases.")

def run_problem(args):
    prob_dir = args.name
    c_file = os.path.join(prob_dir, 'solution.c')
    in_file = os.path.join(prob_dir, 'input.txt')
    exp_file = os.path.join(prob_dir, 'expected.txt')
    exec_file = os.path.join(prob_dir, 'solution.out')

    if not os.path.exists(c_file):
        print(f"[!] Error: {c_file} not found.")
        sys.exit(1)

    print("[*] Compiling with gcc -O3 optimizations...")
    comp = subprocess.run(["gcc", "-O3", c_file, "-o", exec_file], capture_output=True, text=True)
    if comp.returncode != 0:
        print("[!] Compilation Failed:\n" + comp.stderr)
        sys.exit(1)

    if not os.path.exists(in_file):
        print(f"[!] Error: {in_file} is missing. Please create it or run 'arena init' again.")
        sys.exit(1)

    print("[*] Running test cases...")
    start_time = time.time()
    with open(in_file, 'r') as f_in:
        run_proc = subprocess.run([exec_file], stdin=f_in, capture_output=True, text=True)
    elapsed = (time.time() - start_time) * 1000

    if run_proc.returncode != 0:
        print(f"[!] Execution Failed or Crashed (Return Code: {run_proc.returncode}).")
        print(run_proc.stderr)
        sys.exit(1)

    output = run_proc.stdout.strip()
    expected = ""
    if os.path.exists(exp_file):
        with open(exp_file, 'r') as f_exp:
            expected = f_exp.read().strip()

    print("-" * 40)
    print(f"Execution Time : {elapsed:.3f} ms")
    if expected:
        if output == expected:
            print("Result         : [PASS] \u2705")
        else:
            print("Result         : [FAIL] \u274c")
            print("\n--- Expected ---")
            print(expected)
            print("\n--- Got --------")
            print(output)
    else:
        print("\n--- Output ---")
        print(output if output else "(No output)")
    print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description="Algo-Arena: Competitive Programming Local Benchmarking CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_init = subparsers.add_parser("init", help="Initialize a new problem environment")
    parser_init.add_argument("name", help="Name of the problem/directory")

    parser_run = subparsers.add_parser("run", help="Compile (with -O3), run, and benchmark a problem")
    parser_run.add_argument("name", help="Name of the problem/directory to run")

    args = parser.parse_args()
    if args.command == "init":
        init_problem(args)
    elif args.command == "run":
        run_problem(args)

if __name__ == "__main__":
    main()
