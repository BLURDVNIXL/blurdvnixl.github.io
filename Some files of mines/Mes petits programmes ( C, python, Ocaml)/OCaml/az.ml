let rec mem x u = match u with
  | []     -> false          (* liste vide : x absent *)
  | t :: q -> t = x || mem x q
let test1 = mem 9 [1; 2; 3; 4; 5]
let () = Printf.printf "Le nombre 9 est-il dans la liste ? %b\n" test1

let rec nth u n = match u, n with
  | [], _      -> failwith "indice hors bornes"
  | t :: _, 0 -> t                    (* on est arrivé à l'élément voulu *)
  | _ :: q, _ -> nth q (n - 1)     (* on avance dans la liste *)

let test2 = nth [1; 2; 3; 4; 5] 2
let () = Printf.printf "L'élément à l'indice 2 de la liste est : %d\n" test2

let rec take n u = match u, n with
  | [], _     -> []            (* liste trop courte : on renvoie ce qu'on a *)
  | _,  0     -> []            (* on a pris assez d'éléments *)
  | t :: q, _ -> t :: take (n - 1) q

let test3 = take 3 [1; 2; 3; 4; 5]
let () = Printf.printf "Les 3 premiers éléments de la liste sont : %s\n" (String.concat "; " (List.map string_of_int test3))

let rec range a b =
  if a >= b then []
  else a :: range (a + 1) b

let test4 = range 6 6
let () = Printf.printf "La liste des nombres de 6 à 6 est : %s\n" (String.concat "; " (List.map string_of_int test4))

let rec concat u v = match u with
  | []     -> v
  | t :: q -> t :: concat q v

let test5 = concat [1; 2; 3] [9; 5]
let () = Printf.printf "La concaténation des listes est : %s\n" (String.concat "; " (List.map string_of_int test5))

let rec miroir_naif u = match u with
  | []     -> []
  | t :: q -> concat (miroir_naif q) [t]
  (* on place la tête tout à la fin *)

let test6 = miroir_naif [1; 2; 3; 4; 5]
let () = Printf.printf "Le miroir de la liste est : %s\n" (String.concat "; " (List.map string_of_int test6))