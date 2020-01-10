Project1

1 bits History
command:
使用 Python 3.6,pycharm 書寫,
輸入值:
P01_1bit.in
如: T N T N T N T N T N
 
執行主程式:
P01_1bitHistory.py
執行結果:
 ['N', 'N', 'N', 'N', 'T', 'N', 'T', 'N']
 

row | 1bitHistory | word[0]word[1] | Predict | True |
00 | 1bit=0 | SN SN | Pred=N | T |
01 | 1bit=1 | WN SN | Pred=N | N |
02 | 1bit=0 | WN SN | Pred=N | T |
03 | 1bit=1 | WT SN | Pred=N | N |
04 | 1bit=0 | WT SN | Pred=T | T |
05 | 1bit=1 | ST SN | Pred=N | N |
06 | 1bit=0 | ST SN | Pred=T | T |
07 | 1bit=1 | ST SN | Pred=N | N |

系統流程：
1.讀擋 ,P01_1bit.in
2.初始陣列設定
3.做預測
4.根據結果,更新陣列,
5.迴圈,重複 3. 4. ,直到結束,
程式註解:
在主程式P01_1bitHistory.py中,以
#
#註解
#
表示註解,
參考:
Lecture5 (上課驗收日：1024) & Project 1
06-1bit history predictor example [Computer Arch - Branch]
