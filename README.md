# |Movie Recommendation Site|



## 0. 기획



#### > 목표 

- 영화 정보 기반 추천 서비스 구성
- 비슷한 취향을 가진 사용자의 추천 영화를 공유 함으로써 영화 정보를 쉽게 접하고 친근감 있는 사용자 환경 개발



#### > 사용 Tools

- Notion
  
  - 협업 tool
  - 업무 계획
  
  ![image-20211125152440396](./img\image-20211125152440396.png)
  
  - 회의록 작성, 문서 공유
  
  ![image-20211125152646702](./img\image-20211125152646702.png)
  
  - 일정 조율
  
  ![image-20211125152342541](./img\image-20211125152342541.png)



- ovenapp
  - UI 프로토 타이핑
- draw.io
  - ERD 제작
- VSCode
  - 프로젝트 프로그래밍 통합 개발 환경
- Chrome
  - 프로젝트 실행 브라우저



#### > UI 구상

- **홈페이지**
  - 사이트 로고
  - nav-bar 
    - 로그인, 로그아웃, 회원가입, 내 프로필
  - 사용자 맞춤 영화 추천
  - 전체 영화 목록
    - 장르에 따라 조회

![image-20211125141442691](./img\image-20211125141442691.png)


- **로그인 / 회원가입**
  - 계정명 중복 방지
  - 비밀번호 불일치 방지



- **프로필**
  - 프로필 이미지
  - 개인정보 수정
  - 추천한 영화 목록
  - 작성한 게시글 및 댓글 목록
  - 요청 받은 비밀 친구 수
  - ~~활동량에 따른 등급 부여~~
  - ~~일정 기준 이상 신고 받을 시 조치~~

![image-20211125141859292](./img\image-20211125141859292.png)



- **영화 상세 정보 (TMDB API 사용)**
  - 영화 상세 정보
    - 포스터
    - 영화 제목
    - 평점
    - 줄거리
    - 예고편 영상
  - 추천하기 버튼
  - 영화에 대한 리뷰 작성
  - ~~해당 영화를 추천한 사용자 목록~~

![image-20211125142228779](./img\image-20211125142228779.png)



- **커뮤니티**
  - 리뷰 목록 시간순 나열
    - 리뷰 제목, 영화제목, 작성자, 작성일 확인 가능
  - 상세 리뷰에서 작성자 프로필로 이동 가능
  - ~~게시판에서 글쓰기 가능~~
    - 영화 상세 정보 페이지에서 바로 작성 가능하도록 수정
  - ~~부적절한 리뷰에 대한 신고 기능~~

![image-20211125142428352](./img\image-20211125142428352.png)



#### > ERD 설계

![image-20211125143448064](./img\image-20211125143448064.png)



- **accounts (사용자 계정)**
  - 아이디, 비밀번호, 개인정보
  - 사용자는 서로 추천 영화를 공유할 수 있도록 N:M 관계 설정

![image-20211125143739842](./img\image-20211125143739842.png)

- **Movies (영화)**
  - 영화 제목, 출시일, 평점, 줄거리, 포스터주소
  - 영화는 여러 장르를 가지고 장르마다 여러 영화가 있음 (N:M relationship)
  - 영화를 여러 사람이 추천할 수 있으며, 한 사용자가 여러 영화를 추천할 수 있음 (N:M relationship)

![image-20211125143955221](./img\image-20211125143955221.png)



- **Community (게시판)**
  - 한 영화에 여러 리뷰 작성 가능 (1:N Relationship)
    - 리뷰 제목, 영화 제목, 영화에 대한 평점, 내용, 작성일, 수정일
  - 한 사용자가 여러 리뷰 작성 가능 (1:N Relationship)
  - 한 리뷰에 대해 여러 댓글 작성 가능 (1:N Relationship)
    - 한 사용자가 여러 댓글 작성 가능 (1:N Relationship)

![image-20211125144019153](./img\image-20211125144019153.png)



## 1. UI 설계



#### > Home 

###### (비회원 - 기본 기능)

- 영화 목록 홈페이지와 게시판으로 이동 가능한 link
- 스크롤을 내리면 목록이 추가되는 infinite scroll
- 포스터로 마우스 오버 시 간략한 세부정보 표시
  - 클릭 시 세부 정보 페이지로 이동

![image-20211125145700052](./img\image-20211125145700052.png)



######  (회원 - 추가 기능) 

