from model.question import Question


class QuestionFindService:
    def get_questions(self, db):
        return db.query(Question).all()