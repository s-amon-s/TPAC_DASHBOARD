from django.contrib.auth.models import User

google_api = (
	('client_ID','801478657562-4t5lt35fe417lc0fbjjair4qktpd0vb2.apps.googleusercontent.com'),
	('client_secret','9qfT6_MwOqhG79kPozqoZEQs'),
	('api_key','AIzaSyDnAo_wb6IF_TxWUo3eulJLtREX5aq7Ozk')
)

LEVEL_CHOICES = [(1,1), (2,2), (3,3),(4,4), (5,5)]

Is_Important_CHOICES = [(True,'Yes'), (False,'No')]

OCCURRENCE_CHOICES = (
	('at least Once Everyday','at least Once Everyday'),
	('at least Once Everyweek','at least Once Everyweek'),
	('at least Once Everymonth','Everymonth'),
	('Once so far','Once so far'),
	('Few times so far','Few times so far')
)

OU_CHOICES = (
	('Admin and Financial (งานธุรการและการเงิน)','Admin and Financial (งานธุรการและการเงิน)'),
	('CEO & Assist (ซีอีโอและผู้ช่วย)','CEO & Assist (ซีอีโอและผู้ช่วย)'),
	('Center (ส่วนกลาง)','Center (ส่วนกลาง)'),
	('Factory (โรงงาน)','Factory (โรงงาน)'),
	('IT (IT.- เลขา)','IT (IT.- เลขา)'),
	('Sales and Marketing (บริหารงานขาย)','Sales and Marketing (บริหารงานขาย)')
	)

IS_Under_CHOICES = (
	('Khun Kevin','Khun Kevin'),
	('Khun Theerawit','Khun Theerawit'),
	('Khun Phairot','Khun Phairot'),
	('Khun Kohli','Khun Kohli'),
	('Khun Kothari','Khun Kothari'),
	('Khun Anong','Khun Anong'),
	('Khun Chakraphan','Khun Chakraphan'),
	('Khun Phairot','Khun Phairot'),
	('Khun Pricha','Khun Pricha'),
	('Khun Somchai','Khun Somchai'),
	)

DEPARTMENT_CHOICES = (
	('Account (แผนกบัญชี)','Account (แผนกบัญชี)'),
	('Assembly Injection (เตรียมวัตถุดิบ แผนกฉีด)','Assembly Injection (เตรียมวัตถุดิบ แผนกฉีด)'),
	('Blow (แผนกเป่า)','Blow (แผนกเป่า)'),
	('DOC&GMP','DOC&GMP'),
	('Engineering (แผนกวิศวกรรม)','Engineering (แผนกวิศวกรรม)'),
	('Human Resource (ฝ่ายทรัพยากรบุคคล)','Human Resource ()'),
	('Injection (แผนกฉีด)','Injection (แผนกฉีด)'),
	('Injection-Blow','Injection-Blow'),
	('IT (IT.- ECONS)','IT (IT.- ECONS)'),
	('IT (IT.- Hardware & Software)','IT (IT.- Hardware & Software)'),
	('Logistic (แผนกจัดส่ง)','Logistic (แผนกจัดส่ง)'),
	('MatPrepare','MatPrepare'),
	('Mold Shop-Blow','Mold Shop-Blow'),
	('Planning (วางแผนการผลิต)','Planning (วางแผนการผลิต)'),
	('Purchase (แผนกจัดซื้อ)','Purchase (แผนกจัดซื้อ)'),
	('Quality Assurance(ส่วนประกันคุณภาพ )','Quality Assurance(ส่วนประกันคุณภาพ )'),
	('COA (ส่วนประกันคุณภาพ )','COA (ส่วนประกันคุณภาพ )'),
	('R&D (แผนกวิจัยพัฒนาผลิตภัณฑ์)','R&D (แผนกวิจัยพัฒนาผลิตภัณฑ์)'),
	('Sales Admin (แผนกบริหารงานขาย)','Sales Admin (แผนกบริหารงานขาย)'),
	('Sales Technic','Sales Technic'),
	('Stock (แผนกคลังสินค้า)','Stock (แผนกคลังสินค้า)'),
	('Store (แผนกพัสดุ)','Store (แผนกพัสดุ)')	
)

User_Choices = []