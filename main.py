from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# 1. Memoria temporal (si la máquina se apaga se pierden los datos) 
alumnos_db = []
profesores_db = []

# 2. Modelos con validaciones (Validar por vacío y por tipo de dato correcto) 
class Alumno(BaseModel):
    id: int
    nombres: str = Field(..., min_length=1)
    apellidos: str = Field(..., min_length=1)
    matricula: str = Field(..., min_length=1)
    promedio: float

class Profesor(BaseModel):
    id: int
    numero_Empleado: int
    nombres: str = Field(..., min_length=1)
    apellidos: str = Field(..., min_length=1)
    horas_Clase: int

# ==========================================
# ENDPOINTS DE ALUMNOS [cite: 10]
# ==========================================

# GET /alumnos [cite: 11]
@app.get("/alumnos", response_model=List[Alumno], status_code=status.HTTP_200_OK)
def obtener_alumnos():
    return alumnos_db

# GET /alumnos/{id} [cite: 13]
@app.get("/alumnos/{id}", response_model=Alumno, status_code=status.HTTP_200_OK)
def obtener_alumno_por_id(id: int):
    for a in alumnos_db:
        if a.id == id:
            return a
    raise HTTPException(status_code=404, detail="Alumno no encontrado") # Uso de código 404 [cite: 24]

# POST /alumnos [cite: 14]
@app.post("/alumnos", response_model=Alumno, status_code=status.HTTP_201_CREATED)
def crear_alumno(alumno: Alumno):
    for a in alumnos_db:
        if a.id == alumno.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    alumnos_db.append(alumno)
    return alumno

# PUT /alumnos/{id} [cite: 15]
@app.put("/alumnos/{id}", response_model=Alumno, status_code=status.HTTP_200_OK)
def actualizar_alumno(id: int, alumno_actualizado: Alumno):
    for i, a in enumerate(alumnos_db):
        if a.id == id:
            alumnos_db[i] = alumno_actualizado
            return alumno_actualizado
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

# DELETE /alumnos/{id} [cite: 16]
@app.delete("/alumnos/{id}", status_code=status.HTTP_200_OK)
def eliminar_alumno(id: int):
    for i, a in enumerate(alumnos_db):
        if a.id == id:
            del alumnos_db[i]
            return {"mensaje": "Alumno eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

# ==========================================
# ENDPOINTS DE PROFESORES [cite: 17]
# (Misma lógica, aplicados al arreglo de profesores_db)
# ==========================================

# GET /profesores [cite: 18]
@app.get("/profesores", response_model=List[Profesor], status_code=status.HTTP_200_OK)
def obtener_profesores():
    return profesores_db

# GET /profesores/{id} [cite: 19]
@app.get("/profesores/{id}", response_model=Profesor, status_code=status.HTTP_200_OK)
def obtener_profesor_por_id(id: int):
    for p in profesores_db:
        if p.id == id:
            return p
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

# POST /profesores [cite: 20]
@app.post("/profesores", response_model=Profesor, status_code=status.HTTP_201_CREATED)
def crear_profesor(profesor: Profesor):
    for p in profesores_db:
        if p.id == profesor.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    profesores_db.append(profesor)
    return profesor

# PUT /profesores/{id} [cite: 21]
@app.put("/profesores/{id}", response_model=Profesor, status_code=status.HTTP_200_OK)
def actualizar_profesor(id: int, profesor_actualizado: Profesor):
    for i, p in enumerate(profesores_db):
        if p.id == id:
            profesores_db[i] = profesor_actualizado
            return profesor_actualizado
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

# DELETE /profesores/{id} [cite: 22]
@app.delete("/profesores/{id}", status_code=status.HTTP_200_OK)
def eliminar_profesor(id: int):
    for i, p in enumerate(profesores_db):
        if p.id == id:
            del profesores_db[i]
            return {"mensaje": "Profesor eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Profesor no encontrado")