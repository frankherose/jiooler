from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import threading
import random
import string

def generate_random_email():
    """توليد بريد إلكتروني عشوائي"""
    domains = ["gmail.com"]
    username_length = random.randint(8, 15)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_random_phone():
    """توليد رقم هاتف عشوائي (لأنجولا - الكود +244)"""
    # الكود: +244 + 9 أرقام عشوائية
    numbers = random.choice( [
    "255713332307", "255651416849", "255651994739", "255651061995", "255651077306",
    "255651203410", "255651124355", "255651075380", "255651937319", "255652715307",
    "255651201327", "255654278836", "255654505820", "255654512690", "255654547071",
    "255654310649", "255653460857", "255654808398", "255654324676", "255654095275",
    "255654756243", "255654325071", "255651401723", "255654746360", "255654739007",
    "255653716854", "255651469799", "255654172642", "255654263896", "255654398793",
    "255653445836", "255654340180", "255654434567", "255654748491", "255654278621",
    "255654336744", "255654408467", "255654475242", "255654284692", "255653468016",
    "255654204478", "255654164613", "255654154654", "255654159397", "255654788834",
    "255654333903", "255654790221", "255654116945", "255654116577", "255654596555",
    "255654752929", "255654129324", "255654174274", "255651412202", "255654137114",
    "255654357200", "255654132143", "255654448624", "255654328281", "255654183976",
    "255652678345", "255654220743", "255654183642", "255651238205", "255654173762",
    "255654155964", "255654444339", "255654459902", "255654152594", "255654439279",
    "255654225439", "255651247684", "255654692693", "255654782259", "255654690406",
    "255654775142", "255654780491", "255654156497", "255654103531", "255654176275",
    "255654234482", "255652684699", "255654784174", "255654703287", "255654175896",
    "255654270710", "255654631603", "255654661492", "255651372653", "255654268451",
    "255654786719", "255654127406", "255654313538", "255651066045", "255654170345",
    "255654259911", "255654302551", "255653468368", "255654777745", "255651410648",
    "255654290510", "255654136491", "255654291115", "255654348149", "255654124227",
    "255654789241", "255654267653", "255654121491", "255654759110", "255653433907",
    "255654206936", "255654114134", "255654410239", "255654583265", "255654169412",
    "255654330810", "255651401811", "255654603809", "255651058985", "255653458365",
    "255654163684", "255654398636", "255654753248", "255654273864", "255654745500",
    "255653418820", "255654733052", "255654108379", "255654116794", "255654759898",
    "255654320931", "255654667575", "255654154796", "255654676069", "255652684518",
    "255654319720", "255654235085", "255654286702", "255654794168", "255654170387",
    "255654809240", "255654340987", "255654408850", "255654123708", "255654679224",
    "255654097002", "255654763448", "255654253554", "255652709911", "255654331424",
    "255654295214", "255651476209", "255654157270", "255654775178", "255654468829",
    "255654782380", "255654433871", "255654173062", "255651288491", "255654161364",
    "255654139677", "255654791357", "255654488900", "255654761385", "255654137269",
    "255654117223", "255654301914", "255654320462", "255654689151", "255654279618",
    "255654237028", "255654282728", "255654229444", "255652669609", "255650683712",
    "255654239060", "255650686595", "255652703789", "255654116383", "255654093319",
    "255654255247", "255654120107", "255652703904", "255654196124", "255654256515",
    "255654092911", "255653466036", "255654166808", "255654148674", "255654200557",
    "255654175534", "255777248360", "255654165470", "255652686724", "255654179329",
    "255654173868", "255654236837", "255654134301", "255654252797", "255654121098",
    "255654160593", "255651946704", "255716933305", "255650681410", "255653030755",
    "255651199426", "255652700279", "255651654239", "255717898808", "255651376320",
    "255651163408", "255651170993", "255654648971", "255651164500", "255652671462",
    "255652712872", "255651376615", "255713924285", "255651143272", "255652694533",
    "255651295851", "255651822254", "255651989724", "255651091906", "255652062554",
    "255651067500", "255651993469", "255650680088", "255651990771", "255651947885",
    "255651963227", "255651182970", "255650681503", "255650680734", "255656727036",
    "255651992658", "255712077463", "255651934491"
])
    return f"+{numbers}"

