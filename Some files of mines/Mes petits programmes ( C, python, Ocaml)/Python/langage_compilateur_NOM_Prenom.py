# =============================================================================
# NeoLang — Compilateur simplifié
# =============================================================================
#
# Syntaxe du langage :
#   x = 10
#   y = 3 + x * 2
#   print("Résultat : " + y)
#
# Mots-clés : print
# Opérateurs : + - * /
# Commentaires : # jusqu'à la fin de la ligne
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
# ÉTAPE 1 — LEXER
# On lit le texte caractère par caractère et on produit une liste de tokens
# Chaque token est un tuple : (type, valeur)
# ─────────────────────────────────────────────────────────────────────────────

def lex(source):
    tokens = []
    i = 0

    while i < len(source):
        c = source[i]

        # Espaces et sauts de ligne → on ignore
        if c in ' \t\n\r':
            i += 1
            continue

        # Commentaire → on ignore jusqu'à la fin de la ligne
        if c == '#':
            while i < len(source) and source[i] != '\n':
                i += 1
            continue

        # Nombre (entier ou flottant)
        if c.isdigit():
            num = ''
            est_float = False
            while i < len(source) and (source[i].isdigit() or source[i] == '.'):
                if source[i] == '.':
                    est_float = True
                num += source[i]
                i += 1
            if est_float:
                tokens.append(('FLOAT', float(num)))
            else:
                tokens.append(('INT', int(num)))
            continue

        # Chaîne de caractères
        if c == '"':
            i += 1
            s = ''
            while i < len(source) and source[i] != '"':
                s += source[i]
                i += 1
            if i >= len(source):
                raise Exception("Erreur : chaîne non fermée")
            i += 1  # on passe le " fermant
            tokens.append(('STRING', s))
            continue

        # Identifiant ou mot-clé (ex: x, total, print)
        if c.isalpha() or c == '_':
            nom = ''
            while i < len(source) and (source[i].isalnum() or source[i] == '_'):
                nom += source[i]
                i += 1
            if nom == 'print':
                tokens.append(('PRINT', 'print'))
            else:
                tokens.append(('IDENT', nom))
            continue

        # Opérateurs et symboles
        if c == '+': tokens.append(('PLUS',   '+')); i += 1; continue
        if c == '-': tokens.append(('MINUS',  '-')); i += 1; continue
        if c == '*': tokens.append(('STAR',   '*')); i += 1; continue
        if c == '/': tokens.append(('SLASH',  '/')); i += 1; continue
        if c == '(': tokens.append(('LPAREN', '(')); i += 1; continue
        if c == ')': tokens.append(('RPAREN', ')')); i += 1; continue
        if c == '=': tokens.append(('ASSIGN', '=')); i += 1; continue

        raise Exception(f"Erreur : caractère inconnu '{c}'")

    tokens.append(('EOF', None))
    return tokens


# ─────────────────────────────────────────────────────────────────────────────
# ÉTAPE 2 — PARSER
# On transforme la liste de tokens en arbre (AST)
# L'arbre est fait de listes : ['type', ...]
#
# Exemples :
#   ['number', 42]
#   ['binop', '+', ['number', 3], ['number', 5]]
#   ['assign', 'x', ['number', 10]]
#   ['print', ['number', 42]]
#
# La priorité * / > + - est gérée par la hiérarchie :
#   parse_expr   → + -
#   parse_terme  → * /
#   parse_facteur → nombres, variables, parenthèses
# ─────────────────────────────────────────────────────────────────────────────

tokens = []   # liste globale de tokens
pos = 0       # position courante

def current():
    return tokens[pos]

def avancer():
    global pos
    pos += 1

def manger(type_attendu):
    tok = current()
    if tok[0] != type_attendu:
        raise Exception(f"Erreur de syntaxe : attendu '{type_attendu}', trouvé '{tok[0]}'")
    avancer()
    return tok

def parse_programme():
    instructions = []
    while current()[0] != 'EOF':
        instructions.append(parse_instruction())
    return instructions

def parse_instruction():
    tok = current()

    # print(expression)
    if tok[0] == 'PRINT':
        avancer()
        manger('LPAREN')
        expr = parse_expr()
        manger('RPAREN')
        return ['print', expr]

    # x = expression
    if tok[0] == 'IDENT':
        nom = tok[1]
        avancer()
        manger('ASSIGN')
        expr = parse_expr()
        return ['assign', nom, expr]

    raise Exception(f"Erreur : instruction inconnue '{tok[1]}'")

def parse_expr():
    # + et - : priorité basse
    gauche = parse_terme()
    while current()[0] in ('PLUS', 'MINUS'):
        op = current()[1]
        avancer()
        droite = parse_terme()
        gauche = ['binop', op, gauche, droite]
    return gauche

def parse_terme():
    # * et / : priorité haute
    gauche = parse_facteur()
    while current()[0] in ('STAR', 'SLASH'):
        op = current()[1]
        avancer()
        droite = parse_facteur()
        gauche = ['binop', op, gauche, droite]
    return gauche

