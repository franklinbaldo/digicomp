/-!
Experimental candidate models, NOT a formal specification of the DR-70.
Angles are natural numbers in centidegrees; no original output is claimed.
-/
namespace DR70Candidates

def circle : Nat := 36000
def sign : Nat := 3000

def equalHouse (asc index : Nat) : Nat := (asc + sign * index) % circle
def wholeSign (asc index : Nat) : Nat := ((asc / sign) * sign + sign * index) % circle

def fieldIndex (index : Fin 12) : Nat := index.val + 1

theorem same_labels (index : Fin 12) : fieldIndex index = fieldIndex index := rfl

theorem coincide_at_sign_boundary (index : Fin 12) :
    equalHouse 3000 index.val = wholeSign 3000 index.val := by
  simp [equalHouse, wholeSign, sign, circle]

theorem diverge_at_15_25 : equalHouse 1525 0 ≠ wholeSign 1525 0 := by
  decide

end DR70Candidates
