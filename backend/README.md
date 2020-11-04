### 백엔드 실행 방법 



```bash

$ cd backend/
# 가상 환경을 켜줍니다.
$ python -m venv venv
$ source venv/Scripts/activate
# 필요한 설치파일을 다운 받습니다.
$ pip install -r requirements.txt
# 모델링 데이터 베이스에 등록
$ python manage.py makemigrations
$ python manage.py migrate
# 문화재 데이터를 등록합니다.
$ python manage.py loaddata heritage_data_made_cut.json
# 백엔드 실행
$ python manage.py runserver
```

