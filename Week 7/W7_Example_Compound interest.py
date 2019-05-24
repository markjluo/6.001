import matplotlib.pyplot as plt


def retire(monthly, rate, terms):
    base = [0]
    saving = [0]
    mrate = rate/12
    for i in range(1, terms):
        base.append(i)
        saving.append((saving[-1])*(1+mrate) + monthly)
    return base, saving


def DisplayMonthlies(monthlies, rate, terms):
    plt.figure('Retirement Saving vs MC')
    plt.clf()
    plt.xlabel('Month')
    plt.ylabel('Saving Accrued')
    plt.title('Saving vs Monthly Contribution')
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label='Monthly Contribution = ' + str(monthly))
    plt.legend(loc='upper right')
    plt.show()


def DisplayRates(monthly, rates, terms):
    plt.figure('Retirement Saving vs Rates')
    plt.clf()
    plt.xlabel('Month')
    plt.ylabel('Money Saved')
    plt.title('Saving vs Interest Rates')
    for rate in rates:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label='i = ' + str(rate))
    plt.legend()
    plt.show()


def DisplayBoth(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30 * 12, 40 * 12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', '.', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i % len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j % len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel + rateLabel, label='retire:' + str(monthly) + ':' + str(int(rate * 100)))
    plt.legend(loc='upper left')
    plt.show()


def BothWithSubplots(monthlies, rates, terms):
    assert len(monthlies) <= 4, 'The length of Monthlies must not be larger than 4'
    plt.figure('Both with subplots')
    plt.clf()
    for i in range(0, len(monthlies)):
        monthly = monthlies[i]
        plt.subplot(221+i)
        plt.title('Monthly Contribution = ' + str(monthly))
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, label='MC = ' + str(monthly) + ' / i = ' + str(rate))
            plt.legend()
    plt.show()


# Rates(1000, [0.03, 0.05, 0.07], 12*40)
# Monthlies([400, 600, 800, 1000], 0.05, 12*40)
# displayBoth([400, 600, 800, 1000], [0.03, 0.05, 0.07], 12*40)
BothWithSubplots([400, 600, 800, 1000], [0.03, 0.05, 0.07], 12*40)

