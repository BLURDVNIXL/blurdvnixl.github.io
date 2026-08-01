(*Gestion d'un etudiant*)

type etudiant = { matricule : string; nom : string; age : int; moyenne : float }

let e1 = { matricule = "12345"; nom = "Alice"; age = 20; moyenne = 0.5 }
let admis x = x.moyenne >= 11.0

let () =
  if admis e1 then
    Printf.printf "%s est admis.\n" e1.nom 
    (*printf.printf est de la forme format-valeur*)
  else
    Printf.printf "%s n'est pas admis.\n" e1.nom

  (*Gestion vehicule*)

type carburant = Essence | Diesel | Electrique
type vehicule = { immatriculation : string; marque : string; annee_de_fabrication : int; carburant : carburant }

let toyota = { immatriculation = "AB-123-CD"; marque = "Toyota"; annee_de_fabrication = 2010; carburant = Essence }
let tesla = { immatriculation = "EF-456-GH"; marque = "Tesla"; annee_de_fabrication = 2020; carburant = Electrique }
let ferrari = { immatriculation = "IJ-789-KL"; marque = "Ferrari"; annee_de_fabrication = 2015; carburant = Diesel }

let est_electrique x = match x.carburant with
  | Electrique -> true
  | _ -> false

let age_vehicule x = 2026 - x.annee_de_fabrication

(* test *)
let () =
  Printf.printf "Age du Toyota : %d\n" (age_vehicule toyota);
  Printf.printf "Age de la Tesla : %d\n" (age_vehicule tesla);
  Printf.printf "Age de la Ferrari : %d\n" (age_vehicule ferrari);
  if est_electrique tesla then
    Printf.printf "%s est électrique.\n" tesla.marque
  else
    Printf.printf "%s n'est pas électrique.\n" tesla.marque