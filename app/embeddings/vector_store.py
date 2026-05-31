# app/embeddings/vector_store.py

from app.embeddings.embedder import get_embedding


AGENT_DESCRIPTIONS = {

    "home":
    """
    home automation,
    smart home,
    light,
    lamp,
    bulb,
    fan,
    switch,
    air conditioner,
    appliance,
    electricity,
    room control,
    bedroom,
    kitchen,
    living room,
    device control
    """,

    "office":
    """
    office work,
    corporate operations,
    email,
    mail,
    meeting,
    conference,
    attendance,
    hr,
    salary,
    employee,
    manager,
    project,
    timesheet,
    leave application,
    document management
    """,

    "doctor":
    """
    healthcare,
    doctor,
    physician,
    medical consultation,
    diagnosis,
    medicine,
    treatment,
    blood pressure,
    bp,
    sugar,
    diabetes,
    fever,
    hospital,
    clinic,
    patient,
    health checkup,
    symptoms,
    prescription
    """,

    "travel":
    """
    travel,
    flight,
    airline,
    hotel,
    accommodation,
    reservation,
    booking,
    tourism,
    vacation,
    trip,
    ticket,
    airport,
    itinerary,
    transport,
    lodging
    """
}


# --------------------------------------------------
# Pre-compute embeddings once at startup
# --------------------------------------------------

AGENT_EMBEDDINGS = {}

for agent, description in AGENT_DESCRIPTIONS.items():

    AGENT_EMBEDDINGS[agent] = get_embedding(
        description
    )


print(
    f"[Embedding Router] Loaded "
    f"{len(AGENT_EMBEDDINGS)} "
    f"agent embeddings."
)