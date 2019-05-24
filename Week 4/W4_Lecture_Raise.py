a = [2, 3, 4, 2]
b = [3, 4, 0, 20]


def get_ratios(L1, L2):
    """Assumes: L1, L2 are lists of equal lengths of numbers
            Returns: a list containing L1[i]/ L2[i]"""
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i]/L2[i])
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios


print(get_ratios(a, b))