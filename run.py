# -*- encoding=utf8 -*-

import os
import pytest

from lib.tools import gen_result_dir

if __name__ == '__main__':
    # init_config()
    report_path = gen_result_dir()
    # https://buildmedia.readthedocs.org/media/pdf/pytest/latest/pytest.pdf
    pytest.main(['-s', '-q', '-k not slow', '--alluredir', report_path])
    os.system('allure generate %s -o ./result-report --clean' % report_path)
