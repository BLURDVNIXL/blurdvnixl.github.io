#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX 100

/*
 * ═══════════════════════════════════════════════════════════════════════════
 *                GUIDE COMPLET DES STRUCTURES DE DONNÉES EN C
 * ═══════════════════════════════════════════════════════════════════════════
 * 
 * DÉFINITIONS FONDAMENTALES:
 * 
 * 📌 ALLOCATION DYNAMIQUE:
 *    Processus de réservation de mémoire pendant l'exécution du programme
 *    (runtime) plutôt qu'à la compilation. Permet de créer des structures
 *    dont la taille n'est pas connue à l'avance.
 * 
 * 📌 STRUCTURE (struct):
 *    Type de données composé qui regroupe plusieurs variables (possiblement
 *    de types différents) sous un même nom. Permet de modéliser des entités
 *    complexes (ex: étudiant avec nom, âge, note).
 * 
 * 📌 POINTEUR:
 *    Variable qui contient l'adresse mémoire d'une autre variable. Essentiel
 *    pour l'allocation dynamique et la manipulation de structures complexes.
 *    Notation: int *p (p est un pointeur vers un entier).
 * 
 * 📌 LISTE CHAÎNÉE:
 *    Structure de données linéaire où chaque élément (noeud) contient une
 *    valeur et un pointeur vers l'élément suivant. Permet des insertions/
 *    suppressions efficaces mais accès séquentiel uniquement.
 * 
 * 📌 PILE (Stack):
 *    Structure LIFO (Last In, First Out = Dernier Entré, Premier Sorti).
 *    Comme une pile d'assiettes: on ne peut ajouter/retirer qu'au sommet.
 *    Opérations: push (empiler), pop (dépiler), top (consulter sommet).
 * 
 * 📌 FILE (Queue):
 *    Structure FIFO (First In, First Out = Premier Entré, Premier Sorti).
 *    Comme une file d'attente: on entre par derrière, on sort par devant.
 *    Opérations: enqueue (enfiler), dequeue (défiler).
 * 
 * 📌 ARBRE BINAIRE:
 *    Structure hiérarchique où chaque noeud a au maximum deux enfants
 *    (gauche et droite). Un Arbre Binaire de Recherche (ABR) respecte:
 *    fils gauche < parent < fils droit, permettant des recherches rapides.
 * 
 * 📌 COMPLEXITÉ TEMPORELLE:
 *    - O(1): Constant - temps fixe quelle que soit la taille
 *    - O(n): Linéaire - temps proportionnel à la taille
 *    - O(log n): Logarithmique - temps qui double quand taille × 10
 *    - O(n²): Quadratique - temps proportionnel au carré de la taille
 * 
 * ═══════════════════════════════════════════════════════════════════════════
 * 
 * CONTENU DU PROGRAMME:
 * 1. Allocation dynamique pour structures
 * 2. Tableaux de structures dynamiques
 * 3. Allocation pour chaînes de caractères
 * 4. Tableaux 2D dynamiques
 * 5. Listes chaînées simples
 * 6. Piles (Stack - LIFO)
 * 7. Files (Queue - FIFO)
 * 8. Arbres binaires de recherche (ABR)
 * 
 * ═══════════════════════════════════════════════════════════════════════════
 */

// ==================== STRUCTURES ====================

/*
 * DÉFINITION - STRUCTURE ÉTUDIANT:
 * Type composé regroupant plusieurs informations sur un étudiant.
 * Utilise un tableau statique pour le nom (taille fixe de 50 caractères).
 */
typedef struct {
    char nom[50];    // Nom de l'étudiant (chaîne de caractères)
    int age;         // Âge en années
    float note;      // Note sur 20
} Etudiant;

/*
 * DÉFINITION - STRUCTURE PRODUIT:
 * Modélise un article de magasin avec identifiant, nom et prix.
 */
typedef struct {
    int id;          // Identifiant unique du produit
    char nom[30];    // Nom du produit
    float prix;      // Prix en euros
} Produit;

/*
 * DÉFINITION - NOEUD DE LISTE CHAÎNÉE:
 * Élément de base d'une liste chaînée. Contient:
 * - data: la valeur stockée
 * - next: pointeur vers le noeud suivant (NULL si dernier élément)
 * 
 * Structure auto-référencée car elle contient un pointeur vers son propre type.
 */
typedef struct Node {
    int data;              // Valeur du noeud
    struct Node *next;     // Pointeur vers le noeud suivant
} Node;

/*
 * DÉFINITION - PILE (Stack):
 * Implémentation avec tableau statique.
 * - data[]: tableau contenant les éléments
 * - top: indice du sommet (-1 si pile vide)
 * 
 * Principe LIFO: Le dernier élément ajouté est le premier retiré.
 */
