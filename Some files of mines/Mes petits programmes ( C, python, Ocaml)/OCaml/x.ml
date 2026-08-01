(*EXERCICE FICHE 2*)

let rec taille l =
  match l with
  | [] -> 0
  | x :: xs -> 1 + taille (xs);;

let test1= taille [1; 2; 3; 4; 5]
let () = Printf.printf "La taille de la liste est : %d\n" test1

let rec som_list l =
  match l with
  | [] -> 0
  | x :: xs -> x + som_list (xs);;

let test2 = som_list [1; 2; 3; 4; 5]
let () = Printf.printf "La somme de la liste est : %d\n" test2

let rec product l =
  match l with
  | [] -> 1
  | x :: xs -> x * product (xs);;

let test3 = product [1; 2; 3; 4; 5]
let () = Printf.printf "Le produit de la liste est : %d\n" test3

let rec maximum l =
  match l with
  | [] -> failwith "La liste est vide"
  | [x] -> x
  | x :: xs -> let max_rest = maximum xs in
    if x > max_rest then x else max_rest;;

let test4 = maximum [1; 2; 3; 4; 5]
let () = Printf.printf "Le maximum de la liste est : %d\n" test4

let rec last l =
  match l with
  | [] -> failwith "La liste est vide"
  | [x] -> x
  | x :: xs -> last xs;;

let test5 = last [1; 2; 3; 4; 5]
let () = Printf.printf "Le dernier élément de la liste est : %d\n" test5

let rec penultimate l =
  match l with
  | [] | [_] -> failwith "La liste doit contenir au moins deux éléments"
  | [x; _] -> x
  | x :: xs -> penultimate xs;;

let test6 = penultimate [1; 2; 3; 4; 5]
let () = Printf.printf "L'avant-dernier élément de la liste est : %d\n" test6

let reverse l =
  let rec recur cptl l =
    match l with
    | [] -> cptl
    | x :: xs -> recur (x :: cptl) xs
  in
  recur [] l;;

let test7 = reverse [1; 2; 3; 4; 5]

let rec print_int_list l =
  match l with
  | [] -> ()
  | [x] -> print_int x
  | x :: xs -> print_int x; print_string "; "; print_int_list xs

let () =
  print_string "La liste inversée est : [";
  print_int_list test7;
  print_string "]\n";;



let rec map_i f l =
  match l with
  | [] -> []
  | x :: xs -> f x :: map_i f xs;;

let test8 = map_i (fun x -> x * 2) [1; 2; 3; 4; 5]

let () =
  print_string "La liste après application de map_i est : [";
  print_int_list test8;
  print_string "]\n";;
