from sqlalchemy.orm import Session

from src.modules.users.entities.user import User

class DeleteUserService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, uuid: str) -> None:
        #@TODO verificador do usuario para confimar a exclusão de conta
        self._db.query(User).filter(User.uuid == uuid).delete()

        return 'Usuário deletado com sucesso'