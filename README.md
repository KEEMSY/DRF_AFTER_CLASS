# DRF_AFTER_CLASS

DRF 연습을 기록하는 곳입니다.



<hr>

## App 구성
- [userapp](https://github.com/KEEMSY/DRF_AFTER_CLASS/tree/main/userapp)
- [blog](https://github.com/KEEMSY/DRF_AFTER_CLASS/tree/main/blog)
- [assignment](https://github.com/KEEMSY/DRF_AFTER_CLASS/tree/main/assignmnet)
- [product](https://github.com/KEEMSY/DRF_AFTER_CLASS/tree/main/product)

<br>

<hr>



### `product`
product에 대한 기능이 모여있는 앱입니다.


> **[Models](https://github.com/KEEMSY/DRF_AFTER_CLASS/blob/main/product/models.py)**
- Event


<br>

> **[Serializers](https://github.com/KEEMSY/DRF_AFTER_CLASS/blob/main/product/serializers.py)**
- EventSerialize

<br>

> **[Views](https://github.com/KEEMSY/DRF_AFTER_CLASS/blob/main/product/views.py)** (*APiView를 활용한 CBV*)
- ProductApiView

<br>

<hr>

### `userapp`
유저에 관한 기능들이 모여있는 앱입니다.


> **[Models](https://github.com/KEEMSY/DRF_AFTER_CLASS/blob/main/userapp/models.py)**
- Custom user model 
- UserProfile
- Intertest


<br>

> **[Serializers](https://github.com/KEEMSY/DRF_AFTER_CLASS/blob/main/userapp/serializers.py)**
- UserSerializer
- UserProfileSerializer
- InterestSerializer

<br>

> **[Views](https://github.com/KEEMSY/DRF_AFTER_CLASS/blob/main/userapp/views.py)** (*APiView를 활용한 CBV*)
- UserApiView
- UserView

<br>

<hr>

### `blog`
게시글에 관련된 기능들이 모여있는 앱입니다.
> **[Models](https://github.com/KEEMSY/DRF_AFTER_CLASS/blob/main/blog/models.py)**
- Article
- Category
- Comment

<br>

> **[Permissions](https://github.com/KEEMSY/DRF_AFTER_CLASS/blob/main/blog/permissions.py)**
- CanWriteAfter3Days
- CanWriteAfter3Min(for test)


<br>

> **[Serializers](https://github.com/KEEMSY/DRF_AFTER_CLASS/blob/main/blog/serializers.py)**
- ArticleSerializer
- CategorySerializer
- CommentSerializer(예정)

<br>

> **[Views](https://github.com/KEEMSY/DRF_AFTER_CLASS/blob/main/blog/views.py)** (*APiView를 활용한 CBV*)
- ArticleApiView
- CommentApiView

<br>

<hr>

### `assignment`
DRF 사용을 연습하는 앱입니다.

<br>

<hr>

## 설치
### 1. 터미널

>`pip install django` <br>
`pip install djangorestframework`

### 2. settings.py
```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [ # 기본적인 view 접근 권한 지정
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [ # session 혹은 token을 인증 할 클래스 설정
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_PARSER_CLASSES': [ # request.data 속성에 액세스 할 때 사용되는 파서 지정
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ]
}

INSTALLED_APP = [
    .
    .
    'rest_framework', 

```
<br>
 
<hr>

<div align=center>
    <p>
    <a href="https://github.com/KEEMSY/DRF_AFTER_CLASS/wiki">세부공부기록</a>    
    </p>
</div>




<hr>

<div align=center>
    <p>
        <img src="https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white">
        <img src="https://img.shields.io/badge/Django-4.0.5-0c4b33?logo=django&logoColor=white">
        <a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FKEEMSY%2FDRF_AFTER_CLASS&count_bg=%23C83D3D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
    </p>
</div>
