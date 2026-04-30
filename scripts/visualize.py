import matplotlib.pyplot as plt
import os

def save_plot(filename, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, filename), bbox_inches='tight')
    plt.close()
    
def plot_misuse_comparison(output_dir):
    years = ['2015', '2024']
    stimulant_counts = [1219, 408]
    sedative_counts = [145, 45]

    x = range(len(years))  # creates bars on x axis

    fig, ax = plt.subplots(figsize=(8, 5))  # creates the figure, 8 inches wide 5 tall

    ax.bar([i - 0.2 for i in x], stimulant_counts, width=0.4, label='Stimulants', color='steelblue')
    ax.bar([i + 0.2 for i in x], sedative_counts, width=0.4, label='Sedatives', color='coral')
    # the -0.2 and +0.2  place the two bars side by side

    ax.set_xticks(x)
    ax.set_xticklabels(years)  # labels x axis with years
    ax.set_ylabel('Number of Misusers (Ages 16-25)')
    ax.set_title('Prescription Drug Misuse 2015 vs 2024')
    ax.legend()  # shows the legend

    save_plot('misuse_comparison.png', output_dir)
    
def plot_stress_comparison(output_dir):
    years = ['2015', '2024']
    stimulant_counts = [33, 57] 
    sedative_counts = [44, 79] 

    x = range(len(years))

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar([i - 0.2 for i in x], stimulant_counts, width=0.4, label='Stimulants', color='steelblue')
    ax.bar([i + 0.2 for i in x], sedative_counts, width=0.4, label='Sedatives', color='coral')

    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylabel('% of misusers with psychological distress')
    ax.set_title('Stress Levels Among Prescription Drug Misusers 2015 vs 2024')
    ax.legend()

    save_plot('stress_comparison.png', output_dir)
    
def plot_health_breakdown(output_dir):
    health_labels = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']
    
    # 2024
    stim_2024 = [57, 163, 131, 50, 7]
    sed_2024 = [1, 14, 13, 13, 4]
    
    # 2015
    stim_2015 = [315, 537, 289, 73, 5]
    sed_2015 = [31, 71, 37, 6, 0]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    # 2015
    ax1.bar([i - 0.2 for i in range(len(health_labels))], stim_2015, width=0.4, label='Stimulants', color='steelblue')
    ax1.bar([i + 0.2 for i in range(len(health_labels))], sed_2015, width=0.4, label='Sedatives', color='coral')

    ax1.set_xticks(range(len(health_labels)))
    ax1.set_xticklabels(health_labels)
    ax1.set_ylabel('Number of responses')
    ax1.set_title('Health Breakdown (2015)')
    ax1.legend()
    
    # 2024
    ax2.bar([i - 0.2 for i in range(len(health_labels))], stim_2024, width=0.4, label='Stimulants', color='steelblue')
    ax2.bar([i + 0.2 for i in range(len(health_labels))], sed_2024, width=0.4, label='Sedatives', color='coral')
    
    ax2.set_xticks(range(len(health_labels)))
    ax2.set_xticklabels(health_labels)
    ax2.set_ylabel('Number of responses')
    ax2.set_title('Health Breakdown (2024)')
    ax2.legend()
    
    save_plot('health_breakdown.png', output_dir)

def plot_income_breakdown(output_dir):
    income_labels = ['<$10k', '$10-19k', '$20-29k', '$30-39k', '$40-49k', '$50-74k', '$75k+']
    
    # 2024
    stim_2024 = [44, 46, 21, 35, 48, 58, 156]
    sed_2024 = [12, 4, 5, 4, 4, 5, 11]
    
    # 2015
    stim_2015 = [233, 157, 121, 115, 88, 143, 362]
    sed_2015 = [16, 17, 17, 18, 11, 13, 53]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 2015
    ax1.bar([i - 0.2 for i in range(len(income_labels))], stim_2015, width=0.4, label='Stimulants', color='steelblue')
    ax1.bar([i + 0.2 for i in range(len(income_labels))], sed_2015, width=0.4, label='Sedatives', color='coral')

    ax1.set_xticks(range(len(income_labels)))
    ax1.set_xticklabels(income_labels)
    ax1.set_ylabel('Number of misusers')
    ax1.set_title('Income Breakdown (2015)')
    ax1.legend()
    
    # 2024
    ax2.bar([i - 0.2 for i in range(len(income_labels))], stim_2024, width=0.4, label='Stimulants', color='steelblue')
    ax2.bar([i + 0.2 for i in range(len(income_labels))], sed_2024, width=0.4, label='Sedatives', color='coral')
    
    ax2.set_xticks(range(len(income_labels)))
    ax2.set_xticklabels(income_labels)
    ax2.set_ylabel('Number of misusers')
    ax2.set_title('Income Breakdown (2024)')
    ax2.legend()
    save_plot('income_breakdown.png', output_dir)
    
