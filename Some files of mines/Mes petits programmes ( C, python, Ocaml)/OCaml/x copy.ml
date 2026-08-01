(*1. Écrire une fonction double : int array -> int array qui prend en entrée un tableau
[|x1; ...; xn|] d’entiers et renvoie le tableau [|2 * x1; ...; 2 * xn|].
2. Écrire une fonction mul : int -> int array -> int array qui prend en entrée un entier
a et un tableau [|x1; ...; xn|] et renvoie le tableau [|a * x1; ...; a * xn|].
3. Écrire une fonction affiche : int array -> unit qui prend en entrée un tableau d’en-
tiers et affiche ces entiers dans l’ordre du tableau, un entier par ligne.*)

let double arr =
  let n = Array.length arr in
  let res = Array.make n 0 in
  for i = 0 to n - 1 do
    res.(i) <- 2 * arr.(i)
  done;
  res

let mul a arr =
  let n = Array.length arr in
  let res = Array.make n 0 in
  for i = 0 to n - 1 do
    res.(i) <- a * arr.(i)
  done;
  res

let affiche arr =
  let n = Array.length arr in
  for i = 0 to n - 1 do
    Printf.printf "%d\n" arr.(i)
  done
