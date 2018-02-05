import unittest
import pandas as pd
import numpy as np

from IpythonBridge.ipythonbridge import Ipythonbridge

class TestIpythonBridge(unittest.TestCase):

    def test_constructor(self):
        ipb = Ipythonbridge('12004')

    def test_send_dataframe_small_dataframe(self):

        ipb = Ipythonbridge('12004')
        df = pd.read_csv(
            'https://gist.githubusercontent.com/chriddyp/'
            'c78bf172206ce24f77d6363a2d754b59/raw/'
            'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
            'usa-agricultural-exports-2011.csv')

        ipb.sendDataFrame(df)


if __name__ == '__main__':
    unittest.main()
