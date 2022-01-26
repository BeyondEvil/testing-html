import base64
import os
import pytest
import random
from py.xml import html
from pytest_html import extras
# from pytest_html.plugin import HTMLReport
# print("TRHEE")


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["<p>prefix</p>"])
    summary.extend(["<p>summary</p>"])
    postfix.extend(["<p>postfix</p>"])


def pytest_html_results_table_header(cells):
    # print("HEADERS: ", cells)
    cells.insert(2, "<th>Two</th>")
    cells.insert(3, "<th>Three</th>")

    cells.insert(4, html.th("Four", class_="sortable", col='time'))
    # cells[4] = html.th("Four", class_="sortable", col='time')
    #cells.append("<th>Six</th>")
    #cells.append("<th>Five</th>")


def pytest_html_results_table_row(report, cells):
    # print("ROWS: ", cells)
    # if report.skipped:
    #     del cells[:]
    # else:
    from time import time
    cells.insert(2, f"<td>{report.nodeid}</td>")
    cells.insert(3, f"<td>{report.nodeid}</td>")
    cells.insert(4, html.td(time(), class_="col-time"))
    # cells[4] = html.td("fofo", class_="col-time")
    #cells.append(f"<td>meh</td>")
    #cells.append(f"<td>moh</td>")


# def pytest_html_results_table_html(report, data):
    # print("REPORT: ", report)
    # print("DATA:", data)
    # print("TYPE: ", type(data))
    # data.append(f"<p>{report.nodeid}blergh</p>")
    # print("")
    # print(len(data))
    # for each in data:
    #     print("================================")
    #     print(str(each))
    #     print(type(each))
    # if report.passed:
    #     del data[:]
    #     data.append(f"<p>{report.nodeid}blergh</p>")
    # print("DATA:", data[-1])
    # print("TYPE: ", type(data[-1]))


# def pytest_html_results_table_html(report, data):
#     if report.when in ('call', 'teardown'):
#         setup_text = None
#         call_text = None
#         other_text = ''
#         for each in data:
#             title, text = each.split("\n", 1)
#             if 'Captured stdout setup' in title:
#                 setup_text = text
#             elif 'Captured stdout call' in title:
#                 call_text = text
#             else:
#                 other_text += text
#         if setup_text is None or len(setup_text) == 0:
#             return  # ??
#
#         import uuid
#         html = []
#         node_id = uuid.uuid4() # random id
#         html.append(f'<input id="{node_id}" class="toggle" type="checkbox">') # Setup checkbox
#         html.append(f'<label for="{node_id}" class="lbl-toggle">Show setup output</label>') # Label
#         html.append(f'<div class="log collapsible-content">{setup_text}</div>') # Setup log
#         if call_text is not None and len(call_text):
#             node_id = uuid.uuid4() # random id
#             html.append(f'<input id="{node_id}" class="toggle" type="checkbox" checked>') # Call checkbox
#             html.append(f'<label for="{node_id}" class="lbl-toggle">Show test output</label>') # Label
#             html.append(f'<div class="log collapsible-content">{call_text}</div>') # Call log
#         elif not len(other_text):
#             # show setup if no call log and no other data
#             html[0].replace('<input ', '<input checked ')
#
#         if len(other_text):
#             html.append('<div class="log">'+other_text+'</div>')
#         del data[:]
#         data.append('<div>'+''.join(html)+'</div>')


def pytest_html_report_title(report):
    # print("inside hook")
    report.title = "My very own title!"


# @pytest.hookimpl(trylast=True)
# def pytest_runtest_logreport(report):
#     print("err: ", report.capstderr)
#     print("out: ", report.capstdout)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        report.extras = [extras.html('<div>sandman</div>')]
        # content = "u'\u0081'"
        # report.extras = [extras.text(f"{content}")]
        # extra = getattr(report, "extra", [])
        # content = str(random.random())
        # charset = "utf-8"
        # data = base64.b64encode(content.encode(charset)).decode(charset)
        # extra.append(extras.mp4(f"{data}"))
        # report.extra = extra

# def pytest_html_results_table_header(cells):
#     cells[1].attr.class_ = 'sortable initial-sort'
#     cells[0].attr.class_ = 'sortable result'


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     pytest_html2 = item.config.pluginmanager.getplugin('html')
#     extra = getattr(report, 'extra', [])
#     print(pytest_html2)
#     main_script_dir = os.path.dirname(__file__)
#     rel_path = "screenshots/ss.jpg"  # hardcoded image file
#     image = pytest_html2.extras.image(os.path.join(main_script_dir, rel_path))
#     extra.append(image)
#     report.extra = extra
