앱이름: main         
URL주소     views 함수이름                          비고
''              index                           # 잘 나가는 상품 10개 소개  
'about/'        about                           # 회사 소개
'contact/'      contact                         # 오시는 길


앱이름: product         
URL주소     views 함수이름                          비고
''              product                         # 상품 목록
'<int:pk>/'     productdetails                  # 상품 목록 상세 게시물 


앱이름: qna         
URL주소     views 함수이름                          비고
''              qna                             # Q&A 목록
'<int:pk>/'     qnadetails                      # Q&A 상세 게시물


앱이름: notice         
URL주소                 views 함수이름                          비고
''                          notice                          # 자유게시판, 1:1게시판 선택 페이지
'free/'                     notice_free_board_list          # 자유게시판 목록
'free/<int:pk>/'            notice_free_board_details       # 자유게시판 상세 게시물
'onenone/'                  notice_onenone_guide            # 1:1 상담 안내
'onenone/<int:pk>/'         notice_onenone_details          # 1:1 상담 상세 게시물
