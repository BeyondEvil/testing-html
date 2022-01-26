#import pytest
from pytest_html import extras


def test_url(extra):
    """
        bla bla bla bla
        alb alb alb
        @param: hello
        :param just
    """
    # driver.get("https://www.google.com")
    extra.append(extras.text("some string"))
    extra.append(extras.image("file:///Users/jimbrannlund/dev/pytest-dev/testing-html/screenshot.png"))
    extra.append(extras.image("file:///Users/jimbrannlund/dev/pytest-dev/testing-html/screenshot.png"))
    assert False


def test_url2():
    """
        bla bla bla bla
        alb alb alb
        @param: hello
        :param just
    """
    # driver.get("https://www.google.com")
    assert True


# def test_url3(driver, extra):
#     """
#         bla bla bla bla
#         alb alb alb
#         @param: hello
#         :param just
#     """
#     driver.get("https://www.google.com")
#     driver.get_screenshot_as_file("screenshot.png")
#     extra.append(extras.png("screenshot.png"))
#     assert True
