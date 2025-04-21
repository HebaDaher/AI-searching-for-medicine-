% med_knowledge.pl

% Define some symptoms and associated medicines
treats(paracetamol, [fever, headache]).
treats(ibuprofen, [pain, inflammation, fever]).
treats(antacid, [acidity, indigestion]).
treats(antihistamine, [allergy, sneezing]).
treats(amoxicillin, [infection, sore_throat]).

% Get medicine that treats any of the symptoms
recommend_medicine(Symptom, Medicine) :-
    treats(Medicine, Symptoms),
    member(Symptom, Symptoms).