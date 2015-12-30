import argparse
import importlib
import time
from line_profiler import LineProfiler

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Execute Project Euler solution.")
    parser.add_argument("problem_number", metavar="N", type=int,
                        help="problem number")
    parser.add_argument("-p", "--profile", action='store_true',
                        help="whether to profile the solution")
    args = parser.parse_args()

    p = importlib.import_module("problem{:>03}".format(args.problem_number))
    problem_arguments = p.args()

    if args.profile:
        profile = LineProfiler()
        wrapper = profile(p.solution)
        ans = wrapper(*problem_arguments)
        profile.print_stats()
    else:
        start_time = time.process_time()
        ans = p.solution(*problem_arguments)
        end_time = time.process_time()
        print("Total time: {}s".format(end_time - start_time))

    print("Answer: {}".format(ans))
