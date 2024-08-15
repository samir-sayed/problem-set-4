'''
- You will run Problem Set 4 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    directories = ['data/part2_plots', 'data/part3_plots', 'data/part4_plots', 'data/part5_plots']
    part1.create_directories(directories)
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()
    
    felony_charge = part4.create_felony_charge(arrest_events)
    merged_df = part4.merge(pred_universe, felony_charge, arrest_events)
    
    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)

    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    # 1 
    part3.barplot_fta(pred_universe)
    print("fta barplot created.")

    # 2
    part3.barplot_hue(pred_universe)
    print("fta barplot with hue created")

    # 3
    part3.hist_arrest(pred_universe)
    print("histogram age_at_arrest=saved.") #logging as there were issues running part 3


    # 4
    part3.hist_age(pred_universe)
    print("histogram age_at_arrest saved. (BINS)")
    

    ##  PART 4: CATEGORICAL PLOTS  ##
    # 1
    
    part4.catplot_rearrest(merged_df)
    print("Done1") #logging added here as there were troubles correctly running part 4
    print(merged_df.columns)
    
    # 2
    part4.catplot_nonfelony(merged_df)
    print("Done2")

    # 3
    part4.catplot_rearrest_hue_actual(merged_df)
    print("done3")

    ##  PART 5: SCATTERPLOTS  ##
    # 1
    part5.felony_vs_non(merged_df)
    
    # 2
    part5.scatterplot_felony_rearrest_vs_actual(merged_df)


if __name__ == "__main__":
    main()
