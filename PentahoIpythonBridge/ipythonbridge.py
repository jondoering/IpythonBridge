import jupyter_client
import numpy as np
import pandas as pd
import tempfile


class Ipythonbridge:

    def __init__(self, cf_name):
        self.connection_file = jupyter_client.find_connection_file(cf_name)
        self.kernel_client = jupyter_client.BlockingKernelClient(connection_file=self.connection_file)
        self.kernel_client.load_connection_file()

        #execute
        self.kernel_client.execute('import pandas as pd')
        #self.kernel_client.execute('import pandas as pd')


    def sendDataFrame(self, df, df_name='pentaho_df', ):
    #Sends a dataframe

        json_df = df.to_json()
        self.kernel_client.execute("{} = pd.read_json('{}')".format(df_name, json_df))


    def sendObject(self):
        pass


    def close(self):
        self.kernel_client.clo