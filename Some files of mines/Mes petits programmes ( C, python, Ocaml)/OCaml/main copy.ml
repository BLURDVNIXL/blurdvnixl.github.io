
(* somme des 1/(k +n) pour k allant de 1 a n *)

let somme n=
  let s = ref 0.0 in
  for k = 1 to n do
    s := !s +. 1.0 /. float_of_int (k + n)
  done;
  !s

  (* double somme des ij de 1 à n*)
let double_somme n =
  let s = ref 0 in
  for i = 1 to n do
    for j = 1 to n do
      s := !s + i * j
    done
  done;
  !s


(* Écrire une fonction puissance_inf : int -> int prenant en entrée un entier n supposé
strictement positif et renvoyant la plus grande puissance de 2 inférieure ou égale à n : *)
let puissance_inf n =
  let p = ref 1 in
  while !p <= n do
    p := !p * 2
  done;
  !p / 2

(* test *)
let () =
  let n = 100 in
  Printf.printf "La puissance de 2 inférieure ou égale à %d est : %d\n" n (puissance_inf n)