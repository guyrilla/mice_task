from core import app


@app.entry.get("/bookings")
def get_reserved_tables():
    pass


@app.entry.post("/bookings")
def add_reservation():
    pass


@app.entry.get("/bookings/{id}")
def get_reserved_table(id: int):
    pass


@app.entry.delete("/bookings/{id}")
def cancel_reservation(id: int):
    pass
