# Algorithmes pour calculer les récompenses dans un environnement

**Monte Carlo :** dans cet algorithme, la récompense totale pour un état donné est calculée en utilisant **la moyenne des récompenses** obtenues à partir de ce même état jusqu'à la fin de l'épisode.

**Temporal Difference (TD) :** dans cet algorithme, la récompense est estimée en **comparant la récompense immédiate avec la récompense attendue à l'état suivant**. La différence entre les deux valeurs est utilisée pour ajuster la récompense.

**Q-Learning :** cet algorithme est similaire à TD, mais il utilise une estimation de la valeur de la fonction **Q pour prédire la récompense totale pour un état donné et une action donnée.** La valeur de la fonction Q est mise à jour à chaque étape en fonction de la récompense observée.

**SARSA (State-Action-Reward-State-Action):** il est similaire au Q-Learning, mais il utilise l'action sélectionnée pour la prochaine étape pour ajuster la récompense. Au lieu de prédire la récompense totale en fonction de l'état et de l'action, le SARSA utilise la récompense immédiate et la valeur prévue pour l'état suivant et l'action suivante.