typedef struct {
    int data[MAX];   // Tableau des éléments (taille maximale MAX)
    int top;         // Indice du sommet de la pile
} Pile;

/*
 * DÉFINITION - FILE (Queue):
 * Implémentation circulaire avec tableau statique.
 * - data[]: tableau contenant les éléments
 * - front: indice du premier élément
 * - rear: indice du dernier élément
 * 
 * Principe FIFO: Le premier élément ajouté est le premier retiré.
 * File circulaire: utilise l'opérateur modulo (%) pour "boucler" dans le tableau.
 */
typedef struct {
    int data[MAX];   // Tableau des éléments
    int front;       // Indice du premier élément (-1 si vide)
    int rear;        // Indice du dernier élément (-1 si vide)
} File;

/*
 * DÉFINITION - NOEUD D'ARBRE BINAIRE:
 * Élément de base d'un arbre binaire. Chaque noeud possède:
 * - data: la valeur stockée
 * - gauche: pointeur vers le fils gauche (NULL si absent)
 * - droite: pointeur vers le fils droit (NULL si absent)
 * 
 * Dans un ABR: toutes les valeurs à gauche < data < toutes les valeurs à droite
 */
typedef struct Noeud {
    int data;                 // Valeur du noeud
    struct Noeud *gauche;     // Pointeur vers le sous-arbre gauche
    struct Noeud *droite;     // Pointeur vers le sous-arbre droit
} Noeud;

// ==================== ALLOCATION DYNAMIQUE POUR STRUCTURES ====================

/*
 * DÉMONSTRATION: Allocation dynamique pour une structure
 * 
 * CONCEPT CLÉ:
 * malloc() alloue un bloc de mémoire sur le TAS (heap) et retourne un pointeur.
 * sizeof(Etudiant) calcule la taille exacte en octets de la structure.
 * 
 * AVANTAGES:
 * - Taille flexible (déterminée à l'exécution)
 * - Durée de vie contrôlée (existe jusqu'au free())
 * 
 * INCONVÉNIENTS:
 * - Nécessite gestion manuelle de la mémoire (free obligatoire)
 * - Plus lent que l'allocation statique
 * - Risque de fuites mémoire si on oublie le free()
 */
void demo_allocation_structure() {
    printf("\n=== ALLOCATION DYNAMIQUE POUR STRUCTURES ===\n");
    
    // malloc retourne void*, on le cast en Etudiant*
    // sizeof(Etudiant) = taille totale de la structure en octets
    Etudiant *e1 = (Etudiant*)malloc(sizeof(Etudiant));
    
    // IMPORTANT: Toujours vérifier si malloc a réussi
    if(e1 == NULL) {
        printf("Erreur d'allocation!\n");
        return;
    }
    
    // Accès aux champs avec l'opérateur flèche (->)
    // e1->nom équivaut à (*e1).nom
    strcpy(e1->nom, "Alice Dupont");
    e1->age = 20;
    e1->note = 15.5;
    
    printf("Étudiant créé:\n");
    printf("  Nom: %s\n", e1->nom);
    printf("  Age: %d\n", e1->age);
    printf("  Note: %.2f\n", e1->note);
    
    // CRUCIAL: Libérer la mémoire après utilisation
    // Évite les fuites mémoire (memory leaks)
    free(e1);
}

// ==================== TABLEAU DE STRUCTURES DYNAMIQUES ====================

/*
 * FONCTION: Tri à bulles (Bubble Sort) pour tableau de structures
 * 
 * ALGORITHME:
 * Compare chaque paire d'éléments adjacents et les échange si nécessaire.
 * Répète le processus jusqu'à ce que le tableau soit trié.
 * 
 * COMPLEXITÉ:
 * - Temps: O(n²) dans le pire cas
 * - Espace: O(1) - tri en place
 * 
 * EXERCICE CLASSIQUE en exam!
 */
void trierProduits(Produit *tab, int n) {
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n-i-1; j++) {
            // Échange si l'élément courant > élément suivant
            if(tab[j].prix > tab[j+1].prix) {
                Produit temp = tab[j];
                tab[j] = tab[j+1];
                tab[j+1] = temp;
            }
        }
    }
}

/*
 * DÉMONSTRATION: Tableau dynamique de structures
 * 
 * CONCEPT CLÉ:
 * n * sizeof(Produit) alloue un bloc contigu pour n structures.
 * On peut accéder aux éléments avec tab[i] comme un tableau normal.
 * 
 * USAGE TYPIQUE:
 * - Bases de données en mémoire
 * - Listes d'étudiants/produits/clients
 * - Tableaux dont la taille est saisie par l'utilisateur
 */