- 영화 추천 제공
  - 마우스 오버 시 배경에 관련 영상 자동 재생 및 세부 정보 표시

![image-20211125150427477](./img\image-20211125150427477.png)



#### > 로그인 / 회원가입

- 'Login', 'Signup '버튼클릭 혹은 'enter' 키로 입력 가능
- 회원가입 시 중복 아이디, 비밀번호 불일치 방지

![image-20211125150716327](./img\image-20211125150716327.png)

![image-20211125150653137](./img\image-20211125150653137.png)



#### > Movie detail (영화 상세 정보)

- 영화 정보 및 관련 영상 자동 재생
- 추천 시스템을 통해 나의 추천 목록에 저장 가능
- 로그인 한 사용자는 영화에 대한 리뷰 바로 작성 가능

![image-20211125151100613](./img\image-20211125151100613.png)



#### > Community (리뷰 작성)

- 영화에 대한 평점과 내용 작성

![image-20211125195335743](./img\image-20211125195335743.png)



#### > Community (게시판)

- 여러 영화에 대한 모든 사용자의 리뷰 조회
- 페이지네이션 구현

![image-20211125195727292](./img\image-20211125195727292.png)



#### > Community (리뷰 상세)

- 작성자 클릭 시 작성자 프로필로 이동
- 리뷰에 대한 댓글 작성 가능
- 리뷰 및 댓글 작성자라면 삭제 및 수정 가능
  - 댓글 클릭 시 수정 가능

![image-20211125195939764](./img\image-20211125195939764.png)





#### > 프로필 

- 사용자를 나의 비밀 친구로 등록하여 영화 추천 받을 수 있음
- Menu 탭에서 추천 영화페이지와 영화 리뷰 페이지 전환 가능
- 본인 프로필의 경우 개인 정보 수정 탭 생성

![image-20211125200001646](./img\image-20211125200001646.png)

![image-20211125200010119](./img\image-20211125200010119.png)





## 2. 프로젝트 구현 - Backend (Django)

### <작업자 - 오동근>



#### # 2021.11.18(목) - movies 앱 구현

###### 작업 - API 데이터 수집 및 DB 연동

1. TMDB API 사이트로 요청 보내서 인기있는 영화목록 200개 출력 구현

![image-20211118144627768](./img\image-20211118144627768.png)



2. 가져온 영화정보 django DB에 저장

```python
# movies/view.py

@api_view(['GET'])
def call_data(request):
    tmdb_helper = TMDBHelper(TMDBHelper.api_key)
    request_url = tmdb_helper.get_request_url(region='KR', language='ko')
    genre_url = tmdb_helper.get_genre_url(region='KR', language='ko')
    
    # 장르 목록 수집 및 저장
    data_genre = []
    tmp = requests.get(genre_url).json()
    data_genre.append(tmp.get('genres'))
    for i in range(len(data_genre[0])):
        serializer = GenreSerializer(data=data_genre[0][i])
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 영화 목록 수집 및 저장
    data = []
    for i in range(1, 11):
        request_url += f'&page={i}'
        tmp = requests.get(request_url).json()
        for j in range(20):
            data.append(tmp.get('results')[j])
    
    for i in range(len(data)):
        serializer = MovieSerializer(data=data[i])
        if serializer.is_valid(raise_exception=True):
            movie = serializer.save()

        # 중계 테이블 추가
        g_ids = [Genre.objects.get(pk=g_id) for g_id in data[i].get('genre_ids')]    
        for genre in g_ids:
            movie.genre_ids.add(genre)
```

![image-20211118154335434](./img\image-20211118154335434.png)



3. 요청 구분하기 위해 db에 저장하는 url과 출력하는 url 따로 구현

```python
@api_view(['GET'])
@permission_classes([AllowAny])
def index_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
```



#### # 2021.11.19(금) - movies 앱 구현

###### 작업 - 영화 목록과 장르 목록 사이의 N:M 관계 구축

1. 사용자 영화 추천 기능 구현 (Vue에서 axios 요청)

2. 처음 전체 영화 목록 저장 시 중복 방지를 위한 코드 설계했으나 전체 영화 목록이 없는 상태에서 데이터 가져오는 과정에서 오류 발생

   - 관리자 계정으로 목록 저장할 경우에만 동작하도록 수정

3. 장르 정보 db 저장 완료
   ![image-20211119225603550](./img\image-20211119225603550.png)

