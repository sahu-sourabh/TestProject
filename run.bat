@echo off

rem chrome browser
pytest -s -v TestData/test_login_ddt_demo.py
rem pytest -s -v -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=Reports/report.html testCases/ --browser chrome

rem edge browser
rem pytest -s -v -m "sanity" --html=Reports/report_edge.html testCases/ --browser edge
rem pytest -s -v -m "sanity or regression" --html=Reports/report.html testCases/ --browser edge
rem pytest -s -v -m "sanity and regression" --html=Reports/report.html testCases/ --browser edge
rem pytest -s -v -m "regression" --html=Reports/report.html testCases/ --browser edge

pause