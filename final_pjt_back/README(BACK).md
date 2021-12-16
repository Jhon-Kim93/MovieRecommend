# [back]



#### # 2021.11.18(목)

1. TMDB API 사이트로 요청 보내서 영화목록 200개 출력 구현

![image-20211118144627768](C:\Users\오동근\AppData\Roaming\Typora\typora-user-images\image-20211118144627768.png)



2. 가져온 영화정보 django DB에 저장

![image-20211118154411223](C:\Users\오동근\AppData\Roaming\Typora\typora-user-images\image-20211118154411223.png)

![image-20211118154335434](C:\Users\오동근\AppData\Roaming\Typora\typora-user-images\image-20211118154335434.png)



3. 요청 구분하기 위해 db에 저장하는 url과 출력하는 url 따로 구현

![image-20211119001010024](C:\Users\오동근\AppData\Roaming\Typora\typora-user-images\image-20211119001010024.png)



#### # 2021.11.19(금)

1. 사용자가 영화에 추천 선택하는 기능 구현(추후 Vue에서 axios 요청 보내서 확인 필요)
2. 처음 전체 영화 목록 저장 시 중복 방지를 위한 코드 설계했으나 전체 영화 목록이 없는 상태에서 데이터 가져오는 과정에서 오류 발생
   - 추후 수정
3. 장르 정보 db 저장 완료
   ![image-20211119225603550](C:\Users\오동근\AppData\Roaming\Typora\typora-user-images\image-20211119225603550.png)
4. 영화 목록과 장르 정보 관계 구출 실패
   - 각각의 영화 저장할 때마다 장르 정보 추출하여 개별 저장
     ![image-20211119225529725](C:\Users\오동근\AppData\Roaming\Typora\typora-user-images\image-20211119225529725.png)
   - ![image-20211119225550810](C:\Users\오동근\AppData\Roaming\Typora\typora-user-images\image-20211119225550810.png)



#### # 2021.11.20(토)

###### 회의

1. 메인 페이지에서 accounts_user_movie(중계 테이블) data에 접근 필요
2. [홈페이지] user_id(you)를 기준으로 지금 접속한 계정의 비밀친구 중 한명의 id를 가져와서 그 id가 추천하는 movie_id를 가져와서 movie 목록 표시해야한다.
   - 다른 사람 계정 프로필에 들어가면 그 사람 추천 영화 목록은 그냥 보이도록
   - 내 프로필 페이지에 찜한 유저목록이 있고 그 유저를 클릭하면 그 사람 프로필로 이동

3. 지금 로그인 계정에서 영화 상세에 들어갔을 때, 추천 버튼을 누르거나 취소할 수 있어야 한다.
   - 누르면 accounts_user_movie에 movie_id(추천누른 영화)와 user_id(현재 로그인 계정) 추가
4. 홈페이지(랜덤영화추천목록) -> 지금 로그인한 사람의 db에서 내가 몰래친구 맺은 user를 조회해서 user의 추천영화를 가져온다
5. 프로필 -> you를 기준으로 you가 갖고 있는 추천 영화 목록 가져오기 (get)
6. 영화 상세 페이지 -> movie를 기준으로 recommened users를 가져오기



###### 작업

1. accounts 앱에서 비밀 친구 생성 및 추천 영화 목록 조회 함수 구현
   - 특정 사람이 추천한 목록을 db에서 역참조하여 가져온 Queryset이 Json 형태로 반환이 안되는 문제 발생
     - 해당 Queryset에서 제목과 포스터주소만 가져와 리스트 형태로 context에 담아 JsonResponse하여 해결
2. client와 server 연동 착수
   - 회원가입 시도 시 제대로 요청 전달 되지 않는 문제 발생 
     - template의 form 태그로 인해 제대로 정보가 전달되지 않음을 발견 후 제거
   - 회원가입은 해결했으나 login은 되지 않는 문제 발생
     - url 요청 시 '-'를 인식하지 못함을 발견하여 수정 
3. 로그인 완료되면 홈페이지 이동하여 로그인 상태에선 'logout'과 '프로필' 보이게, 비 로그인 시에는 'login'과 'signup' 보이게 구현



#### # 2021.11.21(일)

###### 작업

1. 회원가입 시 admin 계정명은 사용 불가
2. 비밀 번호 불일치 시 경고 문구 alert
3. admin 계정은 영화 정보 db에 갱신 가능하도록 버튼 생성
4. 영화 포스터 클릭하면 상세 페이지 이동
5. 커뮤니티 작성을 위한 사용자 정보 db 연동 방안 마련
   - 사용자 로그인 시 가져오는 user 정보를 store에 username으로 저장하여 사용자 정보가 필요한 경우마다 사용한다
6. 



#### # 2021.11.22(월)

###### 회의

1.  게시글 작성까지 확인
2. 로그아웃 후 재로그인 시 게시판에 안 나타나는 문제 발생 → 추후 해결방안 마련
3. 사용자 프로필 페이지 연동 → 유저 전체 정보도 store에 저장하여 상황에 맞게 조회
4. 추가 작업 : 1. 작성일, 수정일 형태 수정 2. 유튜브 api 방법 찾기



###### 작업

1. 영화 상세 페이지에서 영화 추천 기능 구현

   - 추천 여부에 따라 버튼 토글

   - 페이지 이동 혹은 재로그인 시에도 추천 정보를 확인할 수 있도록 현재 영화 정보에 추천한 사람 목로 중 현재 이용자 있는지 확인하여 isRecommended 값 변경

   - ```vue
     <script>
     export default {
     created: function () {
         const username = this.$store.state.username
         const checkuser = this.movie[0].recommend_users.filter(recommend_user => {
           return recommend_user.username === username
         })
         if (checkuser[0].username === username) {
           this.isRecommended = true
         } else {
           this.isRecommended = false
         }
       }
     }
     </script>
     ```

2. 전체 리뷰 목록과 리뷰 세부 정보에서 사용자 정보 접근이 어려운 문제 발생

   - back에서 리뷰 serializer에 user와 movie를 세부 serializer에 담아서 정보 전달

   - ```python
     class ReviewSerializer(serializers.ModelSerializer):
         class UserSerializer(serializers.ModelSerializer):
             class Meta:
                 model = get_user_model()
                 fields = ('username', 'password',)
     
         user = UserSerializer(read_only=True)
     
         class MovieSerializer(serializers.ModelSerializer):
             class Meta:
                 model = Movie
                 fields = ('pk', 'title',)
         
         movie = MovieSerializer(read_only=True)
     
         class Meta:
             model = Review
             fields = '__all__'
     ```

3. 프로필 페이지 기본 형태 구현

   - 프로필 해당 user의 추천 영화 목록
   - 프로필 해당 user의 작성한 리뷰 목록

4. 리뷰 작성일자 형태 변경

   - 시도 방법

     -  serializer에 담을 때 created_at의 format을  ("%d-%m-%Y %H:%M:%S") 지정

     - 원래 표시되던 문자열을 새롭게 지정

       - ```python
         import datetime
         
         datetime_str = '2016-05-18T15:37:36.993048Z'
         old_format = '%Y-%m-%dT%H:%M:%S.%fZ'
         new_format = '%d-%m-%Y %H:%M:%S'
         
         new_datetime_str = datetime.datetime.strptime(datetime_str, old_format).strftime(new_format)
         print(new_datetime_str)
         #'18-05-2016 15:37:36'
         ```

     - settings.py에 'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S"  설정

   - 배운점

     - USE_L10N은 로컬 형태 지정이 settings.py보다 우선 시 되는 것
     - USE_TZ는 표준 시간대 +9를 표시하는 것

   - 해결 방법 : REST_FRAMEWORK 설정 안에 DATETIME_FORMAT을 지정해 준다

```python
# settings.py

USE_L10N = False

USE_TZ = False

REST_FRAMEWORK = {
    ...
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S" 
}
```



#### # 2021.11.23(화)



```
?autoplay=1`
```

