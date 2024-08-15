'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`




'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
def felony_vs_non(merged_df):
    sns.lmplot(data=merged_df, 
               x='prediction_felony', 
               y='prediction_nonfelony', 
               hue='has_felony_charge', 
               fit_reg=False)
    plt.savefig('./data/part5_plots/scatterplot_felony_vs_nonfelony.png', bbox_inches='tight')
    
    
    print("The dots in the top right indicated that these people are predicted to have been rearrested for a felony")


# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?



# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?

def scatterplot_felony_rearrest_vs_actual(merged_df):
   
    sns.lmplot(data=merged_df, 
               x='prediction_felony', 
               y='y_felony', 
               fit_reg=False)
    plt.savefig('./data/part5_plots/scatterplot_felony_rearrest_vs_actual.png', bbox_inches='tight')

    # Analysis of model calibration based on the plot
   
    print("You would be able to tell if the model is calibrated well if there was a linear relationship, which we do not see, meaning that this model was not calibrated well")