# Apprentissage de réflexes par renforcement

Mise en situation: On joue à un jeu dont on ne connait pas les règles et après environ 100 coups, l'adversaire me dis "tu as perdu"

L'algo d'apprentissage par renforcement consiste à : 
    apprendre les actions à prendre
        - à partir d'expériences
        - de façon à optimiser une récompense quantitative
        - au cours du temps

Deux suppositions:

I- L'agent connait pas ou mal son environnement, par conséquence, il ne connait pas à priori quels sont les renforcements associés à chaque transition, et il ne connait pas la topologie de l'espace
    
II- L'agent ne connaît pas ou mal l'effet de ses actions dans un état donné

Le monde est:
    Stochastique: Les actions peuvent avoir des effets non déterministes
    Stationnaire: Les probabilités de transition et les renforcements restent stables

Pour communiquer avec son environnement, un agent communique par 3 canaux: 
    Un canal perceptif s(t) qui mesure l'état courant de l'agent dans son environnement
    Un canal spécifique aux signaux de renforcement r(t) qui renseigne sur la qualité de l'état courant
    Un canal d'action qui transmet l'action de l'agent a(t) à l'environnement

$$s_{t} \text{ l'éspace des états} $$

$$r_{t} ∈R \text{, l’espace des signaux,} r(t) ∈ [−a,+b], a,b ∈R^+ $$

$a_{t} ∈A$, l’espace des actions

L'agent est une fonction 
$$s_{t} \mapsto a_{t} $$

L'enfironnement est un fonction
$$(s_{t},a_{t}) \mapsto(s_{t+1},r_{t})$$
En pratique elle est décomposée:
    La fonctionde transition entre états T:
    $$(s_{t},a_{t}) \mapsto s_{t+1}$$
    La fonction de renforcement immédiat R:
    $$(s_{t},a_{t}) \mapsto r_{t}$$

La mesure de gain:
    Pas de mesure de gain universelle
    Doit être spécifiée par problème
    En général, on choisit de cumuler le gain dans le temps
    Choix de la mesure est déterminant

