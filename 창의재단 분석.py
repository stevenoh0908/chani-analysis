#창의재단 R&E용 R.C.I. 경계값 분석 프로그램
#데이터 입력 형식은 다음 csv 파일의 형태를 전제로 함.
#=====================================
#제1종류, 제2종류
#값11, 값21
#값12, 값22
#값13, 값23
#...   ,    ...

import ba2cc

filename = None
filename = str(input('csv 파일 이름을 입력하세요: '))
fileManager = ba2cc.FileManager(filename)
cat1, cat2 = fileManager.loadData()
fileManager.closeFile()

cat1_name = 'Straight'
cat2_name = 'Sinuous'

manager = ba2cc.BAManager(cat1, cat2)
manager.setCategoryName(1, cat1_name)
manager.setCategoryName(2, cat2_name)
manager.setStep(0.0001)
border = manager.calculateEntropyBorder()
print('제시된 ' + cat1_name + '형과 ' + cat2_name + '형의 경계값: ' + str(border))
manager.displayBorderInChart(ba2cc.BAManager.OPTION_LAYERED)
