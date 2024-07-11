from sklearn import tree

# Exemplo simples de classificação com árvore de decisão
X = [[0, 0], [1, 1]]
y = [0, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

print(clf.predict([[2., 2.]]))  # Saída: [1]
