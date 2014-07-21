import sys, warnings

if sys.version_info[0] < 3:
    warnings.warn("Este programa necesita Python 3.0 para funcionar.",
    RuntimeWarning)
else:
    print('Proceder normalmente.')