void demo_tableau_structures() {
    printf("\n=== TABLEAU DE STRUCTURES DYNAMIQUES ===\n");
    
    int n = 5;
    
    // Alloue de la mémoire pour n structures Produit
    // Équivalent à: Produit tab[n] mais avec taille dynamique
    Produit *produits = (Produit*)malloc(n * sizeof(Produit));
    
    if(produits == NULL) {
        printf("Erreur d'allocation!\n");
        return;
    }
    
    // Remplissage du tableau
    for(int i = 0; i < n; i++) {
        produits[i].id = i + 1;
        sprintf(produits[i].nom, "Produit%d", i + 1);
        produits[i].prix = (float)(rand() % 100 + 10);
    }
    
    printf("Avant tri:\n");
    for(int i = 0; i < n; i++) {
        printf("  ID: %d, Nom: %s, Prix: %.2f€\n", 
               produits[i].id, produits[i].nom, produits[i].prix);
    }
    
    // Tri du tableau par prix croissant
    trierProduits(produits, n);
    
    printf("\nAprès tri par prix:\n");
    for(int i = 0; i < n; i++) {
        printf("  ID: %d, Nom: %s, Prix: %.2f€\n", 
               produits[i].id, produits[i].nom, produits[i].prix);
    }
    
    // Libération de tout le bloc en une seule fois
    free(produits);
}

// ==================== ALLOCATION POUR CHAÎNES ====================

/*
 * DÉMONSTRATION: Trois fonctions d'allocation mémoire
 * 
 * malloc(taille):
 *   - Alloue un bloc de mémoire de 'taille' octets
 *   - Contenu initial = aléatoire (garbage)
 *   - Plus rapide que calloc
 * 
 * calloc(nombre, taille):
 *   - Alloue 'nombre' éléments de 'taille' octets chacun
 *   - INITIALISE tout à ZÉRO
 *   - Utile pour les tableaux d'entiers/floats
 * 
 * realloc(pointeur, nouvelle_taille):
 *   - Redimensionne un bloc déjà alloué
 *   - Préserve le contenu existant
 *   - Peut déplacer le bloc en mémoire
 *   - ATTENTION: toujours réaffecter le pointeur (peut changer)
 * 
 * USAGE TYPIQUE:
 * - Chaînes de taille variable
 * - Buffers de lecture
 * - Tableaux dynamiques redimensionnables
 */
void demo_allocation_chaines() {
    printf("\n=== ALLOCATION DYNAMIQUE POUR CHAÎNES ===\n");
    
    // malloc: alloue 20 octets non initialisés
    char *str1 = (char*)malloc(20 * sizeof(char));
    strcpy(str1, "Bonjour");
    printf("str1 (malloc): %s\n", str1);
    
    // calloc: alloue 20 octets initialisés à 0
    // Utile car garantit que la chaîne se termine par '\0'
    char *str2 = (char*)calloc(20, sizeof(char));
    strcpy(str2, "Hello");
    printf("str2 (calloc): %s\n", str2);
    
    // realloc: agrandit str1 de 20 à 50 octets
    // Préserve "Bonjour" et permet d'ajouter plus de texte
    str1 = (char*)realloc(str1, 50 * sizeof(char));
    strcat(str1, " le monde!");
    printf("str1 (realloc): %s\n", str1);
    
    // Libération mémoire
    free(str1);
    free(str2);
}

// ==================== TABLEAUX 2D DYNAMIQUES ====================

/*
 * FONCTION: Afficher une matrice
 * %3d = affiche l'entier sur 3 caractères (alignement vertical)
 */
void afficherMatrice(int **matrice, int lignes, int colonnes) {
    for(int i = 0; i < lignes; i++) {
        for(int j = 0; j < colonnes; j++) {
            printf("%3d ", matrice[i][j]);
        }
        printf("\n");
    }
}

/*
 * FONCTION: Libérer une matrice 2D
 * IMPORTANT: Libérer dans l'ordre inverse de l'allocation!
 * 1. D'abord chaque ligne
 * 2. Ensuite le tableau de pointeurs
 */
void libererMatrice(int **matrice, int lignes) {
    for(int i = 0; i < lignes; i++) {
        free(matrice[i]);  // Libère chaque ligne
    }
    free(matrice);  // Libère le tableau de pointeurs
}

