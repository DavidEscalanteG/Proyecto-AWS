from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

alumnos_db = []
profesores_db = []

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

@app.get("/alumnos", response_model=List[Alumno], status_code=status.HTTP_200_OK)
def obtener_alumnos():
    return alumnos_db

@app.get("/alumnos/{id}", response_model=Alumno, status_code=status.HTTP_200_OK)
def obtener_alumno_por_id(id: int):
    for a in alumnos_db:
        if a.id == id:
            return a
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

@app.post("/alumnos", response_model=Alumno, status_code=status.HTTP_201_CREATED)
def crear_alumno(alumno: Alumno):
    for a in alumnos_db:
        if a.id == alumno.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    alumnos_db.append(alumno)
    return alumno

@app.put("/alumnos/{id}", response_model=Alumno, status_code=status.HTTP_200_OK)
def actualizar_alumno(id: int, alumno_actualizado: Alumno):
    for i, a in enumerate(alumnos_db):
        if a.id == id:
            alumnos_db[i] = alumno_actualizado
            return alumno_actualizado
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

@app.delete("/alumnos/{id}", status_code=status.HTTP_200_OK)
def eliminar_alumno(id: int):
    for i, a in enumerate(alumnos_db):
        if a.id == id:
            del alumnos_db[i]
            return {"mensaje": "Alumno eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

@app.get("/profesores", response_model=List[Profesor], status_code=status.HTTP_200_OK)
def obtener_profesores():
    return profesores_db

@app.get("/profesores/{id}", response_model=Profesor, status_code=status.HTTP_200_OK)
def obtener_profesor_por_id(id: int):
    for p in profesores_db:
        if p.id == id:
            return p
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

@app.post("/profesores", response_model=Profesor, status_code=status.HTTP_201_CREATED)
def crear_profesor(profesor: Profesor):
    for p in profesores_db:
        if p.id == profesor.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    profesores_db.append(profesor)
    return profesor

@app.put("/profesores/{id}", response_model=Profesor, status_code=status.HTTP_200_OK)
def actualizar_profesor(id: int, profesor_actualizado: Profesor):
    for i, p in enumerate(profesores_db):
        if p.id == id:
            profesores_db[i] = profesor_actualizado
            return profesor_actualizado
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

@app.delete("/profesores/{id}", status_code=status.HTTP_200_OK)
def eliminar_profesor(id: int):
    for i, p in enumerate(profesores_db):
        if p.id == id:
            del profesores_db[i]
            return {"mensaje": "Profesor eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Profesor no encontrado")
