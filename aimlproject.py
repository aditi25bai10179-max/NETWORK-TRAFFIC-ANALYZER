import pandas as pd
import matplotlib.pyplot as plt
import random

# STEP 1: Generate Network Data
time = list(range(1, 61))  # 60 time points

traffic = [random.randint(40, 100) for _ in time]

# Add artificial spikes (anomalies)
for i in [15, 30, 50]:
    traffic[i] = random.randint(140, 200)

protocols = [random.choice(['HTTP', 'FTP', 'TCP', 'UDP']) for _ in time]

data = pd.DataFrame({
    'Time': time,
    'Traffic': traffic,
    'Protocol': protocols
})

# STEP 2: Detect Anomali
threshold = data['Traffic'].mean() + 30   # dynamic threshold
spikes = data[data['Traffic'] > threshold]

# STEP 3: Print Results
print("\n--- Network Traffic Summary ---")
print("Average Traffic:", round(data['Traffic'].mean(), 2))
print("Maximum Traffic:", data['Traffic'].max())
print("Threshold for Spike Detection:", round(threshold, 2))

print("\nDetected Spikes:")
print(spikes)

# STEP 4: Graph 1 - Traffic Over Time

plt.figure()

plt.plot(data['Time'], data['Traffic'], marker='o', label="Traffic")
plt.scatter(spikes['Time'], spikes['Traffic'], label="Spikes")  # highlight spikes

plt.title("Network Traffic Over Time")
plt.xlabel("Time")
plt.ylabel("Traffic")
plt.legend()

plt.show()

# STEP 5: Graph 2 - Protocol Usage

protocol_count = data['Protocol'].value_counts()

plt.figure()

plt.bar(protocol_count.index, protocol_count.values)

plt.title("Protocol Usage Distribution")
plt.xlabel("Protocol")
plt.ylabel("Count")

plt.show()

# STEP 6: Graph 3 - Traffic Distribution
plt.figure()

plt.hist(data['Traffic'], bins=10)

plt.title("Traffic Distribution")
plt.xlabel("Traffic")
plt.ylabel("Frequency")

plt.show()