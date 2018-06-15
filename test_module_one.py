import pytest


class TestModuleOne:

    @pytest.mark.positive
    def test_module_one_positive(self):
        with pytest.allure.step("Step 1"):
            print("Step 1")

    @pytest.mark.negative
    def test_module_one_negative(self):
        with pytest.allure.step("Step 1"):
            print("Step 1")