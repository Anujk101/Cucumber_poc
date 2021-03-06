# from common.driver import browser
from pytest_bdd import scenarios
from tests.amazon_search import *

scenarios('feature_files')
