# BAZOUZI MOHAMED RASSIM GR-01 security
# Bassem Refrafi GR-02 security
# Said Tigane GR-02 security

nStates = int(input("Enter number of states: "))

nSymbols = int(input("Enter number of symbols: "))
symbols = []
print("Enter symbols:")
for i in range(nSymbols):
    sym = input().strip()
    if sym != 'e':
        symbols.append(sym)

start = int(input("Enter start state: "))

nFinals = int(input("Enter number of final states: "))
finals = set()
print("Enter final states:")
for i in range(nFinals):
    finals.add(int(input()))

nTrans = int(input("Enter number of transitions: "))
transitions = []
print("Enter transitions as: from symbol to (use e for epsilon)")
print("Ex:'0 a 1'")
print("Type 'f' when finished")

for i in range(nTrans):
    while True:
        user_input = input(f"Transition {i+1}/{nTrans}: ")
        if user_input.lower() == 'f':
            print("Stopping input...")
            break
        parts = user_input.split()
        if len(parts) != 3:
            print("Error: Need 3 values. Try again.")
            continue
        fr, sym, to = parts
        transitions.append((int(fr), sym, int(to)))
        break

adj = {}
for s in range(nStates):
    adj[s] = {}

for fr, sym, to in transitions:
    if sym not in adj[fr]:
        adj[fr][sym] = set()
    adj[fr][sym].add(to)

eclose = {}

for s in range(nStates):
    closure = set()
    closure.add(s)

    changed = True
    while changed:
        changed = False

        for u in list(closure):   
            if 'e' in adj[u]:
                for v in adj[u]['e']:
                    if v not in closure:
                        closure.add(v)
                        changed = True

    eclose[s] = closure

print("--- Epsilon-closure ---")
for s in range(nStates):
    print("e-closure(", s, ") =", sorted(eclose[s]))


new_adj = {}
for p in range(nStates):
    new_adj[p] = {}
    for a in symbols:
        new_adj[p][a] = set()

for p in range(nStates):
    for a in symbols:
        temp = set()

        
        for r in eclose[p]:
            if a in adj[r]:
                for x in adj[r][a]:
                    temp.add(x)

        
        for x in temp:
            for t in eclose[x]:
                new_adj[p][a].add(t)

new_finals = set()
for p in range(nStates):
    for f in finals:
        if f in eclose[p]:
            new_finals.add(p)
            break

print("NFA without epsilon (Result)")
print("States:", list(range(nStates)))
print("Alphabet:", symbols)
print("Start state:", start)
print("Final states:", sorted(new_finals))
print("Transitions (without ε) - Arrow style:")
for p in range(nStates):
    for a in symbols:
        if new_adj[p][a]:
            for q in new_adj[p][a]:
                print(f"{p} --{a}--> {q}")
