#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Blake Dukes"
__version__ = "0.1.0"
__license__ = "MIT"


def show_map(subject):
    import os
    import pandas as pd
    import calplot
    import seaborn as sb
    import matplotlib.pyplot as plt
    from matplotlib import font_manager as fm
    from settings import CLEANED_DATA_PATH as cdd
    from settings import FONT_PATH as font_path


    try:


        """ Main entry point of the app """
        df = pd.read_csv(cdd)

        df['Date'] = pd.to_datetime(df['Date'], yearfirst=True)

        df.set_index('Date', inplace=True)
        # formatting
        col = 'counts'
        title = '\nMessages To & From ' + subject
        cmap = sb.color_palette("YlGnBu", as_cmap=True)

        fontproperties = fm.FontProperties(fname=font_path, size=22)
        yearlabel_kws = dict(fontproperties=fontproperties,
                            ha='center', color='#000000')
        suptitle_kws = dict(fontproperties=fontproperties, ha='center', size=52)

        calplot.calplot(df[col], how='sum',
                        suptitle=title, cmap=cmap,
                        figsize=(14, 7), suptitle_kws=suptitle_kws,
                        yearlabel_kws=yearlabel_kws,
                        linecolor='w', linewidth=2,
                        fillcolor='w', edgecolor='black')
        plt.show()
    except Exception as e:
        print('heatmap.py:')
        print(e)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    print('This file outputs the contents of currently cleaned data as a calendar heatmap.')
