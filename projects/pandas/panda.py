from matplotlib import pyplot as plt
import numpy as np
import cufflinks as cf
from plotly.offline import download_plotlyjs,plot,iplot
import pandas as pd
df1 = pd.read_csv('df1.csv',index_col=0)
cf.go_offline()
# DATA
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df.head()
df.iplot(df1)
plt.show()
