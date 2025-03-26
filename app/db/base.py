from sqlalchemy.orm import declarative_base
 
Base = declarative_base()
"""
    declarative_base()는 SQLAlchemy의 "클래스를 테이블로 인식"하게 해주는 함수
    이게 업스면 metadata.create_all() 호출해도 아무 테이블도 안 만들어짐

    Base는 모든 모델이 상속받는 부모클래스이고
    FastAPI 프로젝트에서는 app/db/base.py로 빼두는 게 일반적
"""
