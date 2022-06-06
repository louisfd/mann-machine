def assert_except(func, exception):
    try:
        func()
        assert False
    except exception:
        pass


def assert_list(func, the_list, positivity):
    for element in the_list:
        assert func(element) == positivity


def return_if(expected_input, rightful_output, wrong_output=None):
    return lambda inp: rightful_output if inp == expected_input else wrong_output
