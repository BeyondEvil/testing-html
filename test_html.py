import pytest
from pytest_html import extras
from time import sleep
import logging
from pic_b64 import PIC_AS_BASE64
from selenium import webdriver

# pytest.skip("skip marker module", allow_module_level=True)


# def test_driver_screenshot():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--window-size=1920x1080")
#     driver = webdriver.Remote(
#         command_executor="http://127.0.0.1:4444", options=chrome_options
#     )
#     try:
#         driver.get("https://www.duckduckgo.com")
#         result = driver.get_screenshot_as_base64()
#         print(result)
#     finally:
#         driver.quit()

# def test_driver_screenshot(driver):
#     driver.get("https://www.duckduckgo.com")
#     assert False


# @pytest.mark.flaky(reruns=2)
def test_url(extra):
    """
        bla bla bla bla
        alb alb alb
        @param: hello
        :param just
    """
    # driver.get("https://www.google.com")
    extra.append(extras.text("some string"))
    # extra.append(extras.text(b"\xe2\x80\x94"))
    # extra.append(extras.text("—"))
    # extra.append(extras.html("<div>Additional HTML</div>"))
    extra.append(extras.url("https://example.com"))
    extra.append(extras.json({"hello": "world"}))

    # link (do nothing)
    extra.append(extras.image("https://www.dailydot.com/wp-content/uploads/2018/05/Spiderman-Games.jpg"))
    extra.append(extras.video("vid.mp4"))
    # relative (copy to assets / base64)
    extra.append(extras.image("screenshot1.png"))

    extra.append(extras.html(r"<div>Additional HTML</div>"))
    extra.append(extras.html(r"<div>Second HTML</div>"))

    # absolute (copy to assets / base64)
    extra.append(extras.image("file:///Users/jimbrannlund/dev/pytest/testing-html/screenshot2.png"))

    # base 64
    extra.append(extras.image(PIC_AS_BASE64))
    sleep(0.2)
    assert False


def test_url_2(extra):
    extra.append(extras.image("https://www.dailydot.com/wp-content/uploads/2018/05/Spiderman-Games.jpg"))
    sleep(0.3)
    assert True


def test_pass(extra):
    """
        bla bla bla bla
        alb alb alb
        @param: hello
        :param just
    """
    # driver.get("https://www.google.com")
    extra.append(extras.text("bla bla bla"))
    assert True


def test_skip():
    pytest.skip("I DON*T NEED A REASON")


def test_fail():
    assert False


def test_xfail():
    pytest.xfail('MEH')


@pytest.mark.xfail()
def test_xpass():
    pass


@pytest.fixture
def setup1():
    hello
    

def test_setup(setup1):
    assert True


@pytest.fixture
def setup2():
    print("setup2")
    yield
    hello


def test_teardown(setup2):
    assert True


@pytest.fixture
def setup3():
    sleep(2)
    yield
    sleep(2)


def test_duration(setup3):
    sleep(2)
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


@pytest.fixture
def ansi_setup():
    print("hello")
    yield
    print(bye)


def test_ansi(ansi_setup):
    logging.info("well well well")
    colors = ['\033[31mRCOLOR\033[0m', '\033[32mGCOLOR\033[0m',
              '\033[33mYCOLOR\033[0m']
    for color in colors:
        print(color)

    assert False


def test_time():
    sleep(1)
    assert True


@pytest.fixture
def setup4():
    hello
    yield
    hello


def test_setup_and_teardown(setup4):
    assert True


def test_capture_logging_fail(loggingfixture):
    logging.info("failing")
    logging.info("no")
    assert False


@pytest.fixture
def loggingfixture():
    logging.info("setup")
    yield
    logging.info("teardown")


def test_capture_logging_pass(loggingfixture):
    logging.info("passing")
    logging.info("yes")
    assert True


@pytest.fixture
def capsetup():
    error


def test_capture_setup_fail(capsetup):
    assert True


def test_capture_test_fail():
    import sys
    print("merror", file=sys.stderr)
    print("bah humbug")
    assert False


@pytest.fixture
def stdout():
    import sys
    print("I am setup")
    print("setup error", file=sys.stderr)
    #logging.info("setup")
    yield
    print("I am teardown")
    print("teardown error", file=sys.stderr)
    #logging.info("teardown")


def test_capture_test_pass(stdout):
    import sys
    print("merror", file=sys.stderr)
    #logging.info("fail fail")
    print("bah humbug")
    assert True


@pytest.fixture
def capteardown():
    print("setup")
    yield
    error


def test_capture_test_teardown(capteardown):
    assert True


def test_abc():
    print("这是UTF-8内容")
    assert False


@pytest.mark.flaky(reruns=2)
def test_rerun():
    assert False


@pytest.mark.flaky(reruns=2)
def test_rerun_with_teardown(loggingfixture):
    assert False


import sys


@pytest.mark.skipif(sys.platform != "win32", reason="skip marker")
def test_skip_marker():
    assert False


@pytest.mark.skipif(sys.platform != "win32", reason="skip marker class")
class TestSkip:
    def test_skip_marker_class(self):
        assert False


@pytest.mark.xfail(reason="is broken")
class TestXFail:
    def test_xfail(self):
        assert False


@pytest.fixture
def vegars_setup():
    print("vegars setup")


def test_vegars(vegars_setup):
    print("vegars call")
    assert True
