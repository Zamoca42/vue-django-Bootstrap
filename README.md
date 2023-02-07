# vue-django-blog(작성중)

## 장고 베이스 만들기

- MVT 패턴

   1. settings.py

   2. M. models.py

   3. Urls.py

   4. V. views.py

   5. T. Template/\*.html
      - vue.js


- sqlite -> mysql
   - 전체 개발과정에서 스키마가 정의 되기 전에는 sqlite를 사용하고 완전히 정의 된 후에는 mysql로 마이그레이션
   - django ORM이 잘되어 있기때문에 마이그레이션에는 큰 문제가 없음

- settings 수정
   - 보안에 민감한 SECRET_KEY를 보호할 목적으로 settings.py를 개발용과 product용으로 분리
      - 환경변수패턴 vs 비밀파일패턴
   - manage.py에서 개발용 setting을 호출
   - wsgi.py에서 운영용 setting을 호출
   - \[참고\]
      - https://velog.io/@harukawa99/Django-Django-Settings.py-%EB%B6%84%EB%A6%AC%ED%95%98%EA%B8%B0
      - https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/

- html 수정
   - templete tag를 이용하여 src, href 태그에 static폴더 경로 설정해주기
   - vscode에서 home.html을 변경할 때 정규표현식을 이용하여 바꿔준 부분이 인상적  
      ![스크린샷 2023-02-06 오후 9 47 06](https://user-images.githubusercontent.com/96982072/216975941-3dc93b9b-4286-41f5-aa46-960b04386c4a.png)

- https://djangopackages.org/