/*
 * DÉMONSTRATION: Tableau 2D dynamique (matrice)
 * 
 * STRUCTURE EN MÉMOIRE:
 * matrice → [ptr0] → [0][1][2][3]      (ligne 0)
 *           [ptr1] → [4][5][6][7]      (ligne 1)
 *           [ptr2] → [8][9][10][11]    (ligne 2)
 * 
 * MÉTHODE D'ALLOCATION:
 * 1. Allouer un tableau de pointeurs (une par ligne)
 * 2. Pour chaque pointeur, allouer un tableau d'entiers (les colonnes)
 * 
 * ACCÈS:
 * matrice[i][j] accède à l'élément ligne i, colonne j
 * 
 * APPLICATIONS:
 * - Matrices mathématiques (multiplication, transposée)
 * - Grilles de jeu (échecs, morpion, labyrinthe)
 * - Images (pixels en 2D)
 * - Tableaux de distances
 */
void demo_tableaux_2d() {
    printf("\n=== TABLEAUX 2D DYNAMIQUES ===\n");
    
    int lignes = 3, colonnes = 4;
    
    // Étape 1: Allouer un tableau de 'lignes' pointeurs
    int **matrice = (int**)malloc(lignes * sizeof(int*));
    
    // Étape 2: Pour chaque ligne, allouer un tableau de 'colonnes' entiers
    for(int i = 0; i < lignes; i++) {
        matrice[i] = (int*)malloc(colonnes * sizeof(int));
    }
    
    // Remplissage: valeur = indice linéaire (0, 1, 2, ...)
    for(int i = 0; i < lignes; i++) {
        for(int j = 0; j < colonnes; j++) {
            matrice[i][j] = i * colonnes + j;
        }
    }
    
    printf("Matrice 3x4:\n");
    afficherMatrice(matrice, lignes, colonnes);
    
    // Libération: ordre inverse de l'allocation!
    libererMatrice(matrice, lignes);
}

// ==================== LISTES CHAÎNÉES ====================

/*
 * FONCTION: Insérer au début de la liste
 * COMPLEXITÉ: O(1) - temps constant
 * 
 * PRINCIPE:
 * 1. Créer un nouveau noeud
 * 2. Le faire pointer vers l'ancien premier
 * 3. Il devient le nouveau premier
 */
Node* insererDebut(Node *head, int valeur) {
    Node *nouveau = (Node*)malloc(sizeof(Node));
    nouveau->data = valeur;
    nouveau->next = head;  // Le nouveau pointe vers l'ancien premier
    return nouveau;        // Le nouveau devient le premier
}

/*
 * FONCTION: Insérer à la fin de la liste
 * COMPLEXITÉ: O(n) - doit parcourir toute la liste
 * 
 * PRINCIPE:
 * 1. Créer un nouveau noeud
 * 2. Parcourir jusqu'au dernier noeud
 * 3. Faire pointer le dernier vers le nouveau
 */
