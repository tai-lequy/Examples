import sys
import pandas as pd
import numpy as np
import scipy
import sklearn
import matplotlib
import seaborn
import statsmodels
def main():
    print("python: {}".format(sys.version))
    print("numpy: {}".format(np.__version__))
    print("pandas: {}".format(pd.__version__))
    print("scipy: {}".format(scipy.__version__))
    print("scikit-learn: {}".format(sklearn.__version__))
    print("matplotlib: {}".format(matplotlib.__version__))
    print("seaborn: {}".format(seaborn.__version__))
    print("statsmodels: {}".format(statsmodels.__version__))
if __name__ == '__main__':
   main()