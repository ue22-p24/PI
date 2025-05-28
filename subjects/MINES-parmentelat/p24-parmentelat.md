# 12 « Implémenter sa propre librairie `exact_cover` »

Vous avez aimé le sujet de Hackathon sur les pentaminos ? Ce sujet est pour vous !  
Il s'agit d'écrire, et non plus de simplement utiliser, une librairie qui permet de résoudre le problème dit de l'*exact cover*.

## Contexte

Le problème de l'*exact cover* est un problème classique en informatique, qui
consiste à trouver un sous-ensemble d'éléments qui couvre exactement un ensemble
donné, sans répétition. Il est souvent utilisé dans des applications telles que
la résolution de puzzles, la planification et l'optimisation.

Le sujet du hackathon visait à appliquer cette approche ppour résoudre des
problèmes de pentaminos, mais sa portée est bien plus générale que cela.

## L'algorithme de Knuth

Il s'agit d'un **problème NP-complet** (voir
<https://en.wikipedia.org/wiki/NP-completeness>); toutefois un certain Donald
Knuth (la légende veut qu'on peut lui écrire en mettant simplement comme adresse
"Donald Knuth, USA") a proposé une approche élégante - connue [sous le nom
d'Algorithme X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) - pour le
résoudre de manière relativement efficace.

### backtracking

L'algorithme de Knuth repose sur une approche dite de *backtracking*
(littéralement: retour en arrière), où on explore les différentes possibilités
de manière récursive; et si à un moment donné on se rend compte qu'on ne peut
pas aller plus loin, on revient en arrière pour essayer les autres possibilités.

### dancing links

L'algorithme utilise une structure de données appelée *dancing links*, qui
permet de manipuler efficacement les colonnes et les lignes de la matrice de
contraintes.

## deux versions

On peut trouver (au moins) deux versions de cet algorithme; il sera intéressant
de regarder ces deux papiers, et idéalement des les implémenter tous les deux
pour les comparer; en réalité c'est le même algorithme, mais qui utilise des
structures de données différentes; l'évolution entre les deux est
particulièrement intéressante, car elle reflète très bien l'évolution des
paradigmes de programmation vers un monde où tout est vectorisé.

### première version

un premier article de 2000 [est disponible en ligne sur
arxiv](http://arxiv.org/pdf/cs/0011047v1); dans cette façon de présenter les
  choses (pages 1 à 8 essentiellement), on aurait envie d'utiliser un langage de
bas niveau comme du C ou du Rust, car il s'agit d'implémenter une structure de
données de cellules doublement chainées (i.e. horizontalement et verticalement).

✅ à propos de cette version de l'algorithme, vous pourriez lire le code de
`exact_cover` qui est disponible sur github à l'adresse  
`git@github.com:jwg4/exact_cover.git` où le coeur de l'algorithme est, assez
logiquement du coup, écrit en C.

### deuxième version

on retrouve le même algorithme dans le livre de Knuth "The Art of Computer
Programming", mais cette version utilise cette fois une structure de données en
tableaux, bien plus propice à la vectorisation.

La référence est "Volume 4B, section 7.2.2 "Backtrack Programming", et plus
précisément 7.2.2.1 "Dancing Links" - [voir le pdf joint, pages 1 à
5](knuth-7.2.2.1-dancing-links.pdf)

✅ la librairie `xcover` git@github.com:johnrudge/xcover.git s'inspire de cette
version de l'algorithme, et est écrite cette fois en Python/numpy (et numba,
mais n'anticipons pas).

## le plan

Voici quelques directions de travail possibles:

- lire et comprendre les deux versions de l'algorithme, et les implémenter
  dans le langage de votre choix  
- prenez garde à faire en sorte qu'on puisse utiliser votre librairie même sur
  des gros problèmes; par exemple si vous utilisez Python, pensez à écrire un
  **générateur** de solutions, de cette façon on pourra chercher seulement la
  première - ou les quelques premières -  solutions d'un très gros problème;

- comparer les deux implémentations, en termes à la fois de:
  - performances - typiquement temps d'exécution
  - temps de développement
  - maintenabilité / lisibilité (c'est plus subjectif bien sûr)
- de manière connexe, vous pourriez aussi comparer vos performances avec celles
  des librairies citées plus haut; si vous avez utilisé Python, vous pouvez envisager de regarder les techniques de compilation JIT comme numba etc..

- écrire une batterie de tests, et automatiser leur exécution à chaque commit
  sur github
- écrire une documentation claire et concise, qui explique comment utiliser
  votre librairie, et comment l'installer
- exposer votre librairie, par exemple en la publiant sur PyPI ou npm
- développer des librairies connexes, qui utilisent votre librairie
  `exact_cover` pour résoudre des problèmes concrets, par exemple le sudoku ou
  des problèmes de planification (comme on l'avait fait pour le hackathon)

## autres ressources utiles

- le repo `git@github.com:parmentelat/exact-cover-samples.git` contient des
échantillons de problèmes d'*exact cover*, avec leurs solutions, qui peuvent
être utilisés pour tester votre implémentation - n'hésitez pas à contribuer en
ajoutant des problèmes supplémentaires, les PRs sont les bienvenues !
