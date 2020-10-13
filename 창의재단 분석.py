#창의재단 R&E용 R.C.I. 경계값 분석 프로그램
#데이터 입력 형식은 다음 csv 파일의 형태를 전제로 함.
#=====================================
#제1종류, 제2종류
#값11, 값21
#값12, 값22
#값13, 값23
#...   ,    ...

import ba2cc

cat1 = []
cat2 = []

filename = None
filename = str(input('csv 파일 이름을 입력하세요: '))
with open(filename, 'r') as file:
    while True:
        line = str(file.readline())
        if not line:
            break
        cat1.append(float(line.split(',')[0].strip()))
        cat2.append(float(line.split(',')[1].strip()))
        pass
    pass


cat1_name = 'Straight'
cat2_name = 'Sinuous'

manager = ba2cc.BAManager(cat1, cat2)
manager.setCategoryName(1, cat1_name)
manager.setCategoryName(2, cat2_name)
border = manager.calculateEntropyBorder()
print('제시된 ' + cat1_name + '형과 ' + cat2_name + '형의 경계값: ' + str(border))
manager.displayBorderInChart(ba2cc.BAManager.OPTION_LAYERED)
