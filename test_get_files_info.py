from functions.get_files_info import get_files_info


def run_tests():

    test_case = [
    ("calculator","."),
    ("calculator","/bin"),
    ("calculator","../"),
    ("calculator","main.py")
]

    for work_dir, dir in test_case:
        print(get_files_info(work_dir, dir))


if __name__ == "__main__":
    run_tests()