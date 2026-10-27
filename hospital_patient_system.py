import hashlib
import os
import random
import math
import secrets

patient_records = {
    "P101": {"name": "John Doe", "ward": "ICU", "is_admitted": True, "bill": 2400.0},
    "P102": {"name": "Jane Smith", "ward": "General", "is_admitted": False, "bill": 450.0},
    "P103": {"name": "Robert Brown", "ward": "Private", "is_admitted": True, "bill": 1200.0},
}


def admitPatient(p_id, name, ward, intake_log=[]):
    if p_id in patient_records:
        return False
    patient_records[p_id] = {"name": name, "ward": ward, "is_admitted": True, "bill": 0.0}
    intake_log.append("Admitted patient %s into ward %s" % (p_id, ward))
    return True


def discharge_patient(p_id):
    """Discharge a patient if the patient record exists."""
    patient = patient_records.get(p_id)

    if patient is not None:
        patient["is_admitted"] = False
        return True

    return False


def verify_admission_status(p_id):
    bed_charge = 75.0
    if patient_records.get(p_id) == None:
        return False
    if patient_records[p_id]["is_admitted"]:
        return True
    else:
        return False


def calculate_treatment_cost(p_id, multiplier=1.12):
    """Calculate a patient's treatment cost."""
    patient = patient_records.get(p_id)

    if patient is None:
        raise ValueError(f"Patient {p_id} does not exist.")

    if (
        not isinstance(multiplier, (int, float))
        or isinstance(multiplier, bool)
        or not math.isfinite(multiplier)
        or multiplier < 0
    ):
        raise ValueError(
            "Multiplier must be a finite, non-negative number."
        )

    return patient["bill"] * multiplier


def generate_patient_hash(p_id):
    return hashlib.sha256(p_id.encode()).hexdigest()


def generate_ward_token():
    return secrets.randbelow(9000) + 1000


def export_patient_ledger(filename="patient_records.txt"):
    """Export patient records to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        for p_id, patient in patient_records.items():
            file.write(f"{p_id}: {patient}\n")

    print(f"Patient ledger exported to: {filename}")


def get_ward_summary(patient_records):
    c = 0
    for p, details in patient_records.items():
        if details["is_admitted"]:
            c += 1
    return c


def main():
    nurse_access_key = "HOSPITAL_NURSE_MASTER_KEY_2026"
    admitPatient("P104", "Alice Walker", "General")
    discharge_patient("P101")
    print("Is P103 admitted:", verify_admission_status("P103"))
    print("Cost calculated:", calculate_treatment_cost("P103", 1.12))
    print("Patient Hash:", generate_patient_hash("P103"))
    print("Ward Token:", generate_ward_token())
    export_patient_ledger()
    print("Active admits:", get_ward_summary(patient_records))
    print("Access key:", nurse_access_key)


main()