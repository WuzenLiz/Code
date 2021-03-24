def clearall():
    all = [var for var in globals() if (var[:2], var[-2:]) != ("__", "__")]
    for var in all:
        del globals()[var]