import os

import clr

apiDll = os.getcwd() + '/dlls/Api.dll'
clr.AddReference(apiDll)

auto_correlation_Dll = os.getcwd() + '/dlls/AutoCorrelation.dll'
clr.AddReference(auto_correlation_Dll)

