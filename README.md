
# 머신러닝을 활용한 내일의 미세먼지수치 예측 서비스   

    팀명 : KDK 
  
    결과물 브랜드명 : 엄마눈이따가와   
  
  
# 프로젝트 개요
  다들 한 번쯤 은 외출하려고 마음먹었는데 창문너머 뿌연 하늘을 본 순간 결심이 흔들린 적이 있을 것입니다. 과거 봄에만 만연했던 황사를 넘어, 이제는 계절을 타지 않고 미세먼지가 서울 하늘을 뒤덮는 시대가 왔습니다.
  
  미세먼지는 우리 몸에 심각한 악영향을 줍니다. 장기간 미세먼지에 노출될 경우 면역력이 급격히 저하되어 감기, 천식, 기관지염 등의 호흡기 질환은 물론 심혈관 질환, 피부질환, 안구질환 등 각종질병에 노출될 수 있습니다. 특히 직경 2.5㎛ 이하의 초미세먼지는 인체 내 기관지 및 폐 깊숙한 곳까지 침투하기 쉬워 기관지, 폐 등에 붙어 각종 질환을 유발합니다. 또한 최근 연구에서는 뇌질환과 암을 유발하는 것이 밝혀졌습니다. 

  근본적으로 대기 질의 개선이라는 해결책이 불가능한 지금 시점에서 우리는 최대한으로 대비하고 피해를 입지 않도록 예방해야 합니다.    
  저희는 이러한 미세먼지의 심각성에 대해 미리 경각심을 가지고 대비할 수 있도록 사람들에게 내일의 미세먼지 수치를 예측해서 알려주는 '엄마눈이따가와'를 통해 편의를 제공하고자 합니다.   
    
  이것을 돕기 위해 '엄마눈이따가와'는 미세먼지 예측 수치를 사용자에게 알려주고, 사용자가 야외활동 계획을 세우는데 참고하거나 마스크를 미리 준비하는 등 실질적인 대응책을 갖출 수 있도록 도와줄 것입니다. 


# 프로젝트 상세
  
  비교적 정확한 대기상태를 측정하기 위해 고도가 높은 건물 창문 밖에 미세먼지 센서, 풍속센서, 습도 센서, 온도 센서를 설치합니다.
  이 센서들에서는 매 시간 단위로 미세먼지 농도, 온도, 풍속, 습도를 측정하여 실시간 대기정보를 서버에 전송합니다.
  서버는 이 수치들을 현재 시간과 함께 데이터베이스에 저장합니다.

  과거의 날씨, 풍향, 미세먼지 데이터를 사용하여 PYTHON KERAS를 이용해 Convolution Neural Network 모델을 만듭니다.  
  이 모델은 시간, 온도, 풍속, 습도 등의 대기정보를 토대로 내일의 미세먼지 수치를 예측하도록 만들어집니다.
  데이터가 일정량 모일 때 마다 다시 학습하여 모델을 갱신합니다.

  클라이언트가 서버에 현재 시간, 온도, 풍속, 습도의 정보를 보내면, 이를 토대로 CNN 모델은 내일의 미세먼지 농도를 예측하여 클라이언트에 전송해줍니다.
  추가적으로, WHO에서 정한 미세먼지 등급체계에 따라 위험레벨을 안내 해 주는 기능도 들어갑니다.
 
 
# 예상 시스템 구성도

  <img src="https://user-images.githubusercontent.com/21076531/79040721-7feb9080-7c25-11ea-933e-2ef4f221ae83.png" width="100%" height="100%" title="" alt="SYSTEM"></img>



# 기대성과
  
  내일의 미세먼지 농도를 예측하여 야외활동 계획을 세우고 대비할 수 있고, 산업현장에서 일정을 조율할 수 있도록 도울 수 있을것입니다.
  
  
# Teammates
  
  강동욱
  
    역할 : 데브옵스, 서버 개발, 발표자
  
    핵심기여역량 : 시스템 설계, 프로젝트 관리, 서버 개발

  <img src="https://user-images.githubusercontent.com/21076531/79041137-508a5300-7c28-11ea-9024-f9688c5ca3b4.jpg" width="256px" height="256px" title="강동욱" alt="강동욱"></img>
    
  오새암
  
    역할 : 아이디어 고안, 소스 개발
    
    핵심기여역량 : 소스 개발, 아두이노 설계, 시장 분석
    
    <img src="https://user-images.githubusercontent.com/50190325/79058904-92f67300-7cae-11ea-8831-89778d5b0ab4.jpg" width="256px" height="256px" title="오새암" alt="오새암"></img>
    
  천명철
  
    역할 : 팀장
    
    핵심기여역량 : 아두이노 설계, 예측모델 설계, 제품디자인 설계
   
  <img src="https://user-images.githubusercontent.com/50235391/79042795-aadde080-7c35-11ea-808c-2b4d18932ca3.jpg" width="110px" height="150px" title="천명철" alt="ME"></img>
    
    


# 개발환경


  개발 도구 : Node.js, keras, AWS Lambda, AWS DynamoDB
  
  협업 도구 : github, slack, Trello
  
  개발 방식 : github을 이용한 pull request 방식으로 agile 개발.  Trello를 이용한 프로젝트 관리. AWS Lamda를 이용한 serverless 아키텍쳐 구현. AWS DynamoDB를 이용한 NoSQL DB 사용.