4. 영화 목록과 장르 정보 관계 구축 실패

   - 각각의 영화 저장할 때마다 장르 정보 추출하여 개별 저장

     ```python
     # 영화 목록 수집 및 저장
         data = []
         for i in range(1, 11):
             request_url += f'&page={i}'
             tmp = requests.get(request_url).json()
             for j in range(20):
                 data.append(tmp.get('results')[j])
         
         for i in range(len(data)):
             serializer = MovieSerializer(data=data[i])
             if serializer.is_valid(raise_exception=True):
                 movie = serializer.save()
     
             # 중계 테이블 추가
             g_ids = [Genre.objects.get(pk=g_id) for g_id in data[i].get('genre_ids')]    
             for genre in g_ids:
                 movie.genre_ids.add(genre)
     ```

     ![image-20211119225550810](./img\image-20211119225550810.png)



#### # 2021.11.20(토) - accounts앱 구현

###### 회의

1. 메인 페이지에서 accounts_user_movie(중계 테이블) data에 접근 필요
2. [홈페이지] user_id(you)를 기준으로 지금 접속한 계정의 비밀친구 중 한명의 id를 가져와서 그 id가 추천하는 movie_id를 가져와 movie 목록 표시해야 한다.
   - 다른 사람 계정 프로필에 들어가면 그 사람 추천 영화 목록은 그냥 보이도록
   - 내 프로필 페이지에 찜한 유저목록이 있고 그 유저를 클릭하면 그 사람 프로필로 이동

3. 지금 로그인한 계정에서 영화 상세에 들어갔을 때, 추천 버튼을 누르거나 취소할 수 있어야 한다.
   - 누르면 accounts_user_movie에 movie_id(추천누른 영화)와 user_id(현재 로그인 계정) 추가
4. [홈페이지(랜덤영화추천목록)]-> 지금 로그인한 사람의 db에서 내가 비밀친구 맺은 user를 조회해서 user의 추천영화를 가져온다
5. [프로필] -> you를 기준으로 you가 갖고 있는 추천 영화 목록 가져오기 (get)
6. [영화 상세 페이지] -> movie를 기준으로 recommened users를 가져오기



###### 작업 - accounts (계정) 앱 구현

1. accounts 앱에서 비밀 친구 생성 및 추천 영화 목록 조회 함수 구현

   - 특정 사람이 추천한 목록을 db에서 역참조하여 가져온 Queryset이 Json 형태로 반환이 안되는 문제 발생
     - 해당 Queryset에서 제목과 포스터주소만 가져와 리스트 형태로 context에 담아 JsonResponse하여 해결

   ```python
   @api_view(['POST'])
   def secret_friend(request, username):
       person = get_object_or_404(get_user_model(), username=username)
       user = request.user
       if person != user:
           if person.secret_followers.filter(pk=user.pk).exists():
               person.secret_followers.remove(user)
               is_followed = False
           else:
               person.secret_followers.add(user)
               is_followed = True
       context = {
           'is_followed': is_followed,
           # 'secret_following_nums': person.secret_friends.count(),
           'secret_follower_nums': person.secret_followers.count()
       }
       return JsonResponse(context)
   ```

2. client와 server 연동 착수

   - 회원가입 시도 시 제대로 요청 전달 되지 않는 문제 발생 
     - template의 form 태그로 인해 제대로 정보가 전달되지 않음을 발견 후 제거
   - 회원가입은 해결했으나 login은 되지 않는 문제 발생
     - url 요청 시 '-'를 인식하지 못함을 발견하여 수정 
       - '-'를 인식하지 못함이 아니라 url 순서로 인해 str으로 지정된 다른 주소로 할당됨을 확인

3. 로그인 완료되면 홈페이지 이동하여 로그인 상태에선 'logout'과 '프로필' 보이게, 비 로그인 시에는 'login'과 'signup' 보이게 구현



#### # 2021.11.21(일)

###### 작업

1. 회원가입 시 admin 계정명은 사용 불가하도록 설정
2. 비밀 번호 불일치 시 경고 문구 alert으로 front에서 표시
3. admin 계정은 영화 정보 db에 갱신 가능하도록 버튼 생성
4. 영화 포스터 클릭하면 상세 페이지 이동
5. 커뮤니티 작성을 위한 사용자 정보 db 연동 방안 마련
   - 사용자 로그인 시 가져오는 user 정보를 store에 username으로 저장하여 사용자 정보가 필요한 경우마다 사용한다



