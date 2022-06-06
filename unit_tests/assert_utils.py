def assert_except(func, exception):
    try:
        func()
        assert False
    except exception:
        pass


def assert_list(func, the_list, positivity):
    for element in the_list:
        assert func(element) == positivity
