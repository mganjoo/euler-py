import argparse
import importlib
import pkg_resources
import time
from line_profiler import LineProfiler


class ResourceAccessor:

    def __init__(self, problem_num):
        self._problem_num = problem_num

    def resource_filename(self, basename):
        fullname = "data/p{:>03}_{}".format(self._problem_num, basename)
        return pkg_resources.resource_filename(__name__, fullname)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Execute Project Euler solution.")
    parser.add_argument("problem_number", metavar="N", type=int,
                        help="problem number")
    parser.add_argument("-p", "--profile", action='store_true',
                        help="whether to profile the solution")
    parser.add_argument("-t", "--test", action='store_true',
                        help="whether to use test cases and verify output")
    args = parser.parse_args()

    p = importlib.import_module("problem{:>03}".format(args.problem_number))
    resource_accessor = ResourceAccessor(args.problem_number)
    if args.test:
        args_list, expected_answers = zip(*p.test_cases(resource_accessor))
    else:
        args_list = [p.args(resource_accessor)]

    for i, problem_args in enumerate(args_list):
        if args.test:
            print("Running with test case #{}".format(i + 1))
        else:
            print("Running with problem arguments")

        if args.profile:
            profile = LineProfiler()
            wrapper = profile(p.solution)
            ans = wrapper(*problem_args)
            profile.print_stats()
        else:
            start_time = time.process_time()
            ans = p.solution(*problem_args)
            end_time = time.process_time()
            print("Total time: {}s".format(end_time - start_time))

        print("Answer: {}".format(ans))
        if args.test:
            assert ans == expected_answers[i], \
                "expected answer {}, got {}".format(expected_answers[i], ans)
