# ElasticSearch를 이용한 시맨틱 서치

[소프트웨어공학]을 수강하며 진행된 팀 프로젝트 "GO2SKKU" 중 `ElasticSearch`를 이용한 **시맨틱 서치** API 부분을 간단하게 구현해 보았습니다.

해당 코드는 **윈도우** 환경에서의 실행만 테스트되었습니다.

API는 hashtag와 review에 대해 검색할 수 있게 설계하였습니다.

<br/>

## 프로젝트 환경 구축

```
# python venv 환경 생성 및 활성화
python -m venv your_venv
your_venv/Scripts/activate


# 프로젝트 필수 라이브러리 설치
pip install -r requirements.txt
```

- `ElasticSearch`의 사용을 위해서는 서버를 띄우기 위한 ElasticSearch 다운로드가 추가로 필요합니다.

```
# ElasticSearch 다운로드 : 아래 link에서 Windows를 platform으로 선정하여 다운로드해줍니다.
https://www.elastic.co/kr/downloads/elasticsearch 

# 다운로드 파일 압축 해제
elasticsearch-8.14.0-windows-x86_64.zip를 압축해제 해주시면 됩니다
(경로는 원하는 곳에, 그리고 elasticsearch가 용량을 많이 잡아먹기 때문에, 최대한 용량이 널널한 곳, 최소 50GB 사용가능한 경로를 추천드립니다.)

# ElasticSearch 폴더로 이동
cd elasticsearch-8.14.0/bin

# 한국어 토크나이저 Nori 설치
.\elasticsearch-plugin install analysis-nori
```

<br/>

## 실행 및 인퍼런스

- `ElasticSearch`와의 통신을 위해 **ElasticSearch server**를 실행합니다:
	- _cf. 첫 실행에서 나오는 password를 꼭 기억했다가, main.py에서의 http_auth 부분의 두 번째 문자열을 해당 password로 대체해주셔야 합니다!!

```bash
./elasticsearch-8.14.0/bin/elasticsearch.bat
```

- **Flask API** 서버 실행을 위해 다음 코드를 실행합니다. 첫 실행 시에는 **인덱스 생성**으로 인한 _Latency_ 가 있을 수 있습니다:

```bash
python server.py
```

- **hashtag** 중 검색을 위해 다음 요청을 전송합니다: (windows CMD에서 요청하였습니다.)

```bash
curl -X POST -H "Content-Type: application/json" -d "{ \"query\": \"로봇커피\" }" http://127.0.0.1:5000/hashtag
```
- **review** 중 검색을 위해 다음 요청을 전송합니다:

```bash
curl -X POST -H "Content-Type: application/json" -d "{ \"query\": \"맛있는 자몽\" }" http://127.0.0.1:5000/review
```

<br/>

## 인퍼런스 결과

![](/img/hashtag.png)

- **브런치**와 **로봇커피**를 입력했을 때, `ElasticSearch`가 내놓은 검색결과입니다.

![](/img/review.png)

- **맛있는 자몽**을 입력했을 때, `ElasticSearch`가 내놓은 검색결과입니다.

<br/>

<br/>

## 참조
- [Semantic Search by using FAISS & ElasticSearch](https://github.com/Huffon/semantic-search-faiss)
