# RAG QA 챗봇 샘플 코드

실행 방법과 코드 설명은 `RAG 챗봇 개발 (OpenAI API, Langchain, Streamlit).ipynb` 노트북에 있습니다. Colab 환경에서 실행하는 것을 가정합니다.
- 과거 질문답변 내역을 기억하지 않는 버전: `rag.py`
- 과거 질문답변 내역을 기억하는 버전: `history_rag.py`

## 참고 자료
- Langchain 공식 튜토리얼 (영어) https://python.langchain.com/v0.1/docs/use_cases/question_answering/quickstart/
- 랭체인(langchain) + PDF 기반 질의응답(Question-Answering) (한국어 블로그) https://teddylee777.github.io/langchain/langchain-tutorial-08/
- LangChain RAG 파헤치기: 문서 기반 QA 시스템 설계 방법 - 심화편 (한국어 블로그) https://teddylee777.github.io/langchain/rag-tutorial/ 
- Stremalit 공식 튜토리얼 (영어) https://streamlit.io/generative-ai
- 채팅 내용 저장하는 방법 공식 튜토리얼 (영어) https://python.langchain.com/v0.1/docs/use_cases/question_answering/chat_history/


## 사용 툴

- OpenAI API
    - 임베딩 생성 모델과 LLM을 제공합니다.
    - 모델은 OpenAI의 서버에 올려져 있으므로 민감한 문서나 내용을 넘기지 않도록 주의가 필요합니다.
    - 유료라서 OpenAI API 계정에 돈을 충전해야 합니다. ⚠ ChatGPT Plus와는 다릅니다. ⚠
- Langchain
    - LLM 앱 개발을 위한 프레임워크입니다.
- ChromaDB
    - 문서를 저장할 오픈소스 벡터DB입니다.
- Streamlit
    - 챗봇 UI를 생성하기 위해 사용할 프레임워크입니다.
- localtunnel
    - Streamlit을 실행하기 위해 임시로 코드를 배포합니다.

## 챗봇 답변 성능 높일 수 있는 방법

- LLM에 입력할 프롬프트 개선
- 문서를 벡터DB에 넣기 전에 청크로 나누는 방법 변경 (chunk_size, chunk_overlap)
- 문서 가져오는(retrieve) 방법 개선
- 문서 가져온(retrieve) 후 순위 조정(reranking) 단계 추가
- 더 성능 좋은 모델로 변경
