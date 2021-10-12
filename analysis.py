import json
import itertools
import matplotlib.pyplot as plt

with open('output.ndjson') as fin:
  data = [json.loads(line) for line in fin]

unique = set((datum['low_a'], datum['low_b']) for datum in data)
print(f'Num unique analyses: {len(unique)}')

Qs = {r['q'] for r in itertools.chain.from_iterable([d['result'] for d in data])}
Qs = sorted(Qs)[::-1]
print(f'Num unique triplets: {len(Qs)}')
print(f'Top 5 Q values:      {", ".join([str(q) for q in Qs[:5]])}')

print(f'You have done {round(100*len(unique)/(data[-1]["low_b"]**2), 4)}% of the total work.')
print()

plt.hist(Qs, bins=50)
plt.xlabel('q')
plt.ylabel('Count')
plt.title('Q Values of Found Triplets')
plt.show()