def generate_random_password():
    """توليد كلمة مرور عشوائية قوية"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choices(chars, k=12))
    # التأكد من وجود حرف كبير وصغير ورقم ورمز
    if not any(c.isupper() for c in password):
        password += random.choice(string.ascii_uppercase)
    if not any(c.islower() for c in password):
        password += random.choice(string.ascii_lowercase)
    if not any(c.isdigit() for c in password):
        password += random.choice(string.digits)
    if not any(c in "!@#$%^&*" for c in password):
        password += random.choice("!@#$%^&*")
    return password

def create_account(account_number, results):
    """دالة لإنشاء حساب جديد باستخدام threading"""
    chrome_options = Options()
   # chrome_options.add_argument("--start-maximized")
    # إضافة خيارات لتسريع العملية وتقليل استهلاك الموارد
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(190)  # زيادة إلى 120 ثانية
    driver.set_script_timeout(190)
    driver.implicitly_wait(30)
    try:
        print(f"🔄 [الحساب {account_number}] بدء عملية التسجيل...")
        
        # توليد بيانات عشوائية
        random_email = generate_random_email()
        random_phone = generate_random_phone()
        random_password = "Mmais123zx@#"
        
        print(f"📧 [الحساب {account_number}] البريد الإلكتروني: {random_email}")
        print(f"📱 [الحساب {account_number}] رقم الهاتف: {random_phone}")
        print(f"🔑 [الحساب {account_number}] كلمة المرور: {random_password}")
        
        # ========== فتح صفحة التسجيل ==========
        url = "https://fantasino.com/registration?step=1&type=email"
        driver.get(url)
        print(f"✅ [الحساب {account_number}] تم فتح صفحة التسجيل")
        
        wait = WebDriverWait(driver, 15)
        
        # ملء البريد الإلكتروني
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "email")))
        email_field.clear()
        email_field.send_keys(random_email)
        print(f"✅ [الحساب {account_number}] تم ملء البريد")
        
        # ملء رقم الهاتف
        phone_field = wait.until(EC.presence_of_element_located((By.ID, "phone")))
        driver.execute_script("arguments[0].scrollIntoView(true);", phone_field)
        #time.sleep(0.5)
        
        phone_field = wait.until(EC.element_to_be_clickable((By.ID, "phone")))
        driver.execute_script("arguments[0].value = '';", phone_field)
       #time.sleep(0.3)
        phone_field.send_keys(Keys.CONTROL + "a")
        #phone_field.send_keys(Keys.DELETE)
        #time.sleep(0.6)
        phone_field.send_keys(random_phone)
        print(f"✅ [الحساب {account_number}] تم ملء رقم الهاتف")
        
        # ملء كلمة المرور
        password_field = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_field.clear()
        password_field.send_keys(random_password)
        print(f"✅ [الحساب {account_number}] تم ملء كلمة المرور")
        
        # تمرير الصفحة إلى أسفل
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #time.sleep(1)
        
        # تحديد مربع الاشتراك
        subscribed_checkbox = wait.until(EC.presence_of_element_located((By.ID, "subscribed")))
        if not subscribed_checkbox.is_selected():
            driver.execute_script("arguments[0].click();", subscribed_checkbox)
            print(f"✅ [الحساب {account_number}] تم تحديد مربع الاشتراك")
        
        # تحديد مربع الشروط
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "terms")))
        if not terms_checkbox.is_selected():
            driver.execute_script("arguments[0].click();", terms_checkbox)
            print(f"✅ [الحساب {account_number}] تم تحديد مربع الشروط")
        
        # الضغط على زر Finish
        finish_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Finish']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", finish_button)
        #time.sleep(0.5)
        driver.execute_script("arguments[0].click();", finish_button)
        print(f"✅ [الحساب {account_number}] تم الضغط على زر Finish")
        
        # انتظار اكتمال عملية التسجيل
        time.sleep(5)
        
        # ========== الانتقال إلى صفحة الملف الشخصي ==========
        profile_url = "https://fantasino.com/account/profile/info"
        driver.get(profile_url)
        print(f"✅ [الحساب {account_number}] تم الانتقال إلى صفحة الملف الشخصي")
        
        time.sleep(0.1)
        
        # ========== الضغط على "Verify your number" ==========
        try:
            verify_number_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Verify your number']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", verify_number_element)
            #time.sleep(0.5)
            driver.execute_script("arguments[0].click();", verify_number_element)
            print(f"✅ [الحساب {account_number}] تم الضغط على 'Verify your number'")
            
            time.sleep(0.1)
            
            # ========== الضغط على زر Verify ==========
            verify_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Verify']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", verify_button)
           # time.sleep(0.5)
            driver.execute_script("arguments[0].click();", verify_button)
            print(f"✅ [الحساب {account_number}] تم الضغط على زر Verify")
            
            # حفظ بيانات الحساب الناجح
            results.append({
                "account_number": account_number,
                "email": random_email,
                "phone": random_phone,
                "password": random_password,
                "status": "success"
            })
            
            time.sleep(3)
            
        except Exception as e:
            print(f"❌ [الحساب {account_number}] خطأ في عملية التحقق: {e}")
            results.append({
                "account_number": account_number,
                "email": random_email,
                "phone": random_phone,
                "password": random_password,
                "status": "verification_failed",
                "error": str(e)
            })
        
        print(f"✅ [الحساب {account_number}] اكتملت العملية بنجاح")
        time.sleep(4)
        
    except Exception as e:
        print(f"❌ [الحساب {account_number}] حدث خطأ عام: {e}")
        results.append({
            "account_number": account_number,
            "status": "failed",
            "error": str(e)
        })
        driver.save_screenshot(f"error_screenshot_account_{account_number}.png")
        
    finally:
        driver.quit()
        print(f"🔒 [الحساب {account_number}] تم إغلاق المتصفح")
        create_account(999,results)

def main():
    """الدالة الرئيسية لتشغيل عدة حسابات بشكل متوازي"""
    
    print("=" * 60)
    print("🚀 بدء تشغيل نظام إنشاء الحسابات المتعدد")
    print("=" * 60)
    
    # تحديد عدد الحسابات المطلوب إنشاؤها
    num_accounts = 3  # يمكنك تغيير هذا الرقم حسب حاجتك
    
    print(f"📊 عدد الحسابات المطلوب إنشاؤها: {num_accounts}")
    print("=" * 60)
    
    results = []
    threads = []
    
    # إنشاء وتشغيل الخيوط
    for i in range(1, num_accounts + 1):
        thread = threading.Thread(target=create_account, args=(i, results))
        threads.append(thread)
        thread.start()
        
        # انتظار قليلاً بين بدء الخيوط لتجنب التحميل الزائد
        time.sleep(50.111)
    
    # انتظار اكتمال جميع الخيوط
    for thread in threads:
        thread.join()
    
    # عرض النتائج النهائية
    print("\n" + "=" * 60)
    print("📊 تقرير النتائج النهائي")
    print("=" * 60)
    
    successful = [r for r in results if r.get('status') == 'success']
    failed = [r for r in results if r.get('status') != 'success']
    
    print(f"✅ الحسابات الناجحة: {len(successful)}")
    print(f"❌ الحسابات الفاشلة: {len(failed)}")
    
    if successful:
        print("\n📝 تفاصيل الحسابات الناجحة:")
        for account in successful:
            print(f"  الحساب {account['account_number']}:")
            print(f"    📧 البريد: {account['email']}")
            print(f"    📱 الهاتف: {account['phone']}")
            print(f"    🔑 كلمة المرور: {account['password']}")
            print("-" * 40)
    
    if failed:
        print("\n⚠️ الحسابات الفاشلة:")
        for account in failed:
            print(f"  الحساب {account['account_number']}: {account.get('error', 'خطأ غير معروف')}")
    
    print("\n✨ تم الانتهاء من إنشاء جميع الحسابات")

while True:
    main()