import time

import pytest


class TestModuleTwo:

    @pytest.mark.positive
    def test_module_two_positive(self):
        with pytest.allure.step("Step 1"):
            print("Step 1")

    @pytest.mark.negative
    def test_module_two_negative(self):
        with pytest.allure.step("Step 1"):
            assert int(time.time()) % 2 == 0
