# BASIC SYNTAX
# try:
#     # Code that might raise an exception
#     risky_code()
# except ExceptionType:
#     # Code to handle the exception
#     handle_exception()
# else:
#     # Code to execute if no exception was raised
#     execute_if_successful()
# finally:
#     # Code to execute no matter what (optional)
#     cleanup_code()


class Solution(object):
    def test(self, nums):
        return nums

def main():
    sol = Solution()
    sol.test([1,2,3])

    try:
        num = 0
        result = 100 / num
        print(result)
    except ZeroDivisionError:
        print("You cannot divide by 0")
    finally:
        print(f"Code has been executed with num: {num}")

if __name__ == "__main__":
    main()