import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_girls_distribution(df):
    plt.figure(figsize=(14, 6))
    sns.histplot(data=df, x='girls_count', bins=20, kde=True)
    plt.title('Распределение количества девушек в клипах')
    plt.savefig('../dashboard/assets/girls_dist.png')  # для дэшборда

def plot_yearly_trends(df):
    # ... (ваш код визуализации)
    plt.savefig('../dashboard/assets/yearly_trends.png')
