'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony


def create_felony_charge(arrest_events):
    felony_charge = arrest_events.groupby('arrest_id').apply(
        lambda x: pd.Series({'has_felony_charge': (x['charge_degree'] == 'F').any()})
    ).reset_index()
    return felony_charge
    



# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

def merge(pred_universe, felony_charge, arrest_events):
    
    merged_df = pd.merge(pred_universe, felony_charge, on='arrest_id', how='left') #merge felony_charge df to pred_universe df
    
    
    merged_df = pd.merge(merged_df, arrest_events[['arrest_id', 'charge_degree']], on='arrest_id', how='left') #add the charge_degree column from arrest events to merged_df
    
    return merged_df
    

    

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.

def catplot_rearrest(merged_df):
     
     
     
     sns.catplot(data=merged_df, 
                x='charge_degree', 
                y='prediction_felony', 
                kind='bar')
     plt.savefig('./data/part4_plots/catplot_rearrest.png', bbox_inches='tight')


# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest

def catplot_nonfelony(merged_df):
    sns.catplot(data=merged_df, 
                x='charge_degree', 
                y='prediction_nonfelony', 
                kind='bar')
    plt.savefig('./data/part4_plots/catplot_nonfelony.png', bbox_inches='tight')
    
    
    print("The difference in plots could be because with different crimes, different predictions are being made with different things to account for")
# In a print statement, answer the following question: What might explain the difference between the plots?



# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?

def catplot_rearrest_hue_actual(merged_df):
   
    sns.catplot(data=merged_df, 
                x='charge_degree', 
                y='prediction_felony', 
                hue='y_felony', 
                kind='bar')
    plt.savefig('./data/part4_plots/catplot_rearrest_hue_actual.png', bbox_inches='tight')

    print("Felony charges with no rearrest may indicate the model overestimates risk, while misdemeanor charges with rearrest suggest underestimation.")