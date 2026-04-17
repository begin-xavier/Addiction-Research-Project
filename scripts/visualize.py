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