def plot_distress_age_comparison(output_dir):
    age_groups = ['2015\n(16-25)', '2024\n(16-25)', '2024\n(26-35)']
    
    stim = [33, 57, 43]
    sed = [44, 79, 34]
    
    x = range(len(age_groups))
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.bar([i - 0.2 for i in x], stim, width=0.4, label='Stimulants', color='steelblue')
    ax.bar([i + 0.2 for i in x], sed, width=0.4, label='Sedatives', color='coral')
    
    ax.set_xticks(x)
    ax.set_xticklabels(age_groups)
    ax.set_ylabel('% of misusers with psychological distress')
    ax.set_title('Psychological Distress Among Misusers by Group')
    ax.legend()
    save_plot('distress_age_comparison.png', output_dir)
    
def plot_race_breakdown(output_dir):
    racial_groups = ['White', 'Hispanic', 'Black', 'Multiracial', 'Asian']
    
    stim_2015 = [71, 14, 5, 6, 2]
    stim_2024 = [62, 19, 5, 9, 3]
    
    sed_2015 = [67, 15, 5, 9 ,3]
    sed_2024 = [60, 24, 7, 7, 2]
    
    x = range(len(racial_groups))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # 2015
    ax1.bar([i - 0.2 for i in x], stim_2015, width=0.4, label='Stimulants', color='steelblue')
    ax1.bar([i + 0.2 for i in x], sed_2015, width=0.4, label='Sedatives', color='coral')
    
    ax1.set_xticks(x)
    ax1.set_xticklabels(racial_groups)
    ax1.set_ylabel('% of misusers')
    ax1.set_title('Racial Breakdown (2015)')
    ax1.legend()
    
    # 2024
    ax2.bar([i - 0.2 for i in x], stim_2024, width=0.4, label='Stimulants', color='steelblue')
    ax2.bar([i + 0.2 for i in x], sed_2024, width=0.4, label='Sedatives', color='coral')
    
    ax2.set_xticks(x)
    ax2.set_xticklabels(racial_groups)
    ax2.set_ylabel('% of misusers')
    ax2.set_title('Racial Breakdown (2024)')
    ax2.legend()
    save_plot('race_breakdown.png', output_dir)

    
def plot_grouped_bar(output_dir, filename, title, ylabel, labels, series, figsize=(10, 5)):
        """
        labels: list of x axis labels example ['2015', '2024']
        series: dict of {name: values} example {'Stimulants': [1219, 408], 'Sedatives': [145, 45]}
        """
        x = range(len(labels))
        n = len(series)
        width = 0.8 / n
        
        fig, ax = plt.subplots(figsize=figsize)
        
        # fill in the rest
        # hint: you need to loop through series.items() to plot each bar group
        # the offset for each group needs to be calculated based on how many series there are
        
        for i, (name, values) in enumerate(series.items()):
            offset = (i - n/2 + 0.5) * width
            ax.bar ([x + offset for x in range (len(labels))], values, width = width, label = name)
    
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.legend()
        save_plot(filename, output_dir)

def plot_trend_line(output_dir, years, series):
    fig, ax = plt.subplots(figsize=(10, 5))
    
    for name, values in series.items():
        ax.plot(years, values, marker='o', label=name)
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Misusers (Ages 16-25)')
    ax.set_title('Prescription Drug Misuse Trend 2015-2024')
    ax.legend()
    save_plot('trend_line.png', output_dir)

def plot_race_rates(output_dir):
    groups = ['White', 'Black', 'Native Am.', 'Pacific Isl.', 'Asian', 'Multiracial', 'Hispanic']
    
    stim_2015 = [8.6, 2.3, 3.5, 4.2, 3.0, 7.5, 4.3]
    stim_2024 = [3.0, 0.8, 2.0, 1.9, 1.4, 3.2, 1.7]
    
    sed_2015 = [1.0, 0.3, 0.3, 0.8, 0.4, 1.4, 0.5]
    sed_2024 = [0.3, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    x = range(len(groups))
    width = 0.35
    
    ax1.bar([i - width/2 for i in x], stim_2015, width=width, label='2015', color='steelblue')
    ax1.bar([i + width/2 for i in x], stim_2024, width=width, label='2024', color='coral')
    ax1.set_xticks(x)
    ax1.set_xticklabels(groups, rotation=45, ha='right')
    ax1.set_ylabel('% of racial group that misuses')
    ax1.set_title('Stimulant Misuse Rate by Race')
    ax1.legend()
    
    ax2.bar([i - width/2 for i in x], sed_2015, width=width, label='2015', color='steelblue')
    ax2.bar([i + width/2 for i in x], sed_2024, width=width, label='2024', color='coral')
    ax2.set_xticks(x)
    ax2.set_xticklabels(groups, rotation=45, ha='right')
    ax2.set_ylabel('% of racial group that misuses')
    ax2.set_title('Sedative Misuse Rate by Race')
    ax2.legend()
    
    plt.tight_layout()
    save_plot('race_rates.png', output_dir)