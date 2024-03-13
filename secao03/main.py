from typing import Dict, List, Optional, Any
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header

from models import Curso

app = FastAPI(
    title='API do Fabinho',
    version='0.01'
)

cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },

    2: {
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 87,
        "horas": 67
    }
}

##### ENDPOINT GET #####

@app.get('/cursos',
         description='Retorna os cursos disponiveis.', 
         summary='Pode retornar todos os cursos ou uma lista vazia.',
         response_model=List[Curso],
         response_description='Cursos encontrados com sucesso.'
         )
async def get_cursos():
    return cursos

##### ENDPOINT GET ID #####

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(title='ID do Curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

##### ENDPOINT POST #####

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

##### ENDPOINT PUT #####

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe um curso com essa ID = {curso_id}')
    

##### ENDPOINT DELETE #####
          
@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe um curso com essa ID = {curso_id}')





##### SERVIDOR MAIN #####

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)