#### # 2021.11.22(월)

###### 회의

1.  게시글 작성까지 확인
2.  로그아웃 후 재로그인 시 게시판에 안 나타나는 문제 발생 → 추후 해결방안 마련
3.  사용자 프로필 페이지 연동 → 유저 전체 정보도 store에 저장하여 상황에 맞게 조회
4.  추가 작업 : 1. 작성일, 수정일 형태 수정 2. 유튜브 api 방법 찾기



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

     - serializer에 담을 때 created_at의 format을  ("%d-%m-%Y %H:%M:%S") 지정

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

###### 작업

1. Infinite Scroll 구현

   - 영화 목록의 component로 infinite scroll 지정하여 이벤트 발생 시 마다 리스트에 일정량 추가

   ```vue
   <script>
       data: function () {
           return{
               page: 1,
               list: [],
               index: -1,
           }
       },
       methods: {
           infiniteHandler($state) {
             axios.get(api, {
               params: {
                 page: this.page,
               },
             }).then(({ data }) => {
               if (data) {
                 this.page += 1;
                 this.index += 9;
                 for (let i = 8; i >= 0; i--) {
                   this.list.push(data[this.index - i])
                 }
                 $state.loaded()
               } else {
                 $state.complete()
               }
             })
           },
         },
   </script>
   ```

2. 영화 상세 정보 및 추천 영화에서 youtube 영상 자동재생 구현

   - 영화 상세 페이지 시작 시 youtube로 영화 제목에 대한 검색어 결과를 반환 받도록 설계

   - youtube API를 통해 생성한 url 뒤에 autoplay 추가

```
?autoplay=1`
```

3. 랜덤영화 추천 함수 구현 
   - (랜덤영화추천목록) -> 지금 로그인한 사람의 db에서 내가 비밀친구 맺은 user를 조회해서 user의 추천영화를 가져온다 

```python
@api_view(['GET'])
def random_recommend_movies(request):
    secret_friends_recommend_movies = set()
    secret_friends = request.user.secret_friends.all()

    for secret_friend in secret_friends:
        recommended_movies = secret_friend.recommend_movies.all()
        for recommended_movie in recommended_movies:
            secret_friends_recommend_movies.add(recommended_movie)

    serializer = MovieSerializer(list(secret_friends_recommend_movies), many=True)
    return Response(serializer.data)
