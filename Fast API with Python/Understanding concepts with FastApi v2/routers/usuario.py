from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/usuarios') # router de efetuação do comando 'get'
async def get_cursos():
    return {'info':'todos os usuarios'}