Node* insererFin(Node *head, int valeur) {
    Node *nouveau = (Node*)malloc(sizeof(Node));
    nouveau->data = valeur;
    nouveau->next = NULL;
    
    if(head == NULL) return nouveau;  // Liste vide
    
    // Parcourir jusqu'au dernier
    Node *temp = head;
    while(temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = nouveau;
    return head;
}

/*
 * FONCTION: Afficher tous les éléments de la liste
 */
void afficherListe(Node *head) {
    Node *temp = head;
    while(temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

/*
 * FONCTION: Supprimer un élément de valeur donnée
 * COMPLEXITÉ: O(n)
 * 
 * CAS PARTICULIERS:
 * - Élément à supprimer = premier → simple
 * - Élément au milieu → relier précédent au suivant
 * - Élément non trouvé → ne rien faire
 */
Node* supprimerElement(Node *head, int valeur) {
    if(head == NULL) return NULL;
    
    // Cas 1: Supprimer le premier
    if(head->data == valeur) {
        Node *temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    
    // Cas 2: Chercher dans le reste
    Node *current = head;
    while(current->next != NULL && current->next->data != valeur) {
        current = current->next;
    }
    
    // Si trouvé, supprimer
    if(current->next != NULL) {
        Node *temp = current->next;
        current->next = current->next->next;  // Sauter le noeud à supprimer
        free(temp);
    }
    
    return head;
}

/*
 * FONCTION: Inverser la liste (EXERCICE TRÈS FRÉQUENT!)
 * COMPLEXITÉ: O(n)
 * 
 * TECHNIQUE DES 3 POINTEURS:
 * - prev: noeud précédent (NULL au début)
 * - current: noeud actuel
 * - next: noeud suivant (sauvegarde)
 * 
 * PRINCIPE:
 * Pour chaque noeud, inverser son lien next pour qu'il pointe vers prev
 */
Node* inverserListe(Node *head) {
    Node *prev = NULL;
    Node *current = head;
    Node *next = NULL;
    
    while(current != NULL) {
        next = current->next;      // Sauvegarder le suivant
        current->next = prev;      // Inverser le lien
        prev = current;            // Avancer prev
        current = next;            // Avancer current
    }
    
    return prev;  // prev est devenu le nouveau premier
}

/*
 * FONCTION: Libérer toute la liste
 * IMPORTANT: Parcourir et libérer chaque noeud un par un
 */
void libererListe(Node *head) {
    Node *temp;
    while(head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

/*
 * DÉMONSTRATION: Listes chaînées
 * 
 * AVANTAGES:
 * - Insertion/suppression en O(1) au début
 * - Taille dynamique illimitée
 * - Pas de réallocation nécessaire
 * 
 * INCONVÉNIENTS:
 * - Accès séquentiel uniquement (pas d'accès direct)
 * - Consomme plus de mémoire (pointeurs)
 * - Cache CPU moins efficace
 */
void demo_listes_chainees() {
    printf("\n=== LISTES CHAÎNÉES SIMPLES ===\n");
    
    Node *head = NULL;
    
    // Construire: 20 -> 10 -> 5 -> 15 -> NULL
    head = insererDebut(head, 10);
    head = insererDebut(head, 20);
    head = insererFin(head, 5);
    head = insererFin(head, 15);
    
    printf("Liste initiale: ");
    afficherListe(head);
    
    head = supprimerElement(head, 10);
    printf("Après suppression de 10: ");
    afficherListe(head);
    
    head = inverserListe(head);
    printf("Liste inversée: ");
    afficherListe(head);
    
    libererListe(head);
}

// ==================== PILES (STACK) ====================

/*
 * FONCTION: Initialiser une pile vide
 * top = -1 signifie pile vide
 */
void initialiserPile(Pile *p) {
    p->top = -1;
}

/*
 * FONCTION: Vérifier si la pile est vide
 * Retourne 1 (vrai) si vide, 0 (faux) sinon
 */
int pileEstVide(Pile *p) {
    return p->top == -1;
}

/*
 * FONCTION: Vérifier si la pile est pleine
 * top == MAX-1 signifie que tous les emplacements sont utilisés
 */
int pileEstPleine(Pile *p) {
    return p->top == MAX - 1;
}

/*
 * FONCTION: Empiler (PUSH) - Ajouter au sommet
 * COMPLEXITÉ: O(1)
 * 
 * PRINCIPE:
 * 1. Incrémenter top
 * 2. Placer la valeur à la position top
 */
void empiler(Pile *p, int valeur) {
    if(pileEstPleine(p)) {
        printf("Pile pleine!\n");
        return;
    }
    p->data[++(p->top)] = valeur;  // ++top puis data[top] = valeur
}

/*
 * FONCTION: Dépiler (POP) - Retirer du sommet
 * COMPLEXITÉ: O(1)
 * 
 * PRINCIPE LIFO: Le dernier empilé est le premier dépilé
 */
int depiler(Pile *p) {
    if(pileEstVide(p)) {
        printf("Pile vide!\n");
        return -1;
    }
    return p->data[(p->top)--];  // Retourne data[top] puis top--
}

/*
 * FONCTION: Consulter le sommet sans dépiler
 */
int sommetPile(Pile *p) {
    if(pileEstVide(p)) {
        printf("Pile vide!\n");
        return -1;
    }
    return p->data[p->top];
}

/*
 * EXERCICE CLASSIQUE: Vérifier si les parenthèses sont équilibrées
 * 
 * PRINCIPE:
 * - Empiler chaque ouvrante: ( { [
 * - Pour chaque fermante: ) } ]
 *   → Dépiler et vérifier la correspondance
 * - À la fin, pile doit être vide
 * 
 * EXEMPLES:
 * "{[()]}" → Équilibré
 * "{[(])}" → Non équilibré ('] avant )')
 * "(()"    → Non équilibré (pile non vide à la fin)
 * 
 * APPLICATIONS:
 * - Vérification syntaxique des langages de programmation
 * - Éditeurs de code
 */
int parenthesesEquilibrees(char *expression) {
    Pile p;
    initialiserPile(&p);
    
    for(int i = 0; expression[i] != '\0'; i++) {
        char c = expression[i];
        
        // Si ouvrante, empiler
        if(c == '(' || c == '{' || c == '[') {
            empiler(&p, c);
        }
        // Si fermante, vérifier correspondance
        else if(c == ')' || c == '}' || c == ']') {
            if(pileEstVide(&p)) return 0;
            
            int top = depiler(&p);
            
            // Vérifier la paire
            if((c == ')' && top != '(') ||
               (c == '}' && top != '{') ||
               (c == ']' && top != '[')) {
                return 0;
            }
        }
    }
    
    // Équilibré ssi pile vide à la fin
    return pileEstVide(&p);
}

/*
 * DÉMONSTRATION: Piles
 * 
 * APPLICATIONS TYPIQUES:
 * - Historique de navigation (bouton "retour")
 * - Fonction UNDO/REDO
 * - Évaluation d'expressions arithmétiques
 * - Parcours en profondeur (DFS) dans les graphes
 * - Gestion des appels de fonctions (call stack)
 */
void demo_piles() {
    printf("\n=== PILES (STACK - LIFO) ===\n");
    
    Pile p;
    initialiserPile(&p);
    
    // Empiler 10, 20, 30
    empiler(&p, 10);
    empiler(&p, 20);
    empiler(&p, 30);
    
    printf("Sommet: %d\n", sommetPile(&p));        // 30
    printf("Dépiler: %d\n", depiler(&p));          // 30
    printf("Nouveau sommet: %d\n", sommetPile(&p)); // 20
    
    // Test parenthèses équilibrées (EXERCICE CLASSIQUE)
    char *expr1 = "{[()]}";
    char *expr2 = "{[(])}";
    printf("\n'%s' est %s\n", expr1, 
           parenthesesEquilibrees(expr1) ? "équilibré" : "non équilibré");
    printf("'%s' est %s\n", expr2, 
           parenthesesEquilibrees(expr2) ? "équilibré" : "non équilibré");
}

// ==================== FILES (QUEUE) ====================

/*
 * FONCTION: Initialiser une file vide
 * front = rear = -1 signifie file vide
 */
void initialiserFile(File *f) {
    f->front = -1;
    f->rear = -1;
}

/*
 * FONCTION: Vérifier si la file est vide
 */
int fileEstVide(File *f) {
    return f->front == -1;
}

/*
 * FONCTION: Vérifier si la file est pleine (file circulaire)
 * (rear + 1) % MAX == front signifie que le prochain emplacement est front
 */
int fileEstPleine(File *f) {
    return (f->rear + 1) % MAX == f->front;
}

/*
 * FONCTION: Enfiler (ENQUEUE) - Ajouter à la fin
 * COMPLEXITÉ: O(1)
 * 
 * PRINCIPE FILE CIRCULAIRE:
 * Utilise l'opérateur modulo (%) pour "boucler" dans le tableau
 * Exemple avec MAX=5:
 *   rear=4 → (4+1)%5=0 → revient au début
 * 
 * Cela permet de réutiliser les emplacements libérés à l'avant
 */
void enfiler(File *f, int valeur) {
    if(fileEstPleine(f)) {
        printf("File pleine!\n");
        return;
    }
    
    // Si file vide, initialiser front
    if(fileEstVide(f)) {
        f->front = 0;
    }
    
    // Avancer rear de façon circulaire
    f->rear = (f->rear + 1) % MAX;
    f->data[f->rear] = valeur;
}

/*
 * FONCTION: Défiler (DEQUEUE) - Retirer du début
 * COMPLEXITÉ: O(1)
 * 
 * PRINCIPE FIFO: Le premier enfilé est le premier défilé
 */
int defiler(File *f) {
    if(fileEstVide(f)) {
        printf("File vide!\n");
        return -1;
    }
    
    int valeur = f->data[f->front];
    
    // Si c'était le dernier élément, réinitialiser
    if(f->front == f->rear) {
        f->front = f->rear = -1;
    } else {
        // Avancer front de façon circulaire
        f->front = (f->front + 1) % MAX;
    }
    
    return valeur;
}

/*
 * FONCTION: Afficher le contenu de la file
 * Parcourt de front à rear en gérant le caractère circulaire
 */
void afficherFile(File *f) {
    if(fileEstVide(f)) {
        printf("File vide\n");
        return;
    }
    
    printf("File: ");
    int i = f->front;
    
    // Parcours circulaire
    while(1) {
        printf("%d ", f->data[i]);
        if(i == f->rear) break;  // Arrêt quand on atteint rear
        i = (i + 1) % MAX;       // Avancer de façon circulaire
    }
    printf("\n");
}

/*
 * DÉMONSTRATION: Files (simulation file d'attente)
 * 
 * APPLICATIONS TYPIQUES:
 * - Files d'attente de clients (banque, caisse, guichet)
 * - Gestion d'imprimante (print spooler)
 * - Ordonnancement de processus (CPU scheduling)
 * - Parcours en largeur (BFS) dans les graphes
 * - Buffer de communication
 * - Gestion de messages (messagerie)
 * 
 * AVANTAGES FILE CIRCULAIRE:
 * - Réutilise l'espace libéré à l'avant
 * - Évite le décalage des éléments
 * - Operations en O(1)
 */
void demo_files() {
    printf("\n=== FILES (QUEUE - FIFO) ===\n");
    
    File f;
    initialiserFile(&f);
    
    // Simulation d'une banque
    printf("Clients arrivent: 101, 102, 103\n");
    enfiler(&f, 101);
    enfiler(&f, 102);
    enfiler(&f, 103);
    afficherFile(&f);
    
    printf("\nService du client %d\n", defiler(&f));
    afficherFile(&f);
    
    printf("\nNouveau client: 104\n");
    enfiler(&f, 104);
    afficherFile(&f);
}

// ==================== ARBRES BINAIRES ====================

/*
 * FONCTION: Créer un nouveau noeud
 * Alloue un noeud avec valeur, fils gauche et droit à NULL
 */
Noeud* creerNoeud(int valeur) {
    Noeud *nouveau = (Noeud*)malloc(sizeof(Noeud));
    nouveau->data = valeur;
    nouveau->gauche = NULL;
    nouveau->droite = NULL;
    return nouveau;
}

/*
 * FONCTION: Insérer dans un Arbre Binaire de Recherche (ABR)
 * COMPLEXITÉ: O(log n) si équilibré, O(n) si dégénéré
 * 
 * PROPRIÉTÉ ABR (Binary Search Tree):
 * - Toutes les valeurs du sous-arbre GAUCHE < valeur du noeud
 * - Toutes les valeurs du sous-arbre DROIT > valeur du noeud
 * 
 * PRINCIPE (récursif):
 * 1. Si arbre vide, créer un noeud
 * 2. Si valeur < racine, insérer à gauche
 * 3. Si valeur > racine, insérer à droite
 * 4. Si valeur = racine, ne rien faire (pas de doublons)
 */
Noeud* insererArbre(Noeud *racine, int valeur) {
    if(racine == NULL) {
        return creerNoeud(valeur);
    }
    
    if(valeur < racine->data) {
        racine->gauche = insererArbre(racine->gauche, valeur);
    } else if(valeur > racine->data) {
        racine->droite = insererArbre(racine->droite, valeur);
    }
    // Si égal, on n'insère pas (pas de doublons)
    
    return racine;
}

/*
 * PARCOURS INFIXE (In-order): Gauche - Racine - Droite
 * IMPORTANT: Affiche les éléments dans l'ORDRE CROISSANT pour un ABR!
 * 
 * Exemple d'arbre:
 *       50
 *      /  \
 *    30    70
 *   /  \   /  \
 *  20  40 60  80
 * 
 * Parcours infixe: 20, 30, 40, 50, 60, 70, 80
 */
void parcoursInfixe(Noeud *racine) {
    if(racine != NULL) {
        parcoursInfixe(racine->gauche);    // Visiter gauche
        printf("%d ", racine->data);       // Visiter racine
        parcoursInfixe(racine->droite);    // Visiter droite
    }
}

/*
 * PARCOURS PRÉFIXE (Pre-order): Racine - Gauche - Droite
 * Utile pour: copier l'arbre, évaluer expressions préfixes
 * 
 * Même arbre → Parcours préfixe: 50, 30, 20, 40, 70, 60, 80
 */
void parcoursPrefixe(Noeud *racine) {
    if(racine != NULL) {
        printf("%d ", racine->data);       // Visiter racine
        parcoursPrefixe(racine->gauche);   // Visiter gauche
        parcoursPrefixe(racine->droite);   // Visiter droite
    }
}

/*
 * PARCOURS POSTFIXE (Post-order): Gauche - Droite - Racine
 * Utile pour: supprimer l'arbre, évaluer expressions postfixes
 * 
 * Même arbre → Parcours postfixe: 20, 40, 30, 60, 80, 70, 50
 */
void parcoursPostfixe(Noeud *racine) {
    if(racine != NULL) {
        parcoursPostfixe(racine->gauche);  // Visiter gauche
        parcoursPostfixe(racine->droite);  // Visiter droite
        printf("%d ", racine->data);       // Visiter racine
    }
}

/*
 * FONCTION: Calculer la hauteur de l'arbre
 * COMPLEXITÉ: O(n) - doit visiter tous les noeuds
 * 
 * DÉFINITION:
 * Hauteur = nombre de niveaux
 * - Arbre vide: hauteur 0
 * - Arbre avec une seule racine: hauteur 1
 * - Hauteur = 1 + max(hauteur gauche, hauteur droite)
 */
int hauteurArbre(Noeud *racine) {
    if(racine == NULL) return 0;
    
    int hGauche = hauteurArbre(racine->gauche);
    int hDroite = hauteurArbre(racine->droite);
    
    return 1 + (hGauche > hDroite ? hGauche : hDroite);
}

/*
 * FONCTION: Compter le nombre total de noeuds
 * COMPLEXITÉ: O(n)
 * 
 * PRINCIPE:
 * Nombre de noeuds = 1 (racine) + noeuds à gauche + noeuds à droite
 */
int compterNoeuds(Noeud *racine) {
    if(racine == NULL) return 0;
    return 1 + compterNoeuds(racine->gauche) + compterNoeuds(racine->droite);
}

/*
 * DÉMONSTRATION: Arbres Binaires de Recherche
 * 
 * APPLICATIONS TYPIQUES:
 * - Dictionnaires (recherche rapide)
 * - Index de bases de données
 * - Systèmes de fichiers (hiérarchie)
 * - Expressions arithmétiques
 * - Arbres de décision
 * - Arbres généalogiques
 * 
 * AVANTAGES ABR (si équilibré):
 * - Recherche en O(log n)
 * - Insertion en O(log n)
 * - Suppression en O(log n)
 * - Parcours infixe donne l'ordre trié
 * 
 * INCONVÉNIENTS:
 * - Peut dégénérer en liste si insertions triées (O(n))
 * - Solutions: AVL, Red-Black trees (auto-équilibrage)
 */
void demo_arbres() {
    printf("\n=== ARBRES BINAIRES DE RECHERCHE ===\n");
    
    Noeud *racine = NULL;
    
    // Construction de l'arbre (insertion de valeurs)
    racine = insererArbre(racine, 50);
    insererArbre(racine, 30);
    insererArbre(racine, 70);
    insererArbre(racine, 20);
    insererArbre(racine, 40);
    insererArbre(racine, 60);
    insererArbre(racine, 80);
    
    /*
     * Arbre créé:
     *       50
     *      /  \
     *    30    70
     *   /  \   /  \
     *  20  40 60  80
     */
    
    // PARCOURS (toujours demandés en exam!)
    printf("Parcours Infixe (ordre croissant): ");
    parcoursInfixe(racine);
    printf("\n");
    
    printf("Parcours Préfixe: ");
    parcoursPrefixe(racine);
    printf("\n");
    
    printf("Parcours Postfixe: ");
    parcoursPostfixe(racine);
    printf("\n");
    
    // Statistiques
    printf("\nHauteur: %d\n", hauteurArbre(racine));
    printf("Nombre de noeuds: %d\n", compterNoeuds(racine));
}

// ==================== MENU PRINCIPAL ====================

void afficherMenu() {
    printf("\n");
    printf("╔════════════════════════════════════════════════════════╗\n");
    printf("║    GUIDE DES STRUCTURES DE DONNÉES DYNAMIQUES EN C    ║\n");
    printf("╠════════════════════════════════════════════════════════╣\n");
    printf("║  1. Allocation dynamique pour structures              ║\n");
    printf("║  2. Tableau de structures dynamiques                  ║\n");
    printf("║  3. Allocation pour chaînes de caractères             ║\n");
    printf("║  4. Tableaux 2D dynamiques                            ║\n");
    printf("║  5. Listes chaînées simples                           ║\n");
    printf("║  6. Piles (Stack - LIFO)                              ║\n");
    printf("║  7. Files (Queue - FIFO)                              ║\n");
    printf("║  8. Arbres binaires de recherche                      ║\n");
    printf("║  9. Toutes les démonstrations                         ║\n");
    printf("║  0. Quitter                                           ║\n");
    printf("╚════════════════════════════════════════════════════════╝\n");
    printf("Votre choix: ");
}

int main() {
    int choix;
    
    printf("╔════════════════════════════════════════════════════════╗\n");
    printf("║          BIENVENUE DANS LE GUIDE COMPLET DES          ║\n");
    printf("║        STRUCTURES DE DONNÉES DYNAMIQUES EN C          ║\n");
    printf("╚════════════════════════════════════════════════════════╝\n");
    
    do {
        afficherMenu();
        scanf("%d", &choix);
        
        switch(choix) {
            case 1:
                demo_allocation_structure();
                break;
            case 2:
                demo_tableau_structures();
                break;
            case 3:
                demo_allocation_chaines();
                break;
            case 4:
                demo_tableaux_2d();
                break;
            case 5:
                demo_listes_chainees();
                break;
            case 6:
                demo_piles();
                break;
            case 7:
                demo_files();
                break;
            case 8:
                demo_arbres();
                break;
            case 9:
                demo_allocation_structure();
                demo_tableau_structures();
                demo_allocation_chaines();
                demo_tableaux_2d();
                demo_listes_chainees();
                demo_piles();
                demo_files();
                demo_arbres();
                break;
            case 0:
                printf("\nMerci d'avoir utilisé ce guide! Bon courage! 🚀\n");
                break;
            default:
                printf("\nChoix invalide!\n");
        }
        
        if(choix != 0) {
            printf("\nAppuyez sur Entrée pour continuer...");
            getchar();
            getchar();
        }
        
    } while(choix != 0);
    
    return 0;
}