def parse_facteur():
    tok = current()

    # Négation : -x
    if tok[0] == 'MINUS':
        avancer()
        return ['neg', parse_facteur()]

    # Parenthèses
    if tok[0] == 'LPAREN':
        avancer()
        node = parse_expr()
        manger('RPAREN')
        return node

    if tok[0] == 'INT':
        avancer(); return ['number', tok[1]]

    if tok[0] == 'FLOAT':
        avancer(); return ['number', tok[1]]

    if tok[0] == 'STRING':
        avancer(); return ['string', tok[1]]

    if tok[0] == 'IDENT':
        avancer(); return ['ident', tok[1]]

    raise Exception(f"Erreur : expression attendue, trouvé '{tok[1]}'")


# ─────────────────────────────────────────────────────────────────────────────
# ÉTAPE 3 — INTERPRÉTEUR
# On parcourt l'arbre et on exécute chaque nœud
# ─────────────────────────────────────────────────────────────────────────────

variables = {}   # stocke les variables : {'x': 10, 'y': 23, ...}

def evaluer(node):
    """Calcule la valeur d'une expression."""

    if node[0] == 'number':
        return node[1]

    if node[0] == 'string':
        return node[1]

    if node[0] == 'ident':
        nom = node[1]
        if nom not in variables:
            raise Exception(f"Erreur : variable '{nom}' non définie")
        return variables[nom]

    if node[0] == 'neg':
        return -evaluer(node[1])

    if node[0] == 'binop':
        op    = node[1]
        gauche = evaluer(node[2])
        droite = evaluer(node[3])

        # Si l'un des deux est une chaîne et op est +, on concatène
        if op == '+' and (isinstance(gauche, str) or isinstance(droite, str)):
            return str(gauche) + str(droite)

        if op == '+': return gauche + droite
        if op == '-': return gauche - droite
        if op == '*': return gauche * droite
        if op == '/':
            if droite == 0:
                raise Exception("Erreur : division par zéro")
            return gauche / droite

def executer(node):
    """Exécute une instruction."""

    if node[0] == 'assign':
        variables[node[1]] = evaluer(node[2])

    elif node[0] == 'print':
        val = evaluer(node[1])
        # Si c'est 4.0, on affiche 4
        if isinstance(val, float) and val == int(val):
            print(int(val))
        else:
            print(val)

def run(instructions):
    for instr in instructions:
        executer(instr)


# ─────────────────────────────────────────────────────────────────────────────
# POINT D'ENTRÉE
# ─────────────────────────────────────────────────────────────────────────────

def executer_fichier(nom_fichier):
    global tokens, pos, variables

    with open(nom_fichier, 'r', encoding='utf-8') as f:
        source = f.read()

    tokens = lex(source)
    pos = 0
    variables = {}

    ast = parse_programme()
    run(ast)


# ─────────────────────────────────────────────────────────────────────────────
# TESTS
# ─────────────────────────────────────────────────────────────────────────────

def run_tests():
    import io, sys

    ok = 0; ko = 0

    def test(nom, fn):
        nonlocal ok, ko
        try:
            fn(); print(f"  [PASS] {nom}"); ok += 1
        except Exception as e:
            print(f"  [FAIL] {nom} → {e}"); ko += 1

    def executer_source(source):
        global tokens, pos, variables
        tokens = lex(source); pos = 0; variables = {}
        ast = parse_programme()
        buf = io.StringIO(); sys.stdout = buf
        run(ast)
        sys.stdout = sys.__stdout__
        return buf.getvalue().strip()

    print("\n── Lexer ────────────────────────────────────────────────────────")
    test("entier 42",          lambda: None if lex("42")[0] == ('INT', 42) else (_ for _ in ()).throw(Exception("raté")))
    test("flottant 3.14",      lambda: None if lex("3.14")[0][0] == 'FLOAT' else (_ for _ in ()).throw(Exception("raté")))
    test("chaîne non fermée",  lambda: (lambda: lex('"oups'))() if False else _attend_erreur(lambda: lex('"oups')))
    test("commentaire ignoré", lambda: None if lex("# test")[0][0] == 'EOF' else (_ for _ in ()).throw(Exception("raté")))

    print("\n── Interpréteur ─────────────────────────────────────────────────")
    test("affectation + lecture",  lambda: _eq(executer_source("x = 7\nprint(x)"), "7"))
    test("2 + 3 * 4 = 14",        lambda: _eq(executer_source("x = 2+3*4\nprint(x)"), "14"))
    test("(2+3)*4 = 20",          lambda: _eq(executer_source("x=(2+3)*4\nprint(x)"), "20"))
    test("10-3-2 = 5",            lambda: _eq(executer_source("x=10-3-2\nprint(x)"), "5"))
    test("concaténation str+int", lambda: _eq(executer_source('x=23\nprint("val : "+x)'), "val : 23"))

    print(f"\n── {ok} réussis, {ko} échoués ──────────────────────────────────\n")

def _eq(a, b):
    if a != b: raise Exception(f"Attendu {repr(b)}, obtenu {repr(a)}")

def _attend_erreur(fn):
    try:
        fn(); raise Exception("Erreur attendue mais pas levée")
    except Exception as e:
        if "Erreur attendue" in str(e): raise


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2 or sys.argv[1] == '--test':
        run_tests()
    else:
        executer_fichier(sys.argv[1])
