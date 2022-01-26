import os
import pytest


# def pytest_html_results_table_header(cells):
#     cells[1].attr.class_ = 'sortable initial-sort'
#     cells[0].attr.class_ = 'sortable result'


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     extra = getattr(report, 'extra', [])

#     main_script_dir = os.path.dirname(__file__)
#     rel_path = "screenshots/ss.jpg" # hardcoded image file
#     image = pytest_html.extras.image(os.path.join(main_script_dir, rel_path))
#     extra.append(image)
#     report.extra = extra
