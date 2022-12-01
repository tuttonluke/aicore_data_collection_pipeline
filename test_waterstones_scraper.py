#%%
from pandas.testing import assert_series_equal
from project_files.waterstones_scraper import WaterstonesScraper
from unittest import TestCase
import pandas as pd
import unittest

#%%
class WaterstonesScraperTestCase(TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_driver = WaterstonesScraper('Jose Saramago')
        return super().setUpClass()
    
    def setUp(self) -> None:
        self.df = self.test_driver.get_book_data()
        return super().setUp()
    
    # @unittest.skip('Skip')
    def test_IDs(self):
        expected = pd.Series([9780099573586, 9780099461654, 9781784871789]).astype(str).rename("ID")
        actual = self.df["ID"]
        assert_series_equal(expected, actual)
    
    def test_dtypes(self):
        assert all(self.df.dtypes)
        #TestCase.assertEqual(self.df.dtypes, object)



#%%
unittest.main(argv=[''], exit=False)
# %%
