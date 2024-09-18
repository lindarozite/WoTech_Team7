import numpy as np

coin = ["H", "T"]

simulation_sizes = [100, 500, 1000]

simulations = {}

for size in simulation_sizes:
    sim_coin1 = np.random.choice(coin, size)
    sim_coin2 = np.random.choice(coin, size)
    simulations[size] = [''.join(pair) for pair in zip(sim_coin1, sim_coin2)]

nr_hh = np.sum([sim.count("HH") for sim in simulations.values()])
nr_tt = np.sum([sim.count("TT") for sim in simulations.values()])
nr_ht = np.sum([sim.count("HT") for sim in simulations.values()])
nr_th = np.sum([sim.count("TH") for sim in simulations.values()])


prob_hh = nr_hh / sum(simulation_sizes)
prob_tt = nr_tt / sum(simulation_sizes)
prob_ht = nr_ht / sum(simulation_sizes)
prob_th = nr_th / sum(simulation_sizes)

print(f"P(HH) = {prob_hh}")
print(f"P(TT) = {prob_tt}")
print(f"P(HT) = {prob_ht}")
print(f"P(TH) = {prob_th}")

#visualisation1
import matplotlib.pyplot as plt

bars = plt.bar(["HH", "TT", "HT", "TH"], [prob_hh, prob_tt, prob_ht, prob_th], 
               color=['#e63946', '#f1faee', '#a8dadc', '#457b9d'], edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', va='bottom', ha='center', fontsize=10, color='black')

plt.axhline(y=0.25, color='grey', linestyle='--', linewidth=1.5, label='Theoretical Probability')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.xlabel('Toss outcome', fontsize=12, fontweight='bold')
plt.ylabel('Probability', fontsize=12, fontweight='bold')
plt.title('Probability Distribution', fontsize=14, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend(loc='lower right')

plt.tight_layout()
plt.show()

#visualisation2
probs = [prob_hh, prob_tt, prob_ht, prob_th]

colors = ['#e63946', '#f1faee', '#a8dadc', '#457b9d']

wedges, texts, autotexts = plt.pie(probs, 
                                   labels=["HH", "TT", "HT", "TH"], 
                                   colors=colors,
                                   autopct='%1.1f%%',  
                                   startangle=140,    
                                   wedgeprops=dict(width=0.6, edgecolor='black')) 

for text in texts:
    text.set_color('black')
    text.set_fontsize(10)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('#003366')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')
  
plt.title('Probability Distribution of Coin Toss Outcomes', fontsize=14, fontweight='bold')

plt.show()
