from pages.signin.sign_in_page import SignInPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    #Class Level Setup definig the lp object for the SignInPage class
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = SignInPage(self.driver)

# Test Cases:
    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.clickSignInLink()
        # result = self.lp.verifySignInPageIsLoaded()
        # assert result == True
