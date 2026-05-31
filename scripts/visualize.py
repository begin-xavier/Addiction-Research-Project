import matplotlib.pyplot as plt
import os

def save_plot(filename, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, filename), bbox_inches='tight')
    plt.close()

def add_bar_labels(ax, bars):
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.annotate(f'{height}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3), textcoords='offset points',
                       ha='center', va='bottom', fontsize=8)

def plot_trend_line(output_dir, years, series, figure_num, caption):
    fig, ax = plt.subplots(figsize=(10, 5))
    for name, values in series.items():
        ax.plot(years, values, marker='o', label=name)
        for x, y in zip(years, values):
            ax.annotate(f'{y}%', xy=(x, y), xytext=(0, 6),
                       textcoords='offset points', ha='center', fontsize=8)
    ax.set_xlabel('Year')
    ax.set_ylabel('% of Sample Reporting Misuse')
    ax.legend()
    fig.suptitle(f'Figure {figure_num}', fontsize=12, fontweight='bold')
    fig.text(0.5, -0.02, caption, ha='center', fontsize=10, style='italic', wrap=True)
    plt.tight_layout()
    save_plot('trend_line.png', output_dir)

def plot_health_breakdown(output_dir, stim_2015, stim_2024, sed_2015, sed_2024, figure_num, caption):
    health_labels = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    x = range(len(health_labels))
    width = 0.35

    bars1 = ax1.bar([i - width/2 for i in x], stim_2015, width=width, label='2015', color='steelblue')
    bars2 = ax1.bar([i + width/2 for i in x], stim_2024, width=width, label='2024', color='mediumpurple')
    add_bar_labels(ax1, bars1)
    add_bar_labels(ax1, bars2)
    ax1.set_xticks(x)
    ax1.set_xticklabels(health_labels)
    ax1.set_ylabel('% of misusers')
    ax1.set_title('Stimulant Misusers')
    ax1.legend()

    bars3 = ax2.bar([i - width/2 for i in x], sed_2015, width=width, label='2015', color='steelblue')
    bars4 = ax2.bar([i + width/2 for i in x], sed_2024, width=width, label='2024', color='mediumpurple')
    add_bar_labels(ax2, bars3)
    add_bar_labels(ax2, bars4)
    ax2.set_xticks(x)
    ax2.set_xticklabels(health_labels)
    ax2.set_ylabel('% of misusers')
    ax2.set_title('Sedative Misusers')
    ax2.legend()

    fig.suptitle(f'Figure {figure_num}', fontsize=12, fontweight='bold')
    fig.text(0.5, -0.02, caption, ha='center', fontsize=10, style='italic', wrap=True)
    plt.tight_layout()
    save_plot('health_breakdown.png', output_dir)

def plot_income_breakdown(output_dir, stim_2015, stim_2024, sed_2015, sed_2024, labels, figure_num, caption):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    x = range(len(labels))
    width = 0.35

    bars1 = ax1.bar([i - width/2 for i in x], stim_2015, width=width, label='Stimulants', color='steelblue')
    bars2 = ax1.bar([i + width/2 for i in x], sed_2015, width=width, label='Sedatives', color='coral')
    add_bar_labels(ax1, bars1)
    add_bar_labels(ax1, bars2)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, rotation=45, ha='right')
    ax1.set_ylabel('% of misusers')
    ax1.set_title('Income Breakdown (2015)')
    ax1.legend()

    bars3 = ax2.bar([i - width/2 for i in x], stim_2024, width=width, label='Stimulants', color='steelblue')
    bars4 = ax2.bar([i + width/2 for i in x], sed_2024, width=width, label='Sedatives', color='coral')
    add_bar_labels(ax2, bars3)
    add_bar_labels(ax2, bars4)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, rotation=45, ha='right')
    ax2.set_ylabel('% of misusers')
    ax2.set_title('Income Breakdown (2024)')
    ax2.legend()

    fig.suptitle(f'Figure {figure_num}', fontsize=12, fontweight='bold')
    fig.text(0.5, -0.02, caption, ha='center', fontsize=10, style='italic', wrap=True)
    plt.tight_layout()
    save_plot('income_breakdown.png', output_dir)

def plot_distress_age_comparison(output_dir, stim_vals, sed_vals, labels, figure_num, caption):
    x = range(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(8, 5))
    bars1 = ax.bar([i - width/2 for i in x], stim_vals, width=width, label='Stimulants', color='steelblue')
    bars2 = ax.bar([i + width/2 for i in x], sed_vals, width=width, label='Sedatives', color='coral')
    add_bar_labels(ax, bars1)
    add_bar_labels(ax, bars2)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel('% of misusers with psychological distress')
    ax.legend()
    fig.suptitle(f'Figure {figure_num}', fontsize=12, fontweight='bold')
    fig.text(0.5, -0.02, caption, ha='center', fontsize=10, style='italic', wrap=True)
    plt.tight_layout()
    save_plot('distress_age_comparison.png', output_dir)

def plot_race_rates(output_dir, groups, stim_2015, stim_2024, sed_2015, sed_2024, figure_num, caption):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    x = range(len(groups))
    width = 0.35

    bars1 = ax1.bar([i - width/2 for i in x], stim_2015, width=width, label='2015', color='steelblue')
    bars2 = ax1.bar([i + width/2 for i in x], stim_2024, width=width, label='2024', color='mediumpurple')
    add_bar_labels(ax1, bars1)
    add_bar_labels(ax1, bars2)
    ax1.set_xticks(x)
    ax1.set_xticklabels(groups, rotation=45, ha='right')
    ax1.set_ylabel('% of racial group that misuses')
    ax1.set_title('Stimulant Misuse Rate by Race')
    ax1.legend()

    bars3 = ax2.bar([i - width/2 for i in x], sed_2015, width=width, label='2015', color='steelblue')
    bars4 = ax2.bar([i + width/2 for i in x], sed_2024, width=width, label='2024', color='mediumpurple')
    add_bar_labels(ax2, bars3)
    add_bar_labels(ax2, bars4)
    ax2.set_xticks(x)
    ax2.set_xticklabels(groups, rotation=45, ha='right')
    ax2.set_ylabel('% of racial group that misuses')
    ax2.set_title('Sedative Misuse Rate by Race')
    ax2.legend()

    fig.suptitle(f'Figure {figure_num}', fontsize=12, fontweight='bold')
    fig.text(0.5, -0.02, caption, ha='center', fontsize=10, style='italic', wrap=True)
    plt.tight_layout()
    save_plot('race_rates.png', output_dir)