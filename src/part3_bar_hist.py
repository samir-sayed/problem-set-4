'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def barplot_fta(pred_universe):
    
    sns.countplot(data=pred_universe, 
                  x='fta')
    plt.savefig('./data/part3_plots/barplot_fta.png', bbox_inches='tight')
    
    



# 2. Hue the previous barplot by sex
def barplot_hue(pred_universe):
    sns.countplot(data=pred_universe, 
                  x='fta', 
                  hue='sex')
    plt.savefig('./data/part3_plots/barplot_fta_hue_sex.png', bbox_inches='tight')



# 3. Plot a histogram of age_at_arrest

def hist_arrest(pred_universe):
    sns.histplot(data=pred_universe, 
                 x='age_at_arrest')
    plt.savefig('./data/part3_plots/histogram_age_at_arrest.png', bbox_inches='tight')



# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 

def hist_age(pred_universe):
    bins = [18, 21, 30, 40, 100] #age groups
    sns.histplot(data=pred_universe, 
                 x='age_at_arrest', 
                 bins=bins)
    plt.savefig('./data/part3_plots/histogram_age_groups.png', bbox_inches='tight')
