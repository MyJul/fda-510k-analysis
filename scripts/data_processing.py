import matplotlib.pyplot as plt
import seaborn as sns

def plot_avg_decision_days_bar(summary_df, output_path=None):
    """
    Creates a horizontal bar chart of average decision days by product code.

    Args:
        summary_df (pd.DataFrame): Summary statistics DataFrame with 'mean' column.
        output_path (str, optional): Path to save the plot image. If None, shows the plot.

    Returns:
        None
    """
    sorted_avg = summary_df['mean'].sort_values()
    plt.figure(figsize=(10, 6))
    sorted_avg.plot(kind='barh', color='skyblue')
    plt.xlabel('Average Decision Time (Days)')
    plt.ylabel('Product Code')
    plt.title('Average Decision Time by Product Code')
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()

def plot_decision_time_distribution(df, group_col='DECISION'):
    """
    Creates a boxplot showing distribution of decision time by group (e.g., decision type).

    Args:
        df (pd.DataFrame): DataFrame with DECISION_DAYS and group_col.
        group_col (str): Column to group by (e.g., 'DECISION', 'CLASSADVISECOMM').

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x=group_col, y='DECISION_DAYS')
    plt.xticks(rotation=45)
    plt.title(f'Decision Time Distribution by {group_col}')
    plt.xlabel(group_col)
    plt.ylabel('Decision Days')
    plt.tight_layout()
    plt.show()