```



####  # 2021.11.23(수) ~ 2021.11.24(목)

###### 작업

1. 추천 영화에 마우스 오버 시 배경  영상 자동 재생 구현
2. 리뷰, 댓글, 프로필, 영화추천, 비밀 친구 동작 점검
3. 최종 점검 및 인터페이스 세부 수정



#### # 배운점

1. 공식 문서와 구글링을 잘 활용하자
   - 공식 문서 자료만 잘 이해하면 블로그보다 활용이 더 용이하다
2. 작업한 내용은 그날 기록하자
   - 정말 사소한 실수로도 몇 시간을 소비할 수 있다
   - 힘든 작업을 장시간 수행하여 피곤할 수 있다
   - 그래서 기록을 안했더니 지금 작성하는데 기억이 전혀 나지 않는다.
3. 수행할 작업을 정의하고 구현방안을 그리고 나서 시작하자
   - 무작정 생각의 흐름대로 진행하다 처음부터 다시 해야할 수도 있다
4. 코드 공유를 잘하자
   - 내가 한 작업은 분명 비효율적이거나 실수한 부분이 있다
   - 팀원과 작업을 공유하면 훨씬 더 효율적인 코드를 작성할 수 있고 실수를 사전에 방지할 수 있다





## 3. 프로젝트 구현 - Frontend (Vue.js)

### <작업자 - 김종현>

#### 11. 18. 목요일

#### make basic template by vue & vuex

- Router Link를 활용하여 nav bar를 구현
- Login/Signup 페이지의 간략한 화면 구성
- Home 페이지를 영화 추천 컴포넌트와 전체 영화를 조회하는 컴포넌트로 나누어 구성
- 영화 추천 컴포넌트는 Transition과 hover를 사용하여 애니메이션을 구현
- 그리고 이미지 클릭 시 detail 페이지로 넘어가지도록 설계



#### 11. 19. 금요일

- 기본적인 뼈대를 어제에 이어서 마무리
  - 게시판
  - 게시글 상세
  - 프로필
  - 사이드바
- Movie-Genre 데이터를 TMDB에서 가져와서 만드는데 어려움이 있었다. 
  - Movie가 갖고 있는 genre_ids가 여러개인데 id는 하나밖에 적용할 수 없기 때문에 데이터를 가져오는 과정에서 중개 테이블을 만들어줘야 할 것 같은데 방법이 마땅히 떠오르지 않았다. 내일 마무리 예정
- 명일 Back에서 데이터를 받아서 프론트에 적용시키는 작업 예정



#### 11. 20. 토요일

- 수요일에 협업을 통해 프로젝트를 설계하고 계획하였다면 목금에는 분업을 통해 back과 front의 틀을 잡았다.
- 협업을 통해 vue-django 간 데이터 연동을 시도
- 오늘 목표는 user와 movies 데이터를 모두 연동시키는 것이었으나 생각치 못한 난관을 만나서 user데이터 연동에만 성공했다.
- user데이터 연동 시 마주한 첫번째 난관은 signup 시 발생한 "broken pipe error" 였다. 
  - 5개월의 시간동안 처음 만나보는 에러라 도대체 뭐가 문제고 어떻게 해결해야 하는지 구글링을 통해 파헤치고 해결하기까지 거의 3시간은 걸린 것 같다. 
  - broken pipe error 우선 앞선 요청이 끝나지 않았는데 중복해서 빠르게 요청을 재시도할 때 발생하는 오류라고 한다. 나는 signup을 한번 요청했는데 왜 이 에러가 발생하는지 도무지 알 수가 없었다. 
  - 하지만 약 3시간에 걸친 구글링 끝에 stackoverflow에서 나와 같은 상황에 놓인 사람의 글을 발견할 수 있었고 단 한 줄의 답변을 발견했다. " remove form tag, it solves that problem. " 결과는 너무나 허무하게도 vue template에서 form 태그를 사용해서 발생한 에러였다.
- 두번째 난관은 jwt를 적용하면서 발생했다. 
  - jwt를 적용했는데 로그인 시 계속해서 unauthorized 401에러 발생
  - django의 accounts/urls.py에 obtain jwt에 해당하는 url이 교재에는 분명 'api-token-auth/'로 되어있는데 이거를 'api/token/'으로 바꾸니까 정상적으로 작동
  - 아마도 url에 -를 사용한 게 문제가 아닐까 추정하는데 교수님 컴퓨터의 설정과 내 컴퓨터 설정이 달라서 발생한 에러로 추정
- user 데이터 연동은 수업을 했던 부분이기에 금방 끝낼 수 있을거라고 생각했는데 예상치 못한 변수에 너무 오랜 시간을 할애하게 되었다. 그래서 계획했던 다른 옵셔널한 부분에서 포기해야할 부분들이 생길 것 같다.  하지만 에러를 해결하는 과정에서 결국에는 답을 찾아냈기 때문에 좋은 경험이라고 생각한다. 



#### 11. 21. 일요일

- movie 데이터와 review 데이터를 백엔드에서 만들어서 app이 실행될 때 front의 sotre로 가져오는 작업을 처리



#### 11. 22. 월요일

- review detail에서 글쓴이를 클릭하면 user data를 가져와서 router parameter로 넘겨주고 그 데이터를 받아서 page를 시현하는 작업
  - modelserializer에 하위 modelserializer를 추가해서 user_id가 아닌 username을 데이터로 넘겨받을 수 있게 만들었다. 
  - 페어의 내용 확인으로 협업의 중요성을 느낄 수 있었다.
- 페이지 간에 데이터 이동이 복잡하게 되어가고 있다. 그럼에도 초기 설정 변경 없이 진행되고 있는 걸 보니 초기 모델링을 잘 해놓는 것이 얼마나 중요한지 다시 한번 깨닫게 된다!
- 게시판 기능을 완성하고 영화 추천하기 버튼 생성
- 프로필에서 현재 로그인한 유저가 누구든 간에 보여줘야 할 부분은 프로필 유저가 추천한 영화 / 게시한 리뷰 이 두가지 이고 프로필 유저 = 로그인한 유저일 때는 개인정보 수정이다. 
  - 추가로 비밀친구도 로그인 유저가 누구냐에 따라 전자는 비밀친구 맺기 버튼이 있어야 하고 후자는 나를 비밀친구로 몇명이 맺고 있는지 확인 가능하게 만들어야 한다. 
  - 로그인 유저 != 프로필 유저인 경우까지 완성

