# Finally block always execute even if an exception is raised

# Example 1: No exception happens
def demo1():
    try:
        print("Inside try block")
        x = 10 / 2
    except ZeroDivisionError:
        print("This will not run")
    finally:
        print("Finally block executed")

demo1()

# Explanation:

# try runs successfully.
# No exception → except is skipped.
# finally always runs → prints message.

# Example 2: Exception happens and is handled

def demo2():
    try:
        print("Inside try block")
        x = 10 / 0  # ZeroDivisionError
    except ZeroDivisionError:
        print("Exception handled inside except block")
    finally:
        print("Finally block executed")

demo2()


# Explanation:

# try raises ZeroDivisionError.
# except ZeroDivisionError catches it.
# After except, the finally block